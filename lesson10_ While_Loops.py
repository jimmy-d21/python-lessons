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
