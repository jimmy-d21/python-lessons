# Lesson 8 — Comprehensions & Generators
# File: lesson08_comprehensions_generators.py

# 1) List comprehension
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

# 2) Dict comprehension
d = {x: x*x for x in range(5)}
print(d)
