import requests
import json
import pandas as pd
from keyconnect import key_connect

url, api_key, secret_key = key_connect()


async def get_ticker(instrument_name):  # a:price of latest trade
    infos = requests.get(url + "public/get-ticker?instrument_name=" + instrument_name)
    info = json.loads(infos.text)
    result = info["result"]["data"]
    df = pd.Series(result)
    return df


print(get_ticker('ETH_USDT'))
