import datetime
import pandas as pd
import requests
import json
from keyconnect import key_connect
import time
from WebSockets import hmac_sha256
import asyncio


async def account_balance():
    url, api_key, secret_key = key_connect()
    req = {
        "id": 0,
        "method": "private/get-account-summary",
        "api_key": api_key,
        "params": {},
        "nonce": int(time.time()*1000)
    }
    await hmac_sha256(secret_key, req)
    balance = requests.post(url+"private/get-account-summary", json=req, headers={'Content-Type':'application/json'})
    info = json.loads(balance.text)
    balance = info['result']['accounts']
    return balance


async def balance_USDT():
    balance = await account_balance()
    df = pd.DataFrame(balance)
    df.to_csv('asdf.csv')
    row = df[df['currency'].str.match('USDT')]
    value = float(row['available'])
    return value


print(asyncio.run(balance_USDT()))