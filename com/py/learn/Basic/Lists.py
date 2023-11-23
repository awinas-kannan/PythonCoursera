my_list = ["awinas","kannan"]
print(type(my_list))
print(my_list[1])

my_list_2 = ["M","R"]
my_list_3 = my_list + my_list_2
print(my_list_3)

# List are mutable
my_list_3[2] = "Manicka"
print(my_list_3)
my_list_3.extend(["SDE","3"])
print(my_list_3)
print(len(my_list_3))
my_list_3.append(["Walmart","Chennai"])
print(my_list_3)
print(len(my_list_3))

#split
my_str = "aw,in,as"
print(my_str.split(","))


#aliasing
#list a will change if list b is changed
my_alias = ["awinas",1,22,"wal","chennai"]
my_alias_1 = my_alias
print(my_alias_1)
my_alias_1[0] = "kannan"
print(my_alias)
print(my_alias_1)

#clone
#list a will not change if list b is changed
my_alias_3 = my_alias[2:len(my_alias)]
my_alias_4 = my_alias[:]
print(my_alias_3)
print(my_alias_4)

my_alias_4[0] = "Manicka Rajan"
print("Before" , my_alias ,"After ", my_alias_4)
print(my_alias_4)
print(my_alias)

# print(help(my_alias_4))

#delete
del(my_alias_4[0])
print(my_alias_4)

del(my_alias_4)
# print(my_alias_4) # name 'my_alias_4' is not defined


### Functions ..



fruits = ["apple", "banana", "orange"]
fruits.append("mango")
print(fruits)

