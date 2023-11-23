try:
    my_file = open("/Users/a0m0rtj/AwinasKannan/exception.txt", 'r')
    print("My File", my_file.name)
    my_file.write("Awinas")
    # my_file_1 = open("/Users/a0m0rtj/AwinasKannan/xxx.txt",'r')
    # print("My File",my_file_1.name)
except IOError:
    print("Cannot Write IO Error")
else:
    print("Successfully written")
finally:
    my_file.close()
    print("My File closed")

print("******************************")

try:
    my_file = open("/Users/a0m0rtj/AwinasKannan/exception.txt", 'w')
    print("My File", my_file.name)
    my_file.write("Awinas")
    # my_file_1 = open("/Users/a0m0rtj/AwinasKannan/xxx.txt",'r')
    # print("My File",my_file_1.name)
except IOError:
    print("IO Error")
else:
    print("Successfully written")
finally:
    my_file.close()
    print("My File closed")

print("******************************")

# using Try- except
try:
    result = 10 / 0
except ZeroDivisionError as zde:
    print("Error: Cannot divide by zero", zde)
    print(f"Error: Cannot divide by zero {zde}")

try:
    num = int("abc")
except ValueError:
    print("Error ValueError")

try:
    my_list = ["a", "b", "c"]
    print(my_list[1])
    str = my_list[5]
except IndexError:
    print("Error: IndexError")

try:
    my_dict = {"A": 1, "B": 2, "C": 3}
    print("my_dict.get(\"A\")", my_dict.get("A"))
    print("my_dict.get("F")", my_dict.get("F"))
    str = my_dict["F"]
except KeyError as KE:
    print(f"Error: KeyError {KE}")

try:
    result = "hello" + 5
except TypeError:
    print("Error: TypeError")

try:
    text = "example"
    length = len(text)  # No AttributeError, correct method usage
    missing = text.some_method()
except AttributeError:
    print("Error: AttributeError")

print("******************************")

a = 1
try:
    b = int(input("Please enter a number to divide a  ->  "))
    a = a / b
    print("Success a=", a)
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except (ValueError):
    print("You did not provide a number")
except:
    print("Something went wrong")

print("******************************")

import math


def perform_calculation(number1):
    try:
        result = math.sqrt(number1)
        print(f"Result: {result}")
    except ValueError:
        print("Error: Invalid input! Please enter a positive integer or a float value.")


number1 = float(input("Enter the number:-"))
perform_calculation(number1)

print("******************************")


def complex_calculation(num):
    try:
        result = num / (num - 5)
        print(f"Result: {result}")
    except Exception as e:
        print("An error occurred during calculation.")

user_input = float(input("Enter a number: "))
complex_calculation(user_input)

