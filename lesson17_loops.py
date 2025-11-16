# For loop
for i in range(3):
    print(i)  # Output: 0 1 2

# While loop
count = 0
while count < 3:
    print(count)  # Output: 0 1 2
    count += 1

# Break statement
for i in range(5):
    if i == 3:
        break
    print(i)  # Output: 0 1 2

# Continue statement
for i in range(5):
    if i == 2:
        continue
    print(i)  # Output: 0 1 3 4

# Nested loop
for i in range(2):
    for j in range(2):
        print(i, j)  # Output: 0 0, 0 1, 1 0, 1 1
