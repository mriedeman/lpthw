#READING AND WRITING FILES

#CLOSE - Closes the file. Like File -> Save in your editor
#READ - Reads the contents of the file. You can assign the result to a variable
#READLINE - Reads just one line of a text file. 
#TRUNCATE - Empties the file. **Watch out if you care about the file.**
#WRITE('stuff') - Writes "stuff" to the file.
#SEEK(0) - Move the read/write location to the beginning of the file.

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")


line1 = input("line 1: ") + "\n"
line2 = input("line 2: ") + "\n"
line3 = input("line 3: ") + "\n"

print("I'm going to write these to the file.")

lines = line1 + line2 + line3

target.write(lines)

print("And finally, we close it.")
target.close()

#Study Drills

# 1. Do you understand it?
# Yep

# 2. Write a script similar to the last exercise that uses read and argv to read the file you just created.

# Wrote a script that reads a text file line by line.

# 3. There's too much repetition in this file. Use strings, formats, and escapes to print out line1, line2, and line 3 with just one target.write() command instead of six
# Done
