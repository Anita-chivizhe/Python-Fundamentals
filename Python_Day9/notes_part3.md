# 5.3 Tuples

Tuples are immutable, ordered collections.

- Tuples CRUD

  - Create: ()

  - Read: By index : tuple [index]

  - Update/Delete : Tuples cannot be updated or deleted after creation.

Example:

```py
coordinates = (10, 20, 30)
print(coordinates[0])  # Output: 10
```

# 5.4 Sets

Sets are unordered collections of unique items.

- CRUD Operations:
  - Create: {} or set()
  - Read:
  - Update: add() or update()
  - Delete: remove() or discard()
    Example:

unique_numbers = {1, 2, 3}
unique_numbers.add(4)
unique_numbers.remove(2)

1.  Unpacking and Unpacking Operator
    10.1 Unpacking
    Unpacking allows you to assign values from a sequence (like a list or tuple) to multiple variables.

Example:

x, y, z = (1, 2, 3)
print(x, y, z) # Output: 1 2 3
10.2 Unpacking Operator _
The _ operator can be used to collect multiple values from an iterable.

Example:

a, \*b = [1, 2, 3, 4]
print(a) # Output: 1
print(b) # Output: [2, 3, 4]

11.4 Sets
Create: unique_numbers = {1, 2, 3}
Add: unique_numbers.add(4)
Remove: unique_numbers.remove(2)
