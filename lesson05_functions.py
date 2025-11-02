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


# 3) Keyword arguments
def info(name, age):
    print(name, age)


info(age=30, name="Sam")


# 4) Variable args (*args)
def sum_all(*args):
    return sum(args)


print(sum_all(1, 2, 3))


# 5) Keyword args (**kwargs)
def show(**kwargs):
    print(kwargs)


show(a=1, b=2)


# 6) Returning multiple values
def coords():
    return 10, 20


x, y = coords()
print(x, y)
