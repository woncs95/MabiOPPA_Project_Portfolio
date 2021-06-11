from BackTesting import *
from misc import list_USDT_quote_instruments
import pandas as pd
import asyncio
from VolBreakOut import get_target_price
from BullApprox import is_over_ma5
from WebSockets import subscribe_ticker
import websockets
from accountBalance import account_balance
import datetime



async def make_invest_list(time_frame):
    all_instruments = list_USDT_quote_instruments()
    zerobond_dic = {}
    best_dic = {}
    for instrument in all_instruments:
        best_k, max_revenue = await set_k(np.arange(0.1, 1.0, 0.1), instrument, time_frame)
        max_dropdown = await get_mdd(best_k, instrument, time_frame)
        #print(best_k, max_revenue, max_dropdown)
        if max_dropdown == 0 and max_revenue > 1:
            zerobond_dic[instrument] = {'best k': '', 'max revenue': '', 'max dropdown': ''}
            zerodic = zerobond_dic[instrument]
            zerodic['best k'] = best_k
            zerodic['max revenue'] = max_revenue
            zerodic['max dropdown'] = max_dropdown
        elif max_revenue > 4:
            best_dic[instrument] = {'best k': '', 'max revenue': '', 'max dropdown': ''}
            bestdic = best_dic[instrument]
            bestdic['best k'] = best_k
            bestdic['max revenue'] = max_revenue
            bestdic['max dropdown'] = max_dropdown
    df1 = pd.DataFrame(zerobond_dic)
    df1 = df1.T  # transpose df
    df2 = pd.DataFrame(best_dic)
    df2 = df2.T
    zeromax = df1.idxmax()
    revenuemax = df2.idxmin()
    crypto_max_rev_in_zero = zeromax['max revenue']
    crypto_min_mdd_in_best_revenue = revenuemax['max dropdown']
    df1 = df1.T
    df2 = df2.T
    zerobest_k = df1[crypto_max_rev_in_zero]['best k']
    revenuebest_k = df2[crypto_min_mdd_in_best_revenue]['best k']
    print(f"Today's invest is: {crypto_max_rev_in_zero} and {crypto_min_mdd_in_best_revenue}")
    return crypto_max_rev_in_zero, zerobest_k , crypto_min_mdd_in_best_revenue, revenuebest_k

    # df1.to_excel('zerobondreport.xlsx')
    # pass

async def invest_today_crypto():
    crypto_max_rev_in_zero, zerobest_k, crypto_min_mdd_in_best_revenue, revenuebest_k = (),(),(),()
    zerotarget_h, zerotarget_l = 0, 0
    revenuetarget_h, revenuetarget_l = 0, 0
    while True:
        now = datetime.datetime.now(datetime.timezone.utc)
        if now.hour == 0 and now.minute == 0 and (20 <= now.second < 30):
            crypto_max_rev_in_zero, zerobest_k, crypto_min_mdd_in_best_revenue, revenuebest_k = await make_invest_list(
                '1D')
            zerotarget_h, zerotarget_l = await get_target_price(crypto_max_rev_in_zero, zerobest_k)
            revenuetarget_h, revenuetarget_l = await get_target_price(crypto_min_mdd_in_best_revenue, revenuebest_k)

        best_zero_ticker = await subscribe_ticker(crypto_max_rev_in_zero)
        best_rev_ticker = await subscribe_ticker(crypto_min_mdd_in_best_revenue)

        best_zero_bull = await is_over_ma5(crypto_max_rev_in_zero, best_zero_ticker)
        best_revenue_bull = await is_over_ma5(crypto_min_mdd_in_best_revenue, best_rev_ticker)

        if best_zero_bull is True and best_zero_ticker-zerotarget_h >=0:

            pass
        if best_revenue_bull is True and best_rev_ticker-revenuetarget_h >=0:
            pass



async def run_invest_list():
    await make_invest_list('1D')


asyncio.run(run_invest_list())
