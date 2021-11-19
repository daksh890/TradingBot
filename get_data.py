import csv
from binance import Client
import api_config as api
client = Client(api.API_KEY, api.SECRET_KEY)

# prices = client.get_all_tickers()

# for price in prices:
#     print(price)

# print(len(prices))  

candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)

f = open('15_minutes.csv', 'w', newline='')
candlewriter = csv.writer(f, delimiter=',')

for candle in candles:
    candlewriter.writerow(candle)
print(len(candles))    

klines = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_5MINUTE, "1 Jan, 2020")
u = open('2018-now.csv', 'w', newline='')
candlewriter2 = csv.writer(u, delimiter=',')

for data in klines:
    candlewriter2.writerow(data)
print(len(klines))    

