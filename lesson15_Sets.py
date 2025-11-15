# LESSON 15: SETS
# Sets are unordered collections of unique items.

# create set
fruits = {"apple", "banana", "cherry"}
print(fruits)

# add item
fruits.add("orange")
print(fruits)

# remove item
fruits.remove("banana")
print(fruits)

# check membership
print("apple" in fruits)

# union of sets
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))

# intersection of sets
print(a.intersection(b))

# difference of sets
print(a.difference(b))
