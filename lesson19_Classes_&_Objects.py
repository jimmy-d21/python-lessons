# Classes
class Person:
    def __init__(self, name):
        self.name = name


p = Person("Marjani")
print(p.name)  # Output: Marjani


# Classes
class Greeter:
    def greet(self):
        print("Hello!")  # Output: Hello!


g = Greeter()
g.greet()


# Classes
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year


mycar = Car("Toyota", 2023)
print(mycar.brand, mycar.year)  # Output: Toyota 2023


# Classes
class Math:
    def add(self, a, b):
        return a + b


m = Math()
print(m.add(5, 3))  # Output: 8
