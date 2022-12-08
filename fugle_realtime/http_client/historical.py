from urllib.parse import urlencode, urljoin
import os
import requests


class Historical:
    def __init__(self, config):
        self.config = config

    # from is reserved keyword in Python
    def charts(self, symbolId, start, end, fields):
        params = {}
        if symbolId is not None: params['symbolId'] = symbolId
        if start is not None: params['from'] = start
        if end is not None: params['to'] = end
        if fields is not None: params['fields'] = fields

        return requests.get(self.compile_url('/chart', params)).json()

    def compile_url(self, path, params):
        source = 'marketdata'
        params['apiToken'] = self.config['api_token']
        base_url = urljoin(self.config['url'], os.path.join(
            source, self.config['api_version']))
        endpoint = path if (path.startswith('/')) else '/' + path
        query = '?' + urlencode(params)
        return base_url + endpoint + query
