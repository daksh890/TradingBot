import csv
from binance import Client
import api_config as api

from flask import Flask, render_template

app = Flask(__name__)
client = Client(api.API_KEY, api.SECRET_KEY)

@app.route("/")
def index():
    title = "Bot by Daksh"

    info = client.get_account()
    balances = info['balances']
    data = []
    for balance in balances:
        if((float(balance['free']) > 0.00) | (float(balance['locked']) > 0.00)):
            data.append(balance)

    return render_template('index.html', title=title, my_balances=data)

@app.route("/buy")
def buy(): 
    return "<h1>buy</h1>"    


@app.route("/sell")
def sell(): 
    return "<h1>Sell</h1>"


@app.route("/settings")
def settings():
    return "<h1>Settings</h1>"    