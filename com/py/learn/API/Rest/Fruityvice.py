import requests
import json
import pandas

data = requests.get("https://fruityvice.com/api/fruit/all")
print(data.text)
print(data.json())
print(data.headers)
results = json.loads(data.text)
print(results)

df = pandas.DataFrame(results)
print(df)
# The result is in a nested json format. The 'nutrition' column contains multiple subcolumns, so the data needs to be 'flattened' or normalized.

df2 = pandas.json_normalize(results)
print(df2)

cherry = df2.loc[df2["name"] == 'Cherry']
print(cherry)
print(cherry.iloc[0]['family'], cherry.iloc[0]['genus'])
