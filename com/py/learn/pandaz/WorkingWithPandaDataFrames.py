import pandas as pd

songs = {"ALBUM": ["song 1", "song 2", "song 3", "song 4", "song 5"],
         "RELEASE DATE": [1991, 1992, 1993, 1994, 2000],
         "LENGTH": ["1 min", "3 min", "2 min", "2 min", "5 min"],
         "MOVIE": ["Movie 1", "Movie 3", "Movie 3", "Movie 4", "Movie 5"]}
df = pd.DataFrame(songs)
print(df)
print(type(df))
print(type(df["ALBUM"]))
print(type(df[["ALBUM"]]))

print(df[["ALBUM"]])
#### To view the column as a series, just use one bracket:

print(df["ALBUM"])
# print(df["ALBUM", "MOVIE"]) Not Possible
print(df[["ALBUM", "MOVIE"]])
print("*****************")
print(df.iloc[2])
print(df["LENGTH"].unique())
print("******* DF **********")
print(df['RELEASE DATE'] >= 1992)
high_above_1992 = df[df['RELEASE DATE'] >= 1992]
print(high_above_1992)
print("******* Functions **********")
print(df.shape)
df.info()
df.describe()

# loc() and iloc() functions
# loc[row_label, column_label]
# iloc[row_index, column_index]
print("loc() and iloc() functions")
print(df.loc[4, 'ALBUM'])
# print(df.loc['song 1', 'ALBUM'])
print(df.iloc[4, 0])

print("***********************")

df2 = df
df2 = df2.set_index("MOVIE")
# print(df2.values)
df2.head()

# Slicing
print("######### SLICE #########")

print(df.iloc[0:3, 0])
print(df.iloc[0:3, 0:4])
print(df.loc[0:3, 'ALBUM':'LENGTH'])

# df.ix


print("$$$$$$$$$$$$$$$$$$$$$$$$$$$")

list_of_list = [['Song 1', 'Album 1', '1 min'], ['Song 2', 'Album 2', '2 min'], ['Song 4', 'Album 4', '4 min'],
        ['Song 5', 'Album 5', '5 min']]
df_l = pd.DataFrame(list_of_list,columns=['Song name','Album name','duration'])
print(df_l)