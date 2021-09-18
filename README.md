# Fugle Realtime

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

client = HttpClient(api_token='demo')
```

#### intraday.meta

```py
client.intraday.meta(symbolId='2884')
```

#### intraday.quote

```py
client.intraday.quote(symbolId='demo')
```

#### intraday.chart

```py
client.intraday.chart(symbolId='demo')
```

#### intraday.dealts

```py
client.intraday.chart(symbolId='demo', limit=50)
```

#### intraday.volumes

```py
client.intraday.volumes(symbolId='demo')
```

### Simple WebSocket Demo

```py
import time
from fugle_realtime import WebSocketClient

def handle_message(message):
    print(message)

def main():
    client = WebSocketClient(api_token='demo')
    ws = client.intraday.quote(symbolId='2884', on_message=handle_message)
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
