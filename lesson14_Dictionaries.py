# Creating a dictionary
person = {"name": "Marjani", "age": 22, "country": "Tanzania"}
print(person)  # Output: {'name': 'Marjani', 'age': 22, 'country': 'Tanzania'}

# Accessing values
print(person["name"])  # Output: Marjani

# Adding key-value pair
person["job"] = "Engineer"
print(person)  # Output includes 'job': 'Engineer'

# Updating value
person["age"] = 23
print(person["age"])  # Output: 23

# Removing key
del person["country"]
print(person)  # Output: {'name': 'Marjani', 'age': 23, 'job': 'Engineer'}

# Looping keys
for key in person:
    print(key)  # Output: name \n age \n job

# Looping values
for value in person.values():
    print(value)  # Output: Marjani \n 23 \n Engineer

# Looping items
for key, value in person.items():
    print(key, value)  # Output: name Marjani etc.

# Using get() method
print(person.get("name"))  # Output: Marjani
