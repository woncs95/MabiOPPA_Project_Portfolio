import requests
import json
from ticker import get_ticker
url = "https://data-api.defipulse.com/api/v1/egs/api/ethgasAPI.json?api-key="
api_key="6c135fec59e900da1066a42aad8bb2400075b145741a1c520ef017e6c6e4"

def get_eth_gas_price(key):
    infos = requests.get(url+key)
    info = json.loads(infos.text)
    gas_price_range = info['gasPriceRange']
    print(info)
    for gas_price in list(gas_price_range.keys()):
        if gas_price_range[gas_price]==info['fastestWait']:
            highest_gas_price = gas_price
            return highest_gas_price

def get_eth_fee():
    gas_price = get_eth_gas_price(api_key)
    #get_ticker('ETH_USDT')
    eth_fee = 21000*gas_price/1000000000
    return eth_fee