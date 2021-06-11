import json
import requests
import pandas as pd   # pip install openpyxl nötig
from keyconnect import key_connect
import time

url, api_key, secret_key = key_connect()


async def get_candlestick(instrument_name, timeframe):
    time.sleep(1/30)
    infos = requests.get(url+"public/get-candlestick?instrument_name="+instrument_name+"&timeframe="+timeframe)
    info = json.loads(infos.text)
    result = info["result"]["data"]
    df = pd.DataFrame(result)
    return df


async def filter_candlestick(df):
    if len(df['o']) < 100:
        pass
    else:
        return df