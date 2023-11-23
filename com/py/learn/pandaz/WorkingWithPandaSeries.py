import pandas as pd

data = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 60]
s = pd.Series(data)
print(s.values)
print(s.shape)
print(s.iloc[3])
print(s[1:4])
print(s.index)
print(s.unique())
print(s.get(1))
print(s.sum())
print(s.sort_values())
list = s.sort_values()

for intval in list:
    print("int valu ", intval)
