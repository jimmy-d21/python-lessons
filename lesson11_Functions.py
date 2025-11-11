# LESSON 11: FUNCTIONS
# Functions help organize and reuse code.

# Example 1
def greet():
    print("Hello, world!")


greet()


# Example 2
def greet_user(name):
    print("Hello,", name)


greet_user("Marjani")


# Example 3
def add(a, b):
    print("Sum:", a + b)


add(5, 3)


# function that returns a value
def multiply(a, b):
    return a * b


print(multiply(3, 4))


# function to check if number is even
def is_even(num):
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")


is_even(7)


# function with default argument
def greet_country(country="Tanzania"):
    print("Hello from", country)


greet_country()
greet_country("Kenya")


# function with multiple parameters
def display_info(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")


display_info("Marjani", 21, "Msolwa")
