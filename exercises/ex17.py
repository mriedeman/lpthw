from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how? just apply .read() after the open function

in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Output file exist? {exists(to_file)}")
# print("Ready, hit RETURN TO CONTINUE, CTRL-C to abort.")
# input()

out_file = open(to_file, 'w')
out_file.write(indata)
print("Copying files.....")
print("Task Completed")

out_file.close()
in_file.close()

# Study Drills

# 1. Shorten the script by removing features.
# ex17sd2.py
# 2. See how short you can make the script.
# ex17sd2.py


