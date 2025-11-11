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

# Example 6: Countdown
n = 5
while n >= 0:
    print(n)
    n -= 1

# Example 7: While with else
a = 3
while a > 0:
    print(a)
    a -= 1
else:
    print("Done!")

# Example 8: Infinite loop example (be careful)
# while True:
#     print("Press Ctrl+C to stop")

# Example 9: Summing numbers
total = 0
num = 1
while num <= 5:
    total += num
    num += 1
print("Total:", total)
