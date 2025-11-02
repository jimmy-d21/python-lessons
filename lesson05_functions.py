# Lesson 5 — Functions
# File: lesson05_functions.py


# 1) Basic function
def add(a, b):
    """Return sum of a and b."""
    return a + b


print(add(2, 3))


# 2) Default arguments
def greet(name="friend"):
    print(f"Hello, {name}")


greet()
