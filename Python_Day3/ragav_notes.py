fav_movie = "John Wick"

# Only 'J'

# Index
print(fav_movie[0])  # J
print(fav_movie[5])  # W


# Negative Index
print(fav_movie[-1])  # k
print(fav_movie[-2])  # c


# Only 'Wick'
print(fav_movie[-4] + fav_movie[-3] + fav_movie[-2] + fav_movie[-1])
print(fav_movie[5] + fav_movie[6] + fav_movie[7] + fav_movie[8])


# Slice operator (:)
# fav_movie[start:end:step] - end index not included, step +1
print(fav_movie[2:6])  # hn W
print(fav_movie[2:8])  # hn Wic
print(fav_movie[2:9])  # hn Wick

print(fav_movie[2:])  # hn Wick

# Copy String
print(fav_movie[0:])  # John Wick
print(fav_movie[:])  # John Wick


# Only 'Wick'
print(fav_movie[5:9])  # Wick
print(fav_movie[5:])  # Wick
print(fav_movie[-4:])  # Wick

print(fav_movie[2:9])  # hn Wick
print(fav_movie[2:9:1])  # hn Wick
print(fav_movie[2:9:2])  # h ik


# Reverse string, step < 0
print(fav_movie[::-1])  # kciW nhoJ
print(fav_movie[-4::-1])  # W nhoJ


print(fav_movie[-4:-2:-1])  #
print(fav_movie[-4:-9:-1])  # W nho
