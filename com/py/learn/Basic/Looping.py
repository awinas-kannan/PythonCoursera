print(range(10))
print(range(10, 15))

list_cols = ["red", "blue", "green", "yellow", "pink"]

# for i in range(len(list_cols)):
for i in range(0, len(list_cols)):
    print(list_cols[i])
    if i == 1 or i == 4:
        list_cols[i] = 'white'

print("************")

for each_values in list_cols:
    print(each_values)

for i, each_values in enumerate(list_cols):
    print("index : ", i, "value: ", each_values)

print(enumerate(list_cols))
print(list_cols)

print("************")

list_cols = ["white", "white", "green", "yellow", "pink"]
white_cols = []
i = 0
while list_cols[i] == 'white':
    white_cols.append(i)
    i = i + 1

print(white_cols)
