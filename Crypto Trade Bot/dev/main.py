from keyconnect import key_connect
from PlotGraph import plot_floor
from VolBreakOut import *
from trades import get_trades
from BullApprox import *
from BackTesting import *
##bitcoin monitoring -- auf langer Sicht wichtig weil eine hohe kovarianz mit anderen Coins besteht.
##Details in Chartanalyse nötig


url, api_key, secret_key = key_connect()

#class floor_chart():
candle = await get_candlestick("BTC_USDT", "7D")
#candle.to_excel('candle 1m report.xlsx')
#candle.to_excel("btc.xlsx")
plot_floor(candle["t"], candle["c"])


print("moving average of yesterday is: " + str(get_yesterday_ma5("BTC_USDT")))
#print("target price today is: " + str(get_target_price("BTC_USDT",k)))
print("ticker today is: " + str(get_ticker("BTC_USDT")))
#print("expected profit today is: " + str(expected_profit("BTC_USDT",k)))
print("difference today price to ma5 is: " + str(is_it_over_ma5("BTC_USDT")))
print("traded price now is: " + str(get_trades("BTC_USDT")))



#if (current_price > target_price) and (current_price > ma5)
#sailor_and_floor("BTC_USDT")