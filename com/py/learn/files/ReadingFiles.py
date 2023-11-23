# file.readlines() # reads all lines as a list
# readline() # reads the next line as a string
# file.read() # reads the entire file content as a string

my_file = open("/Users/a0m0rtj/AwinasKannan/pyfiles.txt", 'r')
print(my_file.name)
file_content = my_file.read()
print(file_content)
print(file_content[3])
print(my_file.readlines())
print(my_file.closed)
print(my_file.close())
print(my_file.closed)

print("********************* auto close file ********************")
with  open("/Users/a0m0rtj/AwinasKannan/pyfiles.txt", 'r') as auto_close_file:
    print(auto_close_file)
    auto_close_file_content = auto_close_file.read()
    print(auto_close_file_content)

print(auto_close_file.closed)
# print(auto_close_file.read())
print(auto_close_file_content)

print("********************* auto close file read lines ********************")
with  open("/Users/a0m0rtj/AwinasKannan/pyfiles.txt", 'r') as auto_close_file_rl:
    print(auto_close_file_rl.readline())
    list = auto_close_file_rl.readlines()
    print(list[0])

with  open("/Users/a0m0rtj/AwinasKannan/pyfiles.txt", 'r') as auto_close_file:
    while True:
        line = auto_close_file.readline()
        if not line or 'Global' in line:
            break  # Stop when there are no more lines to read
        print(line)

print("********************* ********************")

with open("/Users/a0m0rtj/AwinasKannan/pyfiles.txt", 'r') as auto_close_file:
    i = 0;
    for line in auto_close_file:
        print("Iteration", str(i), ": ", line)
        i = i + 1
