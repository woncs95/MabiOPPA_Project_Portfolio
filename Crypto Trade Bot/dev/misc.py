import requests
import json
import pandas as pd
from keyconnect import key_connect

##connect with key
url,api_key,secret_key=key_connect()


'''def get_book(instrument_name,depth): ##depth: numbers of bids/asks
    books=requests.get(url+"public/get-book?instrument_name="+instrument_name+"&depth="+depth)
    data=json.loads(books.text)
    #for i in data['result']['data']['bids']:
    return data['result']['data']'''


def get_instruments():
    info = requests.get(url+"public/get-instruments")
    info = json.loads(info.text)
    result = info["result"]["instruments"]
    return result


def list_every_instruments():
    df = get_instruments()
    instrument_name = df["instrument_name"]
    return instrument_name  # list of instrument


def list_USDT_quote_instruments():
    df = get_instruments()
    inst_list=[]
    for instrument_info in df:
        if instrument_info['quote_currency'] == 'USDT':
            inst_list.append(instrument_info['instrument_name'])
    return inst_list
    #instrument_name=df[]



##Example1:
#total_instruments=get_instruments()
#total_instruments.to_excel("crypto_instruments.xlsx")

##Example2:
#for instrument in every_instruments():
   #candle=get_candlestick(instrument,"1D")
   #candle[539]["h"]-candle[539]["l"]
list_USDT_quote_instruments()