import json
import websockets
import time
import pprint
from WebSockets import hmac_sha256

def key_connect():
    url = "https://api.crypto.com/v2/"

    with open('keys.json') as keys:  # time muss man durch 1000 dividieren
        information = json.load(keys)
        api_key = information['api_key']
        secret_key = information['secret_key']

    return url, api_key, secret_key


def input_connect():
    pass


