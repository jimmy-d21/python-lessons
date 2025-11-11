# Creating a list
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']


# Accessing elements
print(fruits[0])  # Output: apple


# Modifying a list
fruits[1] = "orange"
print(fruits)  # Output: ['apple', 'orange', 'cherry']


# Adding elements
fruits.append("grape")
print(fruits)  # Output: ['apple', 'orange', 'cherry', 'grape']


# Inserting at specific position
fruits.insert(1, "mango")
print(fruits)  # Output: ['apple', 'mango', 'orange', 'cherry', 'grape']


# Removing elements
fruits.remove("cherry")
print(fruits)  # Output: ['apple', 'mango', 'orange', 'grape']


# Pop item
fruits.pop(2)
print(fruits)  # Output: ['apple', 'mango', 'grape']
