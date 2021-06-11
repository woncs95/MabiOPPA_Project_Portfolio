from candlestick import get_candlestick
from scipy.interpolate import *
from ticker import get_ticker
import pandas as pd


##변동성돌파전략 - 구매가 정하기
async def get_target_price(instrument,k):
    candle = await get_candlestick(instrument, "1D")
    ##today open price + (yesterday highest + yesterday lowest)*0.5
    yesterday = candle.iloc[-2]
    today = candle.iloc[-1]
    target_h = today["o"]+(yesterday["h"]-yesterday["l"])*k
    target_l = today["o"]-(yesterday["h"]-yesterday["l"])*k
    return target_h, target_l


##고점 - 구매가
async def expected_profit(instrument,k):
    target = await get_target_price(instrument,k)
    ticker = await get_ticker(instrument)
    profit = ticker["h"]-target
    return profit


##하락장일떄 - floor chart
def spline(x,y): ##spline zur Vereinfacherung Funktion
    tck=splrep(x, y, s=0)
    sp=splev(x,tck,der=0)
    df=pd.DataFrame(sp)
    return  x, sp, df


#kernregressionsschaetzer 이용
def approx_nxt_5m(x,y):
    pass


#pick all local maxima
'''def pick_peak(arr):
    _max=[]
    _dict={}

    for i in range(1,len(arr)-1):
        if arr[i-1]*1.005<arr[i]>arr[i+1]*1.005:
            _max.append(i)
        #plateaus
        elif arr[i-1]*1.005<arr[i]==arr[i+1]*1.005:
            for j in range(i, len(arr)-1):
                if arr[j]>arr[j+1]*1.005:
                    _max.append(i)
                    break
                elif arr[j]<arr[j+1]*1.005:
                    break
    _dict['pos'],_dict['peaks'] = _max, [arr[i] for i in _max]
    return _dict

#pick all local minima
def pick_low(arr):
    _min = []
    _dict = {}

    for i in range(1,len(arr)-1):
        if arr[i-1]>arr[i]*1.005<arr[i+1]:
            _min.append(i)
        #plateaus
        elif arr[i-1]>arr[i]*1.005==arr[i+1]:
            for j in range(i, len(arr)-1):
                if arr[j]*1.005<arr[j+1]:
                    _min.append(i)
                    break
                elif arr[j]*1.005>arr[j+1]:
                    break
    _dict['pos'],_dict['low'] = _min, [arr[i] for i in _min]
    return _dict'''


#변동돌파했을때 사고, get candle의 h의 90프로를 erreichen 하면 팔고 아니면 종가에 판다.