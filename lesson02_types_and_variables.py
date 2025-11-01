# Lesson 2 — Types & Variables
# File: lesson02_types_and_variables.py


# 1) Integers and floats
i = 42
f = 3.14
print(type(i), type(f))

# 2) Strings
s = "Python"
print(s, len(s))

# 3) Booleans
b = True
print(b, type(b))

# 4) None
n = None
print(n is None)

# 5) Type casting
num = "123"
num_int = int(num)
print(num_int + 1)

# 6) Converting floats to int
print(int(3.99))  # truncates


# 7) Combining strings
greet = "Hi" + " " + "there"
print(greet)

# 8) f-strings and repr
value = 7
print(f"value={value!r}")

# 9) Multiple assignment
a, b, c = 1, 2.0, "three"
print(a, b, c)
