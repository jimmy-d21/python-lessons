# Lesson 3 — Operators
# File: lesson03_operators.py


# 1) Arithmetic
print(5 + 2, 5 - 2, 5 * 2, 5 / 2, 5 // 2, 5 % 2, 5 ** 2)

# 2) Comparison
print(5 > 2, 5 == 5, 3 != 4)

# 3) Logical
print(True and False, True or False, not True)

# 4) Chained comparisons
x = 5
print(1 < x < 10)  # true if x between 1 and 10

# 5) Assignment operators
x = 10
x += 5
print(x)

# 6) Identity (is)
a = [1, 2]
b = a
print(a is b)  # True

# 7) Membership (in)
print("p" in "python")

# 8) Bitwise operators (simple)
print(5 & 3, 5 | 3, 5 ^ 3)
