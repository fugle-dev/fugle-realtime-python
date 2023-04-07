from urllib.parse import urlencode
import os
import requests


class Intraday:
    def __init__(self, config):
        self.config = config

    def meta(self, **params):
        return requests.get(self.compile_url('/intraday/meta', params)).json()

    def quote(self, **params):
        return requests.get(self.compile_url('/intraday/quote', params)).json()

    def chart(self, **params):
        return requests.get(self.compile_url('/intraday/chart', params)).json()

    def dealts(self, **params):
        return requests.get(self.compile_url('/intraday/dealts', params)).json()

    def volumes(self, **params):
        return requests.get(self.compile_url('/intraday/volumes', params)).json()

    def compile_url(self, path, params):
        params['apiToken'] = self.config['api_token']
        base_url = self.config['url'] + '/realtime/' + self.config['api_version']
        endpoint = path if (path.startswith('/')) else '/' + path
        query = '?' + urlencode(params)
        return base_url + endpoint + query
