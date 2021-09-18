from ..base_client import BaseClient
from .intraday import Intraday

FUGLE_REALTIME_WS_URL = 'wss://api.fugle.tw/realtime'


class WebSocketClient(BaseClient):
    def __init__(self, api_token='demo', api_version='v0.3'):
        super().__init__(api_token, api_version, url=FUGLE_REALTIME_WS_URL)

    @property
    def intraday(self):
        return Intraday(self.config)
