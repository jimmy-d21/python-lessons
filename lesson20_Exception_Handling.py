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


# Exception
try:
    print("Inside try")  # Output: Inside try
finally:
    print("Runs always")  # Output: Runs always


# Exception
try:
    raise ValueError("Custom Error")
except ValueError as e:
    print(e)  # Output: Custom Error


# Exception
class MyError(Exception):
    pass


try:
    raise MyError("Something wrong")
except MyError as e:
    print(e)  # Output: Something wrong
