#number of cars
cars = 100
#average passenger capacity for the fleet
space_in_a_car = 4
#Number of drivers available
drivers = 30
#Number of passengers needed to be driven
passengers = 90

#Number of empty cars 
cars_not_driven = cars - drivers

#Number of cars to be driven
cars_driven = drivers

#The number of people that can be transported
carpool_capacity = cars_driven * space_in_a_car

#Estimated number of passengers per car
average_passengers_per_car = passengers / cars_driven

print(f"There are {cars} cars available")
print(f"There are only {drivers} drivers available")
print(f"There will be {cars_not_driven} empty cars today.")
print(f"We can transport {carpool_capacity} people today")
print(f"We have {passengers} to carpool today")
print(f"We need to put about {average_passengers_per_car} in each car")


# Study drills

# 1. I used 4.0 for space_in_a_car, but is that necessary? What happens if it's just 4

# We can transport 120 people today is printed instead of We can transport 120.0 people today

# 2. Remember 4.0 is a floating point number. It's a number with a decimal point. Divide by a floating point to get a floating point if you need it.

# 3. Comment above each of the variable assignments.

# 4. = assigns the value on the right to a variable on the left
# 
# 5. _ is used instead of space for items expressed with multiple words
# 
# 6.  Run python from terminal and use as a calculator, but this time use variable names for calculations.

