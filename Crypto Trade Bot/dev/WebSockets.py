import pprint
import websockets
import asyncio
import json
import time
import hmac
import hashlib

async def certificate():
    with open('keys.json') as keys:  # time muss man durch 1000 dividieren
        information = json.load(keys)
        api_key = information['api_key']
        secret_key = information['secret_key']

    return api_key, secret_key

async def heart_beat():
    uri = "wss://stream.crypto.com/v2/user"
    async with websockets.connect(uri) as websocket:
        req = {
            "id": 0,
            "method": "public/heartbeat",
            "code": 0
        }
        data = json.dumps(req)
        time.sleep(5)
        await websocket.send(data)



'''async def auth():
    api_key, secret_key = await certificate()
    uri = "wss://stream.crypto.com/v2/user"

    async with websockets.connect(uri) as websocket:
        req = {
            "id": 2,
            "method": "public/auth",
            'api_key': api_key,
            "params": {
            },
            "nonce": int(time.time() * 1000)
        }
        await hmac_sha256(req)
        #print(req)
        subscribed_data = json.dumps(req)
        return subscribed_data
        #await websocket.send(subscribed_data)
        #result = await websocket.recv()
        #result = json.loads(result)
        #pprint.pprint(result)'''


async def hmac_sha256(secret_key, req):
    #api_key, secret_key = await certificate()
    paramString=""

    if "params" in req:
        for key in sorted(req['params']):
            paramString += key
            paramString += str(req['params'][key])

    sigPayload = req['method'] + str(req['id']) + req['api_key'] + paramString + str(req['nonce'])

    req['sig'] = hmac.new(
        bytes(str(secret_key), 'utf-8'),
        msg=bytes(sigPayload, 'utf-8'),
        digestmod=hashlib.sha256
    ).hexdigest()


'''async def key_socket(Api_key):
    uri = "wss://stream.crypto.com/v2/user"
    async with websockets.connect(uri) as websocket:
        req = {
        "id": 11,
        "method": "public/auth",
        "api_key": Api_key,
        "nonce": int(time.time() * 1000)
        }
        await hmac_sha256(req)
        data = json.dumps(req)
        await websocket.send(data)
        recv_data = await websocket.recv()
        recv_data = json.loads(recv_data)
        pprint.pprint(recv_data)


async def wss_key():
    await key_socket(api_key)'''


async def cryptocom_api():
    uri = "wss://uat-stream.3ona.co/v2/user"
    api_key, secret_key = await certificate()
    async with websockets.connect(uri) as websocket:
        req = {
            "method": "subscribe",
            "api_key": api_key,
            "params": {
                "channels": ["user.order.ETH_CRO"],
            },
            "nonce": int(time.time() * 1000)
        }
        subscribed_data = json.dumps(req)
        await websocket.send(subscribed_data)

        while True:
            greeting = await websocket.recv()
            greeting=json.loads(greeting)
            pprint.pprint(greeting)


async def subscribe_ticker(instrument):
    #uri = "wss://uat-stream.3ona.co/v2/market"
    uri = "wss://stream.crypto.com/v2/market"
    async with websockets.connect(uri) as websocket:
        req = {
            "id":0,
            "method": "subscribe",
            #"api_key": api_key,
            "params": {
            "channels": ["ticker." + instrument],
            },
            "nonce": int(time.time() * 1000)
        }
        subscribed_data = json.dumps(req)
        await websocket.send(subscribed_data)
        _ = await websocket.recv()
        data = await websocket.recv()
        data = json.loads(data)
        data = data['result']['data'][0]
        data = data['a']
        return data # print(data)



async def ticker():
    await subscribe_ticker("BTC_USDT")

asyncio.run(ticker())


 # time muss man durch 1000 dividieren
#information = json.load(open('keys.json'))
#api_key = information['api_key']
#secret_key = information['secret_key']
#asyncio.run(wss_key())
#asyncio.run(summary())


