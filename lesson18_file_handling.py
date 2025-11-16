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
