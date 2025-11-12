# Creating a tuple
colors = ("red", "green", "blue")
print(colors)  # Output: ('red', 'green', 'blue')

# Accessing elements
print(colors[1])  # Output: green

# Tuple length
print(len(colors))  # Output: 3

# Nested tuple
nested = (1, (2, 3), 4)
print(nested[1][1])  # Output: 3

# Loop through tuple
for c in colors:
    print(c)  # Output: red \n green \n blue

# Tuple concatenation
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)  # Output: (1, 2, 3, 4)

# Tuple repetition
print(t1 * 3)  # Output: (1, 2, 1, 2, 1, 2)

# Membership test
print("red" in colors)  # Output: True
