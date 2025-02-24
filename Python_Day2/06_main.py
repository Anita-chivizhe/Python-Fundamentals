# Task 4
# Task: Build a loader
# Input: 70
# Output: [======= ] 70%

# Input: 23
# Output: [==      ] 23%

percentage = int(input("Enter your progress level: "))
loader = percentage // 10
loader_symbols = loader * "="
space_symbols = (10 - loader) * " "
print(f"Output: [{loader_symbols}{space_symbols}] {percentage}%")
