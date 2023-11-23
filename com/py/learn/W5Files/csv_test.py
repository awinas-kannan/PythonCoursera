import pandas as pd

df = pd.read_csv("addresses.csv", header=None)
print(df)
df.columns = ['First Name', 'Last Name', 'Location ', 'City', 'State', 'Area Code']
print(df)

# To select the first row
print(df.loc[0])
# To select the 0th,1st and 2nd row of "First Name" column only
print(df.loc[[0, 1, 2], "First Name"])
# To select the 0th,1st and 2nd row of "First Name" column only
print(df.iloc[[0, 1, 2], 0])

df.info()
df.describe()

print('############## Missing Data ################')
missing_data = df.isnull()
missing_data.head(5)
for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")
