# Lesson 4 — Control Flow
# File: lesson04_control_flow.py


# 1) if/elif/else
x = 10
if x < 5:
    print("small")
elif x < 20:
    print("medium")
else:
    print("large")

# 2) for over list
for i in [1, 2, 3]:
    print(i)

# 3) for with range
for i in range(5):
    print(i)

# 4) while loop
n = 0
while n < 3:
    print(n)
n += 1

# 5) break
for i in range(10):
    if i == 3:
        break
    print(i)

# 6) continue
for i in range(5):
    if i % 2 == 0:
        continue
print("odd", i)
