# LESSON 10: WHILE LOOPS
# While loops run as long as a condition is true.

# Example 1
count = 0
while count < 5:
    print("Count:", count)
    count += 1

# Example 2
x = 10
while x > 0:
    print(x)
    x -= 2

# Example 3: Using break
num = 1
while True:
    if num > 5:
        break
    print(num)
    num += 1

# Example 4: Using continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# Example 5: User input
# Uncomment to use:
# while True:
#     name = input("Enter name (or 'exit'): ")
#     if name == "exit":
#         break
#     print("Hello,", name)
