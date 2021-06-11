import requests
import json
import pandas as pd
import time
from keyconnect import key_connect


def get_trades(instrument_name):
    infos = requests.get(url+"public/get-trades?instrument_name="+instrument_name)
    info = json.loads(infos.text)
    result = info["result"]["data"]
    df = pd.DataFrame(result)
    df["dataTime"] = list(map(time.ctime, df["dataTime"] / 1000))
    return df["p"][0]


url, api_key, secret_key = key_connect()
# price = get_trades("BTC_USDT")
# print(price)
