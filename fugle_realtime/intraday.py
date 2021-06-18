from pandas import to_datetime
from pandas.io.json import json_normalize
from requests import get


def chart(
    apiToken="demo",
    apiVersion="v0.2",
    host="api.fugle.tw",
    output="dataframe",
    symbolId="2884",
    oddLot=False,
):
    outputs = ["dataframe", "raw"]
    if output not in outputs:
        raise ValueError('output must be one of ["dataframe", "raw"]')
    url = "https://{}/realtime/{}/intraday/chart".format(host, apiVersion)
    params = dict(apiToken=apiToken, symbolId=symbolId, oddLot=oddLot)
    response = get(url=url, params=params)
    json = response.json()
    if response.status_code != 200:
        if output == "dataframe":
            return json_normalize(json)
        elif output == "raw":
            return json
    chart = json["data"]["chart"]
    if output == "dataframe":
        chart = [dict(at=at, **rest) for at, rest in chart.items()]
        df = json_normalize(chart)
        if "at" in df.columns:
            df["at"] = to_datetime(df["at"])
            df = df.sort_values("at")
            df = df.reset_index(drop=True)
        return df
    elif output == "raw":
        return chart


def meta(
    apiToken="demo",
    apiVersion="v0.2",
    host="api.fugle.tw",
    output="dataframe",
    symbolId="2884",
    oddLot=False,
):
    outputs = ["dataframe", "raw"]
    if output not in outputs:
        raise ValueError('output must be one of ["dataframe", "raw"]')
    url = "https://{}/realtime/{}/intraday/meta".format(host, apiVersion)
    params = dict(apiToken=apiToken, symbolId=symbolId, oddLot=oddLot)
    response = get(url=url, params=params)
    json = response.json()
    if response.status_code != 200:
        if output == "dataframe":
            return json_normalize(json)
        elif output == "raw":
            return json
    meta = json["data"]["meta"]
    if output == "dataframe":
        return json_normalize(meta)
    elif output == "raw":
        return meta


def quote(
    apiToken="demo",
    apiVersion="v0.2",
    host="api.fugle.tw",
    output="dataframe",
    symbolId="2884",
    oddLot=False,
):
    outputs = ["dataframe", "raw"]
    if output not in outputs:
        raise ValueError('output must be one of ["dataframe", "raw"]')
    url = "https://{}/realtime/{}/intraday/quote".format(host, apiVersion)
    params = dict(apiToken=apiToken, symbolId=symbolId, oddLot=oddLot)
    response = get(url=url, params=params)
    json = response.json()
    if response.status_code != 200:
        if output == "dataframe":
            return json_normalize(json)
        elif output == "raw":
            return json
    quote = json["data"]["quote"]
    if output == "dataframe":
        return json_normalize(quote)
    elif output == "raw":
        return quote


def dealts(
    apiToken="demo",
    apiVersion="v0.2",
    host="api.fugle.tw",
    output="dataframe",
    symbolId="2884",
    limit=50,
    offset=0,
    oddLot=False,
):
    outputs = ["dataframe", "raw"]
    if output not in outputs:
        raise ValueError('output must be one of ["dataframe", "raw"]')
    url = "https://{}/realtime/{}/intraday/dealts".format(host, apiVersion)
    params = dict(
        apiToken=apiToken,
        symbolId=symbolId,
        limit=limit,
        offset=offset,
        oddLot=oddLot,
    )
    response = get(url=url, params=params)
    json = response.json()
    if response.status_code != 200:
        if output == "dataframe":
            return json_normalize(json)
        elif output == "raw":
            return json
    dealts = json["data"]["dealts"]
    if output == "dataframe":
        df = json_normalize(dealts)
        if "at" in df.columns:
            df["at"] = to_datetime(df["at"])
            df = df.sort_values("at")
            df = df.reset_index(drop=True)
        return df
    elif output == "raw":
        return dealts
