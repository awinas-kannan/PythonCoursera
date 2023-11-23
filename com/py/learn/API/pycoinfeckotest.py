from pycoingecko import CoinGeckoAPI
import pandas as pd

cg = CoinGeckoAPI()
bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='inr', days=5)
print(bitcoin_data)
print(type(bitcoin_data))
print(bitcoin_data['prices'])
bitcoin_prices_data = bitcoin_data['prices']

df = pd.DataFrame(bitcoin_data)
print(type(df))
print(df)

# Convert to DF
df = pd.DataFrame(bitcoin_prices_data)
print(type(df))
print(df)

df = pd.DataFrame(bitcoin_prices_data, columns=['Time', 'Price'])
print(type(df))
print(df)
time_series = df['Time']
print(type(time_series))
df['Time'] = pd.to_datetime(df['Time'], unit='ms')
print(df)

candle_Stick = df.groupby(df['Time'].dt.date).agg({'Price', ['min', 'max', 'first', 'last']})
print(candle_Stick)
