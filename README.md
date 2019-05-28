# fugle-realtime-py

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

For complete documentation of each URL specified above, please visit https://developer.fugle.tw/realtime/document.

## Contributing

Git clone the repository:

```sh
git clone https://github.com/fortuna-intelligence/fugle-realtime-py.git
cd fugle-realtime-py
```

Install [`poetry`](https://poetry.eustace.io/) if not yet installed:

```sh
curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
```

Then install dependencies and setup [`pre-commit`](https://pre-commit.com/):

```sh
poetry install
poetry run pre-commit install
```

Code formatting using [`black`](https://black.readthedocs.io/en/stable/):

```sh
poetry run black .
```

Testing using [`pytest`](https://pytest.org):

```sh
poetry run pytest
```

## Publishing

### [`PyPI`](https://pypi.org/): [`fugle-realtime`](https://pypi.org/project/fugle-realtime/)

```sh
poetry publish --build --repository pypi --username username --password password
```
