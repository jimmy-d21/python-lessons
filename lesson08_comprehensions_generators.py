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

# 5) Using generator in for loop
for val in (x+1 for x in range(3)):
    print(val)

# 6) Memory note: generators use less memory
# 7) Convert generator to list
print(list(x for x in range(3)))

# 8) Nested comprehension
pairs = [(i, j) for i in range(3) for j in range(2)]
print(pairs)

# 9) Conditional expression in comprehension
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(labels)
