from fugle_realtime import WebSocketClient
import websocket

class TestHttpClient(object):

    def test_config(self):
        client = WebSocketClient()
        assert client.config['api_token'] == 'demo'
        assert client.config['api_version'] == 'v0.3'

    def test_config_with_api_token(self):
        client = WebSocketClient(api_token = 'api-token')
        assert client.config['api_token'] == 'api-token'
        assert client.config['api_version'] == 'v0.3'

    def test_config_with_api_version(self):
        client = WebSocketClient(api_version = 'v0.2')
        assert client.config['api_token'] == 'demo'
        assert client.config['api_version'] == 'v0.2'

    def test_set_api_token(self):
        client = WebSocketClient()
        client.set_api_token('api-token')
        assert client.config['api_token'] == 'api-token'

    def test_set_api_version(self):
        client = WebSocketClient()
        client.set_api_version('v0.2')
        assert client.config['api_version'] == 'v0.2'

    def test_intraday_meta(self, mocker):
        mocker.patch('websocket.WebSocketApp')
        client = WebSocketClient()
        ws = client.intraday.meta(symbolId='2884')
        assert ws._url == 'wss://api.fugle.tw/realtime/v0.3/intraday/meta?symbolId=2884&apiToken=demo'

    def test_intraday_quote(self, mocker):
        mocker.patch('websocket.WebSocketApp')
        client = WebSocketClient()
        ws = client.intraday.quote(symbolId='2884')
        assert ws._url == 'wss://api.fugle.tw/realtime/v0.3/intraday/quote?symbolId=2884&apiToken=demo'

    def test_intraday_chart(self, mocker):
        mocker.patch('websocket.WebSocketApp')
        client = WebSocketClient()
        ws = client.intraday.chart(symbolId='2884')
        assert ws._url == 'wss://api.fugle.tw/realtime/v0.3/intraday/chart?symbolId=2884&apiToken=demo'
