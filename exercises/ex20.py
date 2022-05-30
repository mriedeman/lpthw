from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read(), end = '')

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline(), end = '')

current_file = open(input_file)

print("first let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.", end = '')

#resets where readline reads it from
rewind(current_file)

print("Let's print three lines")

current_line = 1

print_a_line(current_line, current_file)

current_line += 1

print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)