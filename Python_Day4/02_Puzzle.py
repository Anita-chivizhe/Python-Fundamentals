i = 1
while i <= 5:
    print("🔥" * i)
    i = i + 1

for i in range(6):
    print("🔥" * i)

rows = int(input("Please enter the no. rows: "))
pattern = input("Please enter the pattern: ")

x = 1
while x <= rows + 1:
    print(pattern * i)
    x += 1

rows = int(input("Please enter the no. rows: "))
pattern = input("Please enter the pattern: ")

for x in range(1, rows, 1):
    print(pattern * x)
