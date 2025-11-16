# File Handling
with open("demo.txt", "w") as f:
    f.write("Hello, File Handling!")  # Output: File created with text

# File Handling
with open("demo.txt", "r") as f:
    print(f.read())  # Output: Hello, File Handling!
