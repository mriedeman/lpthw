
print("What is your desired level you'd like to achieve at learning Japanese? (N1 is highest, N5 is lowest)", end = ' ')
level = input("Valid inputs are 'N1' 'N2' 'N3' 'N4' 'N5'")

print("How much time in hours can you study per day", end = ' ')
time = int(input("Valind inputs are numbers..examples : 0.5, 1, 2, 3 ,4 "))

study_hours = {
    'N1':5000,
    'N2':4000,
    'N3':3000,
    'N4':2000,
    'N5':1000,
}

#try:
days = study_hours[level] / time / 365
#except: KeyError

print(f"To reach a {level} level of Japanese, it will take you {days} years")

