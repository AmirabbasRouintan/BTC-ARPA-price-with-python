import requests
import json
import time
import os
import tkinter as tk

url_btc = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
url_arpa = 'https://api.binance.com/api/v3/ticker/price?symbol=ARPAUSDT'

def update_prices():
    try:
        response_btc = requests.get(url_btc)
        data_btc = json.loads(response_btc.text)
        price_btc = float(data_btc['price'])
        response_arpa = requests.get(url_arpa)
        data_arpa = json.loads(response_arpa.text)
        price_arpa = float(data_arpa['price'])
        os.system("clear")
        btc_label.config(text=f'BTCUSDT: {price_btc:.2f}')
        arpa_label.config(text=f'ARPAUSDT: {price_arpa:.8f}')
    except:
        os.system("clear")
        btc_label.config(text="BTCUSDT: ...")
        arpa_label.config(text="ARPAUSDT: ...")
    root.after(1000, update_prices)

root = tk.Tk()
root.title("Crypto Prices")

btc_label = tk.Label(root, font=("Arial", 20))
btc_label.pack(pady=10)

arpa_label = tk.Label(root, font=("Arial", 20))
arpa_label.pack(pady=10)

update_prices()

root.mainloop()

