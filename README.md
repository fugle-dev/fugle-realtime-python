# fugle-realtime-py

Fugle Realtime Python

## Documentation

https://developer.fugle.tw/realtime

## Installation

```sh
pip install fugle-realtime
```

## Usage

```py
from fugle_realtime import intraday
```

### [`intraday.chart`](https://developer.fugle.tw/realtime/document#/Intraday/get_intraday_chart): https://api.fugle.tw/realtime/v0/intraday/chart

```py
intraday.chart(apiToken="demo", output="dataframe", symbolId="2884")
```

### [`intraday.meta`](https://developer.fugle.tw/realtime/document#/Intraday/get_intraday_meta): https://api.fugle.tw/realtime/v0/intraday/meta

```py
intraday.meta(apiToken="demo", output="dataframe", symbolId="2884")
```

### [`intraday.quote`](https://developer.fugle.tw/realtime/document#/Intraday/get_intraday_quote): https://api.fugle.tw/realtime/v0/intraday/quote

```py
intraday.quote(apiToken="demo", output="dataframe", symbolId="2884")
```

### [`intraday.trades`](https://developer.fugle.tw/realtime/document#/Intraday/get_intraday_trades): https://api.fugle.tw/realtime/v0/intraday/trades

```py
intraday.trades(apiToken="demo", output="dataframe", symbolId="2884")
```

`output="dataframe"` will return [pandas](https://pandas.pydata.org/) [`DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html), which is the default. `output="raw"` will return [python](https://www.python.org/) built-in [`dict`](https://docs.python.org/3/library/stdtypes.html#dict) or [`list`](https://docs.python.org/3/library/stdtypes.html#list) accordingly.

`symbolId="2884"` is only allowed when `apiToken="demo"`. To access more `symbolId`, you will have to get your own `apiToken`. Please visit https://developer.fugle.tw/realtime/apiToken for detailed instructions.

For complete documentation of each URL and its parameters in association with the corresponding function and its arguments specified above, please visit https://developer.fugle.tw/realtime/document.
