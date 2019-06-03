# fugle-realtime-py

![Travis (.org)](https://img.shields.io/travis/fortuna-intelligence/fugle-realtime-py.svg)
![PyPI](https://img.shields.io/pypi/v/fugle-realtime.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/fugle-realtime.svg)
![PyPI - Downloads](https://img.shields.io/pypi/dm/fugle-realtime.svg)

Fugle Realtime Python is a Python package to query realtime stock quote of Taiwan market through API provided by [Fugle](https://www.fugle.tw/).

Currently supported exchanges are [Taiwan Stock Exchange (TWSE)](http://www.twse.com.tw/) and [Taipei Exchange(TPEx)](https://www.tpex.org.tw/).

## Documentations

-  [Fugle Developer](https://developer.fugle.tw/)

    - https://developer.fugle.tw/realtime

-  [PyPI](https://pypi.org/)

    - https://pypi.org/project/fugle-realtime/

## Installation

```sh
pip install fugle-realtime
```

This package is compatible with Python 3.6 and 3.7.

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
