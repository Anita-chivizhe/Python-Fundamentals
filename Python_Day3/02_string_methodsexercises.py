# Task 1
# Expected Output
# "PYTHON-POWERFUL
secret_message = "   Programming in Python is not only powerful but also fun!   "
clean_secret_message = secret_message.strip()
print(clean_secret_message[15:21].upper() + "-" + clean_secret_message[34:42].upper())


# 1. Solve
# 2. Make it better

# Task 1.2

flipped_message = "!nuf sseldnE dna seitinutroppo lufrewop htiw nohtyP"

# Expected Output
# "python 🗡️ powerful 🌸"

msg = flipped_message[-1:-7:-1] + " 🗡️  " + flipped_message[-13:-21:-1] + " 🌸"
print(msg.lower())

# Task 1.3

# After the 🔑
message_one = "    🚨🔍📱🔑secret_code✌️"
key_message = message_one.find("🔑")
print(message_one[key_message + 1 :].upper())

# Output
# SECRET_CODE✌️
