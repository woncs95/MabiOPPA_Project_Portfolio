from BackTesting import *
from misc import list_USDT_quote_instruments

# 1. Test yesterday's best coin & test their revenue of yesterday
# 2. Compare if best coin for last 550 is also best for yesterday
# 3. Test for 100 days with this strategy and watch its revenue (find everyday's best coin & add the revenue)

async def get_ror_from_days_before(k, crypto, time_frame, days_before):  # k에 따른 수익배율 백테스팅
    df = await get_candlestick(crypto, time_frame)
    df['ma5'] = df['c'].rolling(window=5).mean().shift(1)
    df['range'] = (df['h'] - df['l']) * k
    df['target'] = df['o'] + df['range'].shift(1)
    df['vol_breakout'] = df['h'] > df['target']
    df['bull'] = df['o'] > df['ma5']
    fee = 0.004
    # 수익배율 최고가가 타겟보다 낮을때
    df['ror'] = np.where(df['vol_breakout'] & df['bull'], (df['c']*(1-fee))/(df['target']*(1+fee)), 1)
    day_data = df['ror'].iloc[-days_before-1]
    return day_data


async def set_k_day_before(array, crypto, time_frame, day_before):
    k_array = array
    lst = []
    for k in k_array:
        day_ror = await get_ror_from_days_before(k, crypto, time_frame, day_before)
        lst.append(day_ror)
    max_revenue = max(lst)
    max_index = lst.index(max_revenue)
    best_k = k_array[max_index]
    return round(best_k, 1), max_revenue


async def analyse_historic_revenue(crypto,time_frame, days_before):
    k, day_revenue = await set_k_day_before(np.arange(0.1, 1.0, 0.1), crypto, time_frame, days_before)
    #day_revenue = await get_ror_from_days_before(k, crypto, time_frame, days_before)    # ror이 들어있는 df
    return k, day_revenue


async def runit():
    result = await analyse_historic_revenue('ADA_USDT', '1D', 1)
    print(result)


asyncio.run(runit())


##############################


async def make_invest_list(time_frame):
    all_instruments = list_USDT_quote_instruments()
    #zerobond_dic = {}
    best_dic = {}
    for instrument in all_instruments:
        best_k, yesterday_revenue = await set_k_day_before(np.arange(0.1, 1.0, 0.1), instrument, time_frame, 1)
        if yesterday_revenue > 1:
            best_dic[instrument] = {'best k': '', 'max revenue': '', 'max dropdown': ''}
            bestdic = best_dic[instrument]
            bestdic['best k'] = best_k
            bestdic['max revenue'] = yesterday_revenue
            pass