my_set1 = {"awinas", "kannan", "m", "r", "awinas", ('a', 'b')}
print(my_set1)

my_list = ["awinas", "awinas", "awinas", "kannan"]
print(my_list)
my_set2 = set(my_list)
print(my_set2)

# Set opeations

my_set1.add("add")
my_set1.remove("m")
my_set1.update("update")

print(my_set1)

my_set_x = {"awinas", "kannan", "walmart", "chennai"}
my_set_y = {"person2", "kannan", "walmart", "blr"}

my_set_z = my_set_x & my_set_y
print(my_set_z)
print(my_set_x.union(my_set_y))
# print(my_set_x | my_set_y)

my_set_sub = {"kannan", "walmart"}

print(my_set_sub.issubset(my_set_x))
print(my_set_x.issuperset(my_set_sub))

print(my_set_y.issubset(my_set_x))

# diff -> al elements in Set 1 but not in set 2
print(my_set_x.difference(my_set_y))

# intersection -> common b/w set1 * set 2
print(my_set_x.intersection(my_set_y))

# union -> all unique in set 1 & set 2
print(my_set_x.union(my_set_y))

A = [1, 2, 2, 1]
B = set([1, 2, 2, 1])
print(sum(A))
print(sum(B))

print(my_set_x.clear())
print("clear ", my_set_x, "len", len(my_set_x))
print("Before",my_set_y)
my_set_y.discard("person2")
print("after",my_set_y)


###

empty_set = set() #Creating an Empty Set
fruits = {"apple", "banana", "orange"}
fruits.update(["kiwi", "grape","apple"])
print(fruits)