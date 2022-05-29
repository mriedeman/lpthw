# creates a variable equal to 10, but joke is that its actually binary
types_of_people = 10

#inserts 10 into the string
x = f"There are {types_of_people} types of people."
#creates a string called binary
binary = 'binary'
#creates a string called "don't"
do_not = "don't"

#Two instances where a string is placed inside a string
y = f"Those who know {binary} and those who {do_not}"

print(x)
print(y)

#two more instances where a string is placed inside a string
print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
#create string that can take a variable
joke_evaluation = "Isn't that joke so funny?! {}"


#used the format method to insert a variable value (True/False in this case) into the already created string
print(joke_evaluation.format(hilarious))

w = "this is the lef side of..."
e = "a string with a right side"

print(w + e)

# Study drills
# 1. Comment code
# 2. Find all places where a string is placed inside a string
# 3. Double check
# pretty sure its 4, other instances placed inside strings aren't string type
# 4. What does adding w + e create a longer string
# + symbols concatenates strings