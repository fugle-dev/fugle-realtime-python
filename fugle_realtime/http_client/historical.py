from urllib.parse import urlencode
import os
import requests


class Historical:
    def __init__(self, config):
        self.config = config

    # from is reserved keyword in Python
    def candles(self, symbolId, start, end, fields):
        params = {}
        if symbolId is not None: params['symbolId'] = symbolId
        if start is not None: params['from'] = start
        if end is not None: params['to'] = end
        if fields is not None: params['fields'] = fields

        return requests.get(self.compile_url('/candles', params)).json()

    def compile_url(self, path, params):
        params['apiToken'] = self.config['api_token']
        base_url = self.config['url'] + '/marketdata/' + self.config['api_version']
        endpoint = path if (path.startswith('/')) else '/' + path
        query = '?' + urlencode(params)
        return base_url + endpoint + query
