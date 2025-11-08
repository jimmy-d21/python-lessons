# Lesson 6 — Lists
# File: lesson06_lists.py

# 1) Create list
fruits = ["apple", "banana", "cherry"]

# 2) Indexing
print(fruits[0], fruits[-1])

# 3) Slicing
print(fruits[0:2])

# 4) Append and extend
fruits.append("date")
fruits.extend(["elderberry", "fig"])
print(fruits)

# 5) Insert and remove
fruits.insert(1, "blueberry")
fruits.remove("banana")
print(fruits)
