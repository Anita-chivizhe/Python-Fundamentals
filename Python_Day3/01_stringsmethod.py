fav_movie = " John Wick"

# only 'J'

# Index
print(fav_movie[0])  # J
print(fav_movie[5])  # W

# Negative Index
print(fav_movie[-1])  # k
print(fav_movie[-2])  # c

# Only Wick
print(fav_movie[-4] + fav_movie[-3] + fav_movie[-2] + fav_movie[-1])  # k
print(fav_movie[-2])  # c

# Slice Operators
# fav_movie [start:end] - end index not included
print(fav_movie[2:6])  # hn W
print(fav_movie[2:8])  # hn Wic
print(fav_movie[2:9])  # hn Wick

# Copy String
print(fav_movie[0:])  # John Wick
print(fav_movie[:])  # John Wick

# Only Wick
print(fav_movie[5:9])  #
print(fav_movie[5:])  #
print(fav_movie[-4:9])  #

fav_hero = "The Hulk"
print(fav_hero[0:4] + "h" + fav_hero[-3:])

# repeat operator
print("💕" * 20)

# Case modifying methods

catchphrase = "I am Groot"
print(catchphrase.upper())
print(catchphrase.lower())
print(catchphrase.capitalize())
print(catchphrase.title())
print(catchphrase.swapcase())

print(catchphrase)  # String methods does not modify original value (Immutable)

message = "   With great power comes great responsibility   "
clean_message = message.strip()
print(message)
print(clean_message)

coded_message = "********SO*S******"
decoded = coded_message.strip("*")
print(decoded)

quote = "Dream is not something that you see in sleep, Dream is something that does not let you sleep"
print(quote.replace("Dream", "🛏️ ☁️"))

# find
print(quote.find("something"))
print(quote.find("**"))
