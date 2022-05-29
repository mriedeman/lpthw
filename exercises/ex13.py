# PARAMETERS, UNPACKING, VARIABLES

from sys import argv  #add features to your script from the Python module set

script, first, second, third = argv #argv is the argument variable, this variable holds the arguments you pass
#to your python script when you run it 

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

#Study Drills

# 1. Try giving fewer than three arguments to your script. Explain the error

# ValueError: not enough values to unpack (expected 4, got 3)

# 2 write a script that has fewer arguments and one that has more. make sure you give the unpacked variables good names
# ex13sd2.py

# 3 Combine input with argv to make a script that get more input from a user.

# ex13sd3.py
