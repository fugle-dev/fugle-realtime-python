# Fugle Realtime

[![PyPI version][pypi-image]][pypi-url]
[![Python version][python-image]][python-url]
[![Build Status][action-image]][action-url]

> Fugle Realtime API client library for Python

## Install

```sh
$ pip install fugle-realtime
```

## Usage

The library a Python client that supports HTTP API and WebSocket.

### HTTP API

```py
from fugle_realtime import HttpClient

api_client = HttpClient(api_token='demo')
```

#### intraday.meta

```py
api_client.intraday.meta(symbolId='2884')
```

#### intraday.quote

```py
api_client.intraday.quote(symbolId='2884')
```

#### intraday.chart

```py
api_client.intraday.chart(symbolId='2884')
```

#### intraday.dealts

```py
api_client.intraday.dealts(symbolId='2884', limit=50)
```

#### intraday.volumes

```py
api_client.intraday.volumes(symbolId='2884')
```

### Simple WebSocket Demo

```py
import time
from fugle_realtime import WebSocketClient

def handle_message(message):
    print(message)

def main():
    ws_client = WebSocketClient(api_token='demo')
    ws = ws_client.intraday.quote(symbolId='2884', on_message=handle_message)
    ws.run_async()
    time.sleep(3)
    ws.close()

if __name__ == '__main__':
    main()
```

## Reference

[Fugle Realtime API](https://developer.fugle.tw)

## License

[MIT](LICENSE)

[pypi-image]: https://img.shields.io/pypi/v/fugle-realtime
[pypi-url]: https://pypi.org/project/fugle-realtime
[python-image]: https://img.shields.io/pypi/pyversions/fugle-realtime
[python-url]: https://pypi.org/project/fugle-realtime
[action-image]: https://img.shields.io/github/workflow/status/fugle-dev/fugle-realtime-py/Run%20Tests/next
[action-url]: https://github.com/fugle-dev/fugle-realtime-py/actions/workflows/pytest.yml
