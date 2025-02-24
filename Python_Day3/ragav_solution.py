# secret_message = "   Programming in Python is not only powerful but also fun!   "
# clean_secret_message = secret_message.strip()
# clean_upper_msg = clean_secret_message.upper()
# print(clean_upper_msg)
# print(clean_upper_msg[15:21] + "-" + clean_upper_msg[34:42])


secret_message = "   Programming in Python is not only powerful but also fun!   "
# clean_secret_message = secret_message.strip()
# clean_upper_msg = clean_secret_message.upper()

# Dot Chaining
clean_upper_msg = secret_message.strip().upper()
print(clean_upper_msg)
print(clean_upper_msg[15:21] + "-" + clean_upper_msg[34:42])


# Task 1.1
# Expected Output
# "PYTHON-POWERFUL"


# 1. Solve
# 2. Make it better


# Task 1.2
flipped_message = "!nuf sseldnE dna seitinutroppo lufrewop htiw nohtyP"

# Expected Output
# "python 🗡️ powerful 🌸"

flipped_message_reverse = flipped_message[::-1].lower()
print(f"{flipped_message_reverse[0:6]} 🗡️ {flipped_message_reverse[12:20]} 🌸")


# Task 1.3

# After the 🔑
message = "    🚨🔍📱🔑secret_code✌️"
# Clue: find

# Output
# SECRET_CODE✌️

person1 = input("Please tell me person1 name: ")
person2 = input("Please tell me person2 name: ")
height1 = float(input(f"Please tell me the height of {person1}: "))
height2 = float(input(f"Please tell me the height of {person2}: "))
height_difference = abs(height1 - height2)

if height1 > height2:
    print(f"{person1} is taller than {person2} by {height_difference}cm")
elif height2 > height1:
    print(f"{person2} is taller than {person1} by {height_difference}cm")
else:
    print(f"{person1} and {person2} are of the same height")
