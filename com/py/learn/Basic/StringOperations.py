name = 'awinas kannan'
print(name)
print(name[0])
print(name[-13])  # negative indexing
print(name[0] == name[-13])

# slicing
print("Slicing " + name[0:6] + ' - ' + name[:6])
first_name = name[0:6]
last_name = name[7:1100]
print(first_name)
print(last_name)
print(name[::2])  # Get every second element. The elments on index 1, 3, 5 ...
print(name[0:6:2])  # Get every second element in the range from index 0 to index 4

# Length of element
print(len(name))

# Concat String
print(first_name + ' * ' + last_name)
print(2 * first_name)

# first_name[0] = 'k' # String are immutable # 'str' object does not support item assignment

# Escape sequence
print(" Michael Jackson \n is the best")
# r will tell python that string will be display as raw string
print(r" Michael Jackson \n is the best")

# String Methods
print('\n \nString Methods \n')
company = 'walmart'
up_company = company.upper();
print(up_company)
print(company.replace('wal', 'sams'))
print(company.find('ma'))

print(company.split('m'))
print(' a k '.strip())

print('1'+'2' )
print( type(int(12.3)))