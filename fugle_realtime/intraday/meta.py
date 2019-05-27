from pandas.io.json import json_normalize
from requests import get


def meta(
    apiToken="demo",
    apiVersion="v0",
    host="api.fugle.tw",
    output="pandas",
    symbolId="2884",
):
    url = "https://{}/realtime/{}/intraday/meta".format(host, apiVersion)
    params = dict(apiToken=apiToken, symbolId=symbolId)
    response = get(url=url, params=params)
    json = response.json()
    if response.status_code != 200:
        if output == "pandas":
            return json_normalize(json)
        else:
            return json
    meta = json["data"]["meta"]
    if output == "pandas":
        return json_normalize(meta)
    else:
        return meta
