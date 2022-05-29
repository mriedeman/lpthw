from sys import argv
script, user_name, password = argv

prompt = '>>> '


print(f"Hi {user_name}, I'm the {script} script")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}")
likes = input(prompt)

print(f"Where do you live {user_name}")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input (prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")

print(f"I saved your password into the database ({password}) ")
#Study Drills

# 1. Research Zork and Adventure games. Try to find a copy and play it.
# Some other time

# 2. Change the prompt variable
#check

# 3. Add another argument and use it in your script, the same way you did in the previous exercise.

# Check 