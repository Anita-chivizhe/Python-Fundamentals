# Task
# Get two person name and height
# Case 1:
# Ethan, Luvuyo
# 185cm, 175cm
# Ethan is taller than Luvuyo by 10cm


# Case 2:
# Ethan, Luvuyo
# 185cm, 194cm
# Luvuyo is taller than Ethan by 9cm


name_one = input("Please enter your name? ")
height_one = float(input("Please enter your height"))

name_two = input("Please enter your name? ")
height_two = float(input("Please enter your height"))

height_diff = float(height_one) - float(height_two)

if height_one > height_two:
    print("{name_one} is taller than {name_two} by {height_diff} cm ")
else:
    print(f"{name_two} is shorter than {name_two} by {height_diff} cm ")
# Task 2
name_one = input("Please enter your name? ")
height_one = float(input("Please enter your height"))

name_two = input("Please enter your name? ")
height_two = float(input("Please enter your height"))

height_diff = float(height_one) - float(height_two)

if height_one > height_two:
    print("{name_one} is taller than {name_two} by {height_diff} cm ")
elif height_one > height_two:
    print(f"{name_two} is shorter than {name_two} by {height_diff} cm ")
else:
    print(f"{name_one} is the same height as {name_two} by {height_diff} cm ")
