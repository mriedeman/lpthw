from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}: ")
print(txt.read())


txt.close()
# print("Type the filename again:")
# file_again = input("> ")

# txt_again = open(file_again)

# print(txt_again.read())


# Study Drills

# 1. #Comment code
# I Understand the code so
# 4. Remove the second part of the script
# 5. Why is one way of getting the filename better than another
# https://stackoverflow.com/questions/8246822/argv-vs-raw-input
# That's because you generally should avoid interactive user input if it's not a key feature. 
# In your example: Reading from stdin or the command line allows to combine different programs and run them in scripts and so on.

# Imagine you execute a lot of code and sit in front of the screen waiting for the input request to come.
# Wasn't it better to specify all relevant information on the command line and to go and prepare a cup of coffee instead?

#Good practice

# try:
#     fn = argv[1]

# except IndexError:
#     fn = raw_input("filename > ")

# 7. Have your script call close() after open. It's impotant to close files when you are done with them.
#check