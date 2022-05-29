from sys import argv

script, filename = argv

shrek = open(filename, 'r')

# Iterate through the lines in a file
for line in shrek.readlines():
    print(line)


shrek.close()