#1. Инкапсуляция
class Person:
    def _init_(self, age=0):
        self.__age = 0
        self.set_age(age)

    def set_age(self, age):
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным!")
        self.__age = age

    def get_age(self):
        return self.__age
p = Person()
p.set_age(25)
print(p.get_age())   # 25
#p.set_age(-5) # Должна быть ошибка или предупреждение

# 2. Наследование
class Animal:
    class Animal:
        def __init__(self, name):
            self.name = name

        def speak(self):
            return "животное"

    class Dog(Animal):
        def speak(self):
            return "гав"

    class Cat(Animal):
        def speak(self):
            return "мяу"
    a = Animal("животное")
    d = Dog("гав")
    c = Cat("мяу")

    print(a.name, a.speak())
    print(d.name, d.speak())
    print(c.name, c.speak())

# 3. Полиморфизм
class Vehicle:
    def move(self):
        return "CAR движется"


class Car(Vehicle):
    def move(self):
        return "Car едит"


class Bicycle(Vehicle):
    def move(self):
        return "велосиредис крутет педали"


v = Vehicle()
c = Car()
b = Bicycle()

print(v.move())
print(c.move())
print(b.move())

# 4. Абстракция
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


r = Rectangle(10, 5)
c = Circle(7)

print(r.area())   #50
print(c.area())  #150
