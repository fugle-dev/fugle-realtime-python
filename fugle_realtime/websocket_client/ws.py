import threading
import websocket


class WSClient:
    def __init__(self, url: str, on_message=None, on_open=None, on_close=None, on_error=None):
        self.ws = websocket.WebSocketApp(
            url,
            on_open=self._default_on_open,
            on_close=self._default_on_close,
            on_error=self._default_on_error,
            on_message=self._default_on_message,
        )

        self._url = url
        self._handle_message = on_message
        self._handle_open = on_open
        self._handle_close = on_close
        self._handle_error = on_error
        self._run_thread = None

    def run(self):
        self.ws.run_forever()

    def run_async(self):
        self._run_thread = threading.Thread(target=self.run)
        self._run_thread.start()

    def close(self):
        self.ws.close()
        if self._run_thread:
            self._run_thread.join()

    def _default_on_message(self, ws, message):
        if self._handle_message:
            self._handle_message(message)

    def _default_on_open(self, ws):
        if self._handle_open:
            self._handle_open()

    def _default_on_close(self, ws, close_status_code, close_msg):
        if self._handle_close:
            self._handle_close()

    def _default_on_error(self, ws, error):
        if self._handle_error:
            self._handle_error(error)
