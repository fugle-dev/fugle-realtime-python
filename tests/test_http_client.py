from fugle_realtime import HttpClient
import requests


class TestHttpClient(object):

    def test_default_config(self):
        client = HttpClient()
        assert client.config['api_token'] == 'demo'
        assert client.config['api_version'] == 'v0.3'

    def test_config_with_api_token(self):
        client = HttpClient(api_token='api-token')
        assert client.config['api_token'] == 'api-token'
        assert client.config['api_version'] == 'v0.3'

    def test_config_with_api_version(self):
        client = HttpClient(api_version='v0.2')
        assert client.config['api_token'] == 'demo'
        assert client.config['api_version'] == 'v0.2'

    def test_set_api_token(self):
        client = HttpClient()
        client.set_api_token('api-token')
        assert client.config['api_token'] == 'api-token'

    def test_set_api_version(self):
        client = HttpClient()
        client.set_api_version('v0.2')
        assert client.config['api_version'] == 'v0.2'

    def test_intraday_meta(self, mocker):
        mocker.patch('requests.get')
        client = HttpClient()
        client.intraday.meta(symbolId='2884')
        requests.get.assert_called_once_with(
            'https://api.fugle.tw/realtime/v0.3/intraday/meta?symbolId=2884&apiToken=demo')

    def test_intraday_quote(self, mocker):
        mocker.patch('requests.get')
        client = HttpClient()
        client.intraday.quote(symbolId='2884')
        requests.get.assert_called_once_with(
            'https://api.fugle.tw/realtime/v0.3/intraday/quote?symbolId=2884&apiToken=demo')

    def test_intraday_chart(self, mocker):
        mocker.patch('requests.get')
        client = HttpClient()
        client.intraday.chart(symbolId='2884')
        requests.get.assert_called_once_with(
            'https://api.fugle.tw/realtime/v0.3/intraday/chart?symbolId=2884&apiToken=demo')

    def test_intraday_dealts(self, mocker):
        mocker.patch('requests.get')
        client = HttpClient()
        client.intraday.dealts(symbolId='2884', limit=50)
        requests.get.assert_called_once_with(
            'https://api.fugle.tw/realtime/v0.3/intraday/dealts?symbolId=2884&limit=50&apiToken=demo')

    def test_intraday_volumes(self, mocker):
        mocker.patch('requests.get')
        client = HttpClient()
        client.intraday.volumes(symbolId='2884')
        requests.get.assert_called_once_with(
            'https://api.fugle.tw/realtime/v0.3/intraday/volumes?symbolId=2884&apiToken=demo')

    def test_historical_charts(self, mocker):
        mocker.patch('requests.get')
        client = HttpClient()
        client.historical.charts('2884', '2022-02-07', '2022-02-11', 'open,high,low,close,volume,turnover,change')
        requests.get.assert_called_once_with(
            'https://api.fugle.tw/marketdata/v0.3/chart?symbolId=2884&from=2022-02-07&to=2022-02-11&fields=open%2Chigh%2Clow%2Cclose%2Cvolume%2Cturnover%2Cchange&apiToken=demo')
