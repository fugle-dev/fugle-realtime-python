from urllib.parse import urlencode
from .ws import WSClient


class Intraday:
    def __init__(self, config):
        self.config = config

    def meta(self, on_message=None, on_open=None, on_close=None, on_error=None, **params):
        return self.createSocket(self.compile_url('/intraday/meta', params), on_message, on_open, on_close, on_error)

    def quote(self, on_message=None, on_open=None, on_close=None, on_error=None, **params):
        return self.createSocket(self.compile_url('/intraday/quote', params), on_message, on_open, on_close, on_error)

    def chart(self, on_message=None, on_open=None, on_close=None, on_error=None, **params):
        return self.createSocket(self.compile_url('/intraday/chart', params), on_message, on_open, on_close, on_error)

    def createSocket(self, url, on_message, on_open, on_close, on_error):
        return WSClient(url, on_message, on_open, on_close, on_error)

    def compile_url(self, path, params):
        params['apiToken'] = self.config['api_token']
        baseUrl = self.config['url'] + '/' + self.config['api_version']
        endpoint = path if (path.startswith('/')) else '/' + path
        query = '?' + urlencode(params)
        return baseUrl + endpoint + query
