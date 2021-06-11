from candlestick import get_candlestick
from ticker import get_ticker
from WebSockets import subscribe_ticker

# 5일 이동평균 구하기
async def get_yesterday_ma5(instrument):
    candle = await get_candlestick(instrument, "1D")
    ma = candle["c"].rolling(5).mean()
    return ma.iloc[-1]


# 상승장인가 하락장인가?
async def is_over_ma5(instrument, cur_price):
    ma = await get_yesterday_ma5(instrument)
    difference = cur_price-ma
    if difference >= 0:
        return True
    else: return False