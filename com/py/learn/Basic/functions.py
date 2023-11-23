def add(v1, v2):
    """
    Add two numbers
    :param v1:
    :param v2:
    :return:
    """
    return v1 + v2


def sub(v1, v2):
    return v1 - v2


def mul(v1, v2):
    print(v1 * v2)
    return v1 * v2


def div(v1, v2):
    print(v1 / v2)
    return v1 / v2


def math_operations(v1, v2):
    print(add(v1, v2))
    print(sub(v1, v2))
    mul(v1, v2)
    div(v1, v2)


print(math_operations(10, 5))
help(add)
print("*************** Built in functions **************")

album_rating = [1, 4, 5, 2, 1.5, 5.6, 4.5, 6.6, 4.6, 2.1, 10.1]
print(len(album_rating))
print(sum(album_rating))

##Sorted vs sort
print(album_rating.sort())
print(album_rating)
sortL = sorted(album_rating)
print(sortL)
sortL.reverse()
print(sortL)


# pass

def no_body():
    pass


print(no_body())


# Collecting args

def print_all(values):
    for val in values:
        print(val)


def print_all_arg(*params):
    for val in params:
        print(val)


name = ["a", "aw", "awi", "awin", "awina", "awinas"]
print_all(name)
print_all_arg("a", "aw", "awi", "awin", "awina", "awinas")

print("*************** Scope **************")


# Make a var global

def acc_global(p1):
    add_val = global_p1 + p1
    return add_val


global_p1 = 10
print(acc_global(1))


def make_global():
    global x
    x = 100
    pass


print(make_global())
print(x)

print("***************  **************")


def greet(name):
    return "Hello, " + name


for _ in range(3):
    print(greet("Alice"))


def MJ():
    print('Michael Jackson')


def MJ1():
    print('Michael Jackson')
    return (None)


print(MJ())
print(MJ1())


## Setting default argument values in your custom functions

def isGoodRating(rating=4):
    if (rating < 7):
        print("this album sucks it's rating is", rating)
    else:
        print("this album is good its rating is", rating)


isGoodRating()
isGoodRating(10)

###
print("*********single * args -> tuples ***********")


def printall(*args):  # All the arguments are 'packed' into args which can be treated like a tuple
    print("No of arguments:", len(args))
    for argument in args:
        print(argument)


# printAll with 3 arguments
printall('Horsefeather', 'Adonis', 'Bone')
# printAll with 4 arguments
printall('Sidecar', 'Long Island', 'Mudslide', 'Carriage')

print("*********double * args -> dictionary ***********")


def printdictionary(**args):
    for key in args:
        print(key + " : " + args[key])


printdictionary(Country='Canada', Province='Ontario', City='Toronto')

print("*********Call by reference ***********")


def addItems(list):
    list.append("Three")
    list.append("Four")


myList = ["One", "Two"]
addItems(myList)
print(myList)
