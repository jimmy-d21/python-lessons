# File Handling
with open("demo.txt", "w") as f:
    f.write("Hello, File Handling!")  # Output: File created with text

# File Handling
with open("demo.txt", "r") as f:
    print(f.read())  # Output: Hello, File Handling!

# File Handling
with open("demo.txt", "a") as f:
    f.write("\nSecond line added!")  # Output: Text appended

# File Handling
with open("demo.txt", "r") as f:
    for line in f:
        print(line.strip())  # Output: Each line printed

# File Handling
with open("demo.txt", "r") as f:
    print(f.readlines())  # Output: ['Hello...\n', 'Second line...\n']

# File Handling
import os
print(os.path.exists("demo.txt"))  # Output: True

# File Handling
print(os.path.getsize("demo.txt"))  # Output: (size in bytes)

# File Handling
try:
    open("missing.txt")
except FileNotFoundError:
    print("File not found!")  # Output: File not found!

# File Handling
os.remove("demo.txt")  # Output: File deleted


# File Handling
with open("multi.txt", "w") as f:
    f.writelines(["Line 1\n", "Line 2\n"])  # Output: 2 lines written
