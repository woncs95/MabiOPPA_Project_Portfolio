from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Hello. I am alive!"

def run():
  app.run(host="193.122.125.86",port=1234)

def keep_alive():
    t = Thread(target=run)
    t.start()