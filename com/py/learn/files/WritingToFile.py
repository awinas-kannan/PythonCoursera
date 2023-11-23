# file.write(content) # writes a string to the file
# file.writelines(lines) # writes a list of strings to the file

with  open("/Users/a0m0rtj/AwinasKannan/pyfiles.txt", 'r') as read_file:
    with  open("/Users/a0m0rtj/AwinasKannan/pyfiles_1.txt", 'w') as write_file:
        for line in read_file:
            write_file.write(line)

with open('/Users/a0m0rtj/AwinasKannan/pyfiles.txt', 'r+') as testwritefile:
    testwritefile.seek(0, 0)  # write at beginning of file
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("Line 4" + "\n")
    testwritefile.write("finished\n")
    testwritefile.seek(0, 0)
    print(testwritefile.read())

with open('/Users/a0m0rtj/AwinasKannan/pyfiles.txt', 'r+') as testwritefile:
    testwritefile.seek(0, 0)  # write at beginning of file
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("Line 4" + "\n")
    testwritefile.write("finished\n")
    # Uncomment the line below
    testwritefile.truncate()
    testwritefile.seek(0, 0)
    print(testwritefile.read())

#.truncate() method at the end of your data. This will reduce the file to your data and delete everything that follows.
