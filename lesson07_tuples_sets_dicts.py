# Lesson 7 — Tuples, Sets, Dicts
# File: lesson07_tuples_sets_dicts.py

# 1) Tuple (immutable)
t = (1, 2, 3)
print(t[0])

# 2) Single-element tuple
single = (5,)
print(type(single))

# 3) Set (unique items)
s = {1, 2, 2, 3}
print(s)

# 4) Set operations
print({1, 2} & {2, 3}, {1, 2} | {2, 3})

# 5) Dict creation
d = {"name": "Alice", "age": 25}
print(d["name"])

# 6) Dict get with default
print(d.get("city", "Unknown"))

# 7) Iterating dict
for k, v in d.items():
    print(k, v)

# 8) Dict comprehension
squares = {x: x*x for x in range(5)}
print(squares)

# 9) Packing/unpacking with * and **
vals = [1, 2, 3]
a, *rest = vals
print(a, rest)
