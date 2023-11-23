my_dict = {"awinas": 22, "karthi": 23, "rames": 24, "upper": ["A", "B", "C"], "lower": ('a', 'b', 'c')}
print(my_dict)
print(my_dict.get("awinas"))
print(my_dict.get("lower"))
print(my_dict["upper"])
my_dict["new"] = 100.1
del(my_dict["karthi"])
# del(my_dict["ak"])
print(my_dict)

print("awinas" in my_dict)
print("ak" in my_dict)
print(my_dict.keys())
print(len(my_dict))


print(my_dict.items(),type(my_dict.items()))
print(list(my_dict.items()))

if "awinas" in my_dict:
    print("Name exists in the dictionary.")