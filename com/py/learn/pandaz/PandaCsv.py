import pandas as pd

df = pd.read_csv("TopSellingAlbums.csv")
# print(df.info())
print(df)
print(df.head())

new_index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
df_new = df
df_new.index = new_index
print(df_new.loc['a', 'Artist'])
print(df_new.loc['a':'d', 'Artist'])

print(df_new)
