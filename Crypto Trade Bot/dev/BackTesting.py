import numpy as np
from candlestick import get_candlestick
import asyncio


async def get_ror(k, crypto, time_frame):  # k에 따른 수익배율 백테스팅
    df = await get_candlestick(crypto, time_frame)
    df['ma5'] = df['c'].rolling(window=5).mean().shift(1)
    df['range'] = (df['h'] - df['l']) * k
    df['target'] = df['o'] + df['range'].shift(1)
    df['vol_breakout'] = df['h'] > df['target']
    df['bull'] = df['o'] > df['ma5']
    fee = 0.004
    # 수익배율 최고가가 타겟보다 낮을때
    df['ror'] = np.where(df['vol_breakout'] & df['bull'], (df['c']*(1-fee))/(df['target']*(1+fee)), 1)
    lenror=len(df['ror'])
    ror = np.cumprod(df['ror'])[lenror-1]
    return df, ror


# 알고리즘 진행하면서 지난 하루 수익을 확인해본다.
async def get_last_day_ror(df):
    last_ror = df['ror'].iloc[-2]
    return last_ror



# time_frame 단위로 k 세팅 가능 ##gucken, wie der Preis von gestern aussieht Preis >= 1.0 => brint zu einem schlechteren Ergebnis
async def set_k(array, crypto, time_frame):
    k_array = array
    lst = []
    for k in k_array:
        df, ror = await get_ror(k, crypto, time_frame)
        lst.append(ror)
    max_revenue = max(lst)
    max_index = lst.index(max_revenue)
    best_k = k_array[max_index]
    return round(best_k, 1), max_revenue


async def get_mdd(k, crypto, time_frame):
    df, _ = await get_ror(k, crypto, time_frame)
    df['hpr'] = df['ror'].cumprod()
    df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
    max_dd=df['dd'].max()
    return max_dd









#df['shortdropdown']=(df['h']-df['l'])/df['h']*100
#df.to_excel('shortdropdown.xlsx')
#print((max(df['shortdropdown'])-min(df['shortdropdown']))/2)
#max_point, max_revenue = set_k(np.arange(0.1, 1.0, 0.1),"BTC_USDT","1D")
#print(max_point, mv)
#print(get_mdd(max_point,"BTC_USDT","14D"))
#print(set_k(np.arange(0.1, 1.0, 0.1), "CRO_USDT"))
#min_dd(np.arange(0.1, 1.0, 0.1), "CRO_USDT")