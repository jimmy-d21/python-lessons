# LESSON 9: FOR LOOPS
# For loops are used to repeat code for a specific number of times or over a sequence.

# Example 1: Basic range loop
for i in range(5):
    print("Count:", i)

# Example 2: Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

# Example 3: Loop with custom start and stop
for num in range(2, 7):
    print(num)

# Example 4: Loop with step value
for num in range(0, 10, 2):
    print("Even number:", num)

# Example 5: Loop through string
for letter in "Python":
    print(letter)

# Example 6: Nested loop
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# Example 7: Using break
for i in range(10):
    if i == 5:
        break
    print(i)

# Example 8: Using continue
for i in range(10):
    if i % 2 == 0:
        continue
    print("Odd:", i)

# Example 9: Loop with else
for i in range(3):
    print(i)
else:
    print("Loop finished")

# Example 10: Loop through list with index
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"Index {index}: {color}")
