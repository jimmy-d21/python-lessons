# Lesson 8 — Comprehensions & Generators
# File: lesson08_comprehensions_generators.py

# 1) List comprehension
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

# 2) Dict comprehension
d = {x: x*x for x in range(5)}
print(d)

# 3) Set comprehension
s = {x % 3 for x in range(10)}
print(s)

# 4) Generator expression (lazy)
g = (x*x for x in range(5))
print(next(g))
