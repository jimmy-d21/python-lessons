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

# 6) Pop
last = fruits.pop()
print("popped", last)

# 7) List comprehension
nums = [x*x for x in range(5)]
print(nums)

# 8) Sorting
nums2 = [3, 1, 2]
nums2.sort()
print(nums2)

# 9) Copy vs reference
a = [1, 2]
b = a
c = a.copy()
b.append(3)
print(a, c)
