from fugle_realtime import intraday
from pandas import DataFrame
from pytest import raises


def test_intraday_chart():
    chart = intraday.chart()
    assert type(chart) is DataFrame


def test_intraday_chart_output():
    with raises(ValueError) as excinfo:
        intraday.chart(output="")
    assert excinfo.type is ValueError
    assert excinfo.value.args[0] == 'output must be one of ["dataframe", "raw"]'


def test_intraday_chart_output_dataframe():
    chart = intraday.chart(output="dataframe")
    assert type(chart) is DataFrame


def test_intraday_chart_output_raw():
    chart = intraday.chart(output="raw")
    assert type(chart) is dict


def test_intraday_meta():
    meta = intraday.meta()
    assert type(meta) is DataFrame


def test_intraday_meta_output():
    with raises(ValueError) as excinfo:
        intraday.meta(output="")
    assert excinfo.type is ValueError
    assert excinfo.value.args[0] == 'output must be one of ["dataframe", "raw"]'


def test_intraday_meta_output_dataframe():
    meta = intraday.meta(output="dataframe")
    assert type(meta) is DataFrame


def test_intraday_meta_output_raw():
    meta = intraday.meta(output="raw")
    assert type(meta) is dict


def test_intraday_quote():
    quote = intraday.quote()
    assert type(quote) is DataFrame


def test_intraday_quote_output():
    with raises(ValueError) as excinfo:
        intraday.quote(output="")
    assert excinfo.type is ValueError
    assert excinfo.value.args[0] == 'output must be one of ["dataframe", "raw"]'


def test_intraday_quote_output_dataframe():
    quote = intraday.quote(output="dataframe")
    assert type(quote) is DataFrame


def test_intraday_quote_output_raw():
    quote = intraday.quote(output="raw")
    assert type(quote) is dict


def test_intraday_trades():
    trades = intraday.trades()
    assert type(trades) is DataFrame


def test_intraday_trades_output():
    with raises(ValueError) as excinfo:
        intraday.trades(output="")
    assert excinfo.type is ValueError
    assert excinfo.value.args[0] == 'output must be one of ["dataframe", "raw"]'


def test_intraday_trades_output_dataframe():
    trades = intraday.trades(output="dataframe")
    assert type(trades) is DataFrame


def test_intraday_trades_output_raw():
    trades = intraday.trades(output="raw")
    assert type(trades) is list
