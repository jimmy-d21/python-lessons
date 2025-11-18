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


# Classes
class Animal:
    def sound(self):
        print("Some sound")


class Dog(Animal):
    def sound(self):
        print("Bark!")  # Output: Bark!


Dog().sound()


# Classes
class A:
    def showA(self): print("A")


class B:
    def showB(self): print("B")


class C(A, B):
    pass


c = C()
c.showA()  # Output: A
c.showB()  # Output: B


# Classes
class Helper:
    @staticmethod
    def hello():
        print("Hi!")  # Output: Hi!


Helper.hello()


# Classes
class Student:
    school = "Msolwa High"


print(Student.school)  # Output: Msolwa High


# Classes
class Num:
    def __init__(self, n): self.n = n
    def __eq__(self, other): return self.n == other.n


print(Num(5) == Num(5))  # Output: True
