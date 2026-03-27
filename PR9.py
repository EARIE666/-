#Задача 1: Shape, Square
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
#Задача 2: Vehicle, Car, Bicycle
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Driving")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling")
#Задача 3: Printer, UpperPrinter
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print_message(self, msg):
        pass

class UpperPrinter(Printer):
    def print_message(self, msg):
        print(msg.upper())
#Задача 4: NumberProcessor, SquareProcessor, DoubleProcessor
from abc import ABC, abstractmethod

class NumberProcessor(ABC):
    @abstractmethod
    def process(self, number):
        pass

class SquareProcessor(NumberProcessor):
    def process(self, number):
        return number ** 2

class DoubleProcessor(NumberProcessor):
    def process(self, number):
        return number * 2
#Задача 5: Animal, Dog, Cat
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")
#Задача 6: Employee, Teacher
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def work(self):
        pass
    
    @abstractmethod
    def salary(self):
        pass

class Teacher(Employee):
    def work(self):
        return "Teaching"
    
    def salary(self):
        return 5000
#Задача 7: Account, BankAccount
from abc import ABC, abstractmethod

class Account(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

class BankAccount(Account):
    def __init__(self):
        self.__balance = 0
    
    def deposit(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance
#Задача 8: Logger, ConsoleLogger, FileLogger
from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, data):
        pass

class ConsoleLogger(Logger):
    def log(self, data):
        print(f"Console: {data}")

class FileLogger(Logger):
    def log(self, data):
        print(f"File: {data}")
#Задача 9: Shape, Rectangle
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
#Задача 10: Processor, SumProcessor, MaxProcessor
from abc import ABC, abstractmethod

class Processor(ABC):
    @abstractmethod
    def process(self, data):
        pass

class SumProcessor(Processor):
    def process(self, data):
        return sum(data)

class MaxProcessor(Processor):
    def process(self, data):
        return max(data)

"""
Ключевые особенности абстрактных классов:
1.	Импорт ABC и abstractmethod: from abc import ABC, abstractmethod
2.	Наследование от ABC: класс должен наследовать от ABC
3.	Декоратор @abstractmethod: помечает метод как абстрактный
4.	Обязательная реализация: все абстрактные методы должны быть реализованы в дочерних классах
5.	Невозможность создания экземпляра: нельзя создать объект абстрактного класса
"""
