# 1. Introduction to Python

Python is a high-level, interpreted language, designed for readability and ease of use. It’s versatile, widely used for web development, data analysis, automation, artificial intelligence, and more.

# 2. Variables and Data Types

In Python, you don’t need to explicitly declare the type of a variable; it’s inferred from the value assigned `(dynamically smart)`. Python supports several basic data types:

str: Text like "Hello, World!"
int: Integer numbers like 5, 100
float: Floating point numbers like 3.14, 10.5
bool: Boolean values like True or False

Example:

```py
name = "Alice"   # str
age = 25         # int
height = 5.6     # float
is_student = True # bool
```

# 3. Operators

Python supports a variety of operators, including arithmetic, comparison, logical, and membership operators.

## **Arithmetic Operators**

- **Addition (`+`)**: Adds two operands.

  - Example: `3 + 2` gives `5`

- **Subtraction (`-`)**: Subtracts the second operand from the first.

  - Example: `5 - 2` gives `3`

- **Multiplication (`*`)**: Multiplies two operands.

  - Example: `3 * 2` gives `6`

- **Division (`/`)**: Divides the first operand by the second, returns a float.

  - Example: `5 / 2` gives `2.5`

- **Floor Division (`//`)**: Divides the first operand by the second and returns the integer part of the quotient, removing the remainder.

  - Example: `5 // 2` gives `2`

- **Modulus (`%`)**: Returns the remainder of the division.

  - Example: `5 % 2` gives `1`

- **Exponentiation (`**`)\*\*: Raises the first operand to the power of the second.
  - Example: `2 ** 3` gives `8`

## **Comparison Operators**

- **Equal to (`==`)**: Checks if two operands are equal.

  - Example: `3 == 3` gives `True`

- **Not equal to (`!=`)**: Checks if two operands are not equal.

  - Example: `3 != 2` gives `True`

- **Greater than (`>`)**: Checks if the left operand is greater than the right.

  - Example: `5 > 3` gives `True`

- **Less than (`<`)**: Checks if the left operand is less than the right.

  - Example: `3 < 5` gives `True`

- **Greater than or equal to (`>=`)**: Checks if the left operand is greater than or equal to the right.

  - Example: `5 >= 5` gives `True`

- **Less than or equal to (`<=`)**: Checks if the left operand is less than or equal to the right.
  - Example: `3 <= 5` gives `True`

---

## **Logical Operators**

- **And (`and`)**: Returns `True` if both operands are true.

  - Example: `True and False` gives `False`

- **Or (`or`)**: Returns `True` if at least one operand is true.

  - Example: `True or False` gives `True`

- **Not (`not`)**: Reverses the boolean value of the operand.
  - Example: `not True` gives `False`

---

## **Membership Operators**

- **In (`in`)**: Checks if a value exists in a sequence (like a list, tuple, or string).

  - Example: `"a" in "apple"` gives `True`

- **Not in (`not in`)**: Checks if a value does not exist in a sequence.
  - Example: `"z" not in "apple"` gives `True`

---

## **Ternary (Conditional) Operator**

- **Ternary operator**: A shorthand for `if-else` to assign a value based on a condition.

  - Syntax: `value_if_true if condition else value_if_false`
  - Example: `"Even" if x % 2 == 0 else "Odd"`

---

## 4. Chaining and Lexical Order

### 4.1. Chaining Comparison Operators

Python allows chaining of comparison operators, making code more concise.

Example:

```py
x = 5
if 1 < x < 10:
    print("x is between 1 and 10")
```

## 4.2 Lexical Order

Strings are compared lexicographically (like in a dictionary).

Example:

```py
print("apple" < "banana")  # Output: True
```
