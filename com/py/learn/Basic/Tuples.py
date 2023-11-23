tuple_1 = ("awinas", 22, 0.001)
print(type(tuple_1))
print(type(tuple_1[0]))
print(type(tuple_1[1]))
print(type(tuple_1[2]))
# print(type(tuple_1[3])) # tuple index out of range

tuple_2 = ("nixen", 25)
tuple_3 = tuple_2 + tuple_1
print(tuple_3)

# slicing
print(tuple_3[0:2])
print(tuple_3[::2])

print(len(tuple_3))

# Tuples are immutable

my_tup1 = ("awinas", "kannan")
my_tup2 = ("M", "R")
my_tup3 = my_tup1 + my_tup2
print(my_tup3)
# my_tup3[2] = "Manicka" #'tuple' object does not support item assignment
print(my_tup3)

# functions
ratings = (5, 3, 4, 5, 6, 2, 1, 6, 6, 2, 6, 7, 8, 5)
sortR = sorted(ratings)
print(sortR)

# Nested Tuples
nestT = (1, 1.1, ("awinas", "kannan"), 55, ("x", 1, "y"))
print(nestT[2])
print(nestT[2][1])
print(nestT[2][1][0])
# print(nestT[3][1][0]) #TypeError: 'int' object is not subscriptable


print(nestT.index(("awinas", "kannan")))
print(nestT.index((55)))
