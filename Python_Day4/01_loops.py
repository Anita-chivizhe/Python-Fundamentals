# Refactor in for loop
# for and range (pair)

# range always starts with 0
# range excludes the end

# range(start, end, step)
# range(3) -> range(end)
# for i in range(3):
#     print(i)


# range(start, end) -> range(start, end)
# for and range takes care of incrementing `i`
for i in range(1, 51, 2):
    print(i)

i = 1
while i <= 50:
    print(i)
    i += 2
