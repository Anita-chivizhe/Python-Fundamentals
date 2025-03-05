# 4. Control Flow

## 4.1 if, elif, else Statements

- Conditional statements allow you to execute code based on certain conditions.

  Example:

```py
   x = 10
   if x > 5:
    print("x is greater than 5")
   elif x == 5:
    print("x is equal to 5")
   else:
    print("x is less than 5")
```

## 4.2 Loops

### For loop: Iterates over a sequence (list, string, range, etc.).

Example:

```py
for i in range(3):
    print(i)  # Output: 0, 1, 2
```

### While loop: Repeats a block of code as long as a condition is true.

Example:

```py
count = 0
while count < 3:
    print(count)
    count += 1  # Output: 0, 1, 2
```

# 5. Data Structures

## 5.1 Lists

- Lists are ordered, mutable collections of items.

- List CRUD
  - Create: []
  - Access: By index: list[index]
  - Update: Modify elements by assignment.
  - Delete: del, remove(), pop()

Example:

```py
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Add "orange"
fruits.remove("banana")  # Remove "banana"
del fruits[0]  # Remove the first element
print(fruits)  # Output: ['cherry', 'orange']
```

### 5.1.1 List Comprehension

A concise way to create lists in Python, allowing for optional filtering and transformation.

> [expression for item in iterable if condition]

Example:
squares = [x**2 for x in range(5)] # Output: [0, 1, 4, 9, 16]

## 5.2 Dictionaries

<p style="color:red">Dictionaries are unordered collections of key-value pairs.</p>

- Create: {key: value}
- Read: Access by key: dict[key]
- Update: Modify values with keys.
- Delete: remove or pop()
- Safe Access: Use get() to avoid errors if a key doesn't exist.

```py
student = {"name": "Alice", "age": 25}
print(student.get("name"))  # Output: Alice
print(student.get("grade", "Not Available"))  # Output: Not Available
```

### CRUD Operations:

> - #### Create
>
>   student = {"name": "Alice", "age": 25}
>
> - #### Read
>
>   print(student["name"]) # Output: Alice
>
> - #### Update
>
>   student["age"] = 26
>
> - #### Delete
>   remove.student["age"]
>   Make this text blue.
