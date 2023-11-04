from aiohttp import web
import aiohttp_cors
from aiohttp_route_middleware import UrlDispatcherEx
import plotly.graph_objects as go
import requests
import pandas as pd
from datetime import datetime


app = web.Application(router=UrlDispatcherEx())

cors = aiohttp_cors.setup(app)

cors = aiohttp_cors.setup(app, defaults={
    "*": aiohttp_cors.ResourceOptions(
        allow_credentials=True,
        expose_headers="*",
        allow_headers="*",
    )
})


def show_chart():
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=30"

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

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)


app.router.add_get('/test', handle)
app.router.add_post('/data', show_chart)

for route in list(app.router.routes()):
    cors.add(route)

web.run_app(app,port=9000)
