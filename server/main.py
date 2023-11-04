import plotly.graph_objects as go
import requests
import pandas as pd
from datetime import datetime

def show_chart():
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=1"

    payload = {}
    headers = {
    'Cookie': '__cf_bm=JsWKHrbmsQeMIxDJAxdCrTclNrmMwJz3oMf5eDZck.E-1699077170-0-AV8nxWP5DQdUixpwJ8FVvtKLr4ACb91wYSaikVwSgttTXT/Gul34rQ0Z+4ssaHeuhfoqrz8nRV2/5tLbRIZs6S4='
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()
    data_price = []
    data_time = []
    for x in data['prices']:
        data_price.append(x[1])
        data_time.append(datetime.fromtimestamp(int(x[0]/1000)))
        
    df = {
        "Date":data_time,
        "Price":data_price
    }
    fig = go.Figure([go.Scatter(x=df['Date'], y=df['Price'])])
    fig.show()
show_chart()