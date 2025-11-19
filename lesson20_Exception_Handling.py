# Exception
try:
    print(10/0)
except ZeroDivisionError:
    print("Cannot divide by zero!")  # Output: Cannot divide by zero!


# Exception
try:
    int("abc")
except ValueError:
    print("Invalid number!")  # Output: Invalid number!


# Exception
try:
    x = 5 / 1
except:
    print("Error!")
else:
    print("No error!")  # Output: No error!
