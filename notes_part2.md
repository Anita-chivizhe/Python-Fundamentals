# 1. Python Built-in Functions

<font color="pink">Python has several built-in functions that simplify many tasks. Here are a few:</font>

```py

len(): Returns the length of an object (list, string, etc.).
len([1, 2, 3]) # Output: 3

sum(): Returns the sum of an iterable.
sum([1, 2, 3]) # Output: 6

max() and min(): Return the maximum or minimum of an iterable.
max([1, 2, 3]) # Output: 3
min([1, 2, 3]) # Output: 1

round(): Rounds a number to a specified decimal place.
round(3.14159, 2) # Output: 3.14

sorted(): Returns a sorted list from the specified iterable.
sorted([3, 1, 2]) # Output: [1, 2, 3]

abs(): Returns the absolute value of a number.
```

# 2. Truthiness and Falsiness

In Python, some values are considered **falsy**, meaning they evaluate to False in a boolean context, and all other values are **truthy**.

**Falsy values:**

> None,
>
> False,
>
> 0,
>
> ""(empty string),
>
> [](empty list),
>
> {}(empty dictionary),
>
> ()(empty tuple)

Example:

```py
if []:  # Empty list is falsy
    print("True")
else:
    print("False")  # Output: False
```
