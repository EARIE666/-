#Задача 1: Animal, Dog, Cat
python
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")
#Задача 2: Shape, Rectangle, Circle
python
import math

class Shape:
    def area(self):
        return 0

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
        return math.pi * self.radius ** 2
#Задача 3: Worker, Teacher, Programmer
python
class Worker:
    def work(self):
        print("Working...")

class Teacher(Worker):
    def work(self):
        print("Teaching...")

class Programmer(Worker):
    def work(self):
        print("Coding...")
#Задача 4: Printer, UpperCasePrinter
python
class Printer:
    def print_message(self, msg):
        print(f"Message: {msg}")

class UpperCasePrinter(Printer):
    def print_message(self, msg):
        print(msg.upper())
#Задача 5: Vehicle, Car, Bicycle
python
class Vehicle:
    def move(self):
        print("Moving...")
    
    def fuel_type(self):
        return "Unknown"

class Car(Vehicle):
    def move(self):
        print("Driving...")
    
    def fuel_type(self):
        return "Petrol"

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling...")
    
    def fuel_type(self):
        return "None"
#Задача 6: Employee, FullTimeEmployee, PartTimeEmployee
python
class Employee:
    def salary(self):
        return 0

class FullTimeEmployee(Employee):
    def salary(self):
        return 5000

class PartTimeEmployee(Employee):
    def salary(self):
        return 2000
#Задача 7: Calculator, SafeCalculator
python
class Calculator:
    def calculate(self, x, y):
        return x + y

class SafeCalculator(Calculator):
    def calculate(self, x, y):
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            return x + y
        return "Error"
#Задача 8: Logger, ListLogger, DictLogger
python
class Logger:
    def log(self, data):
        print(f"Log: {data}")

class ListLogger(Logger):
    def log(self, data):
        print(f"List log: {data}")

class DictLogger(Logger):
    def log(self, data):
        print(f"Dict log: {data}")
#Задача 9: Device, Phone, Laptop
python
class Device:
    def action(self):
        print("Doing generic action")

class Phone(Device):
    def action(self):
        print("Making a call")

class Laptop(Device):
    def action(self):
        print("Running software")
#Задача 10: Exam, MathExam, EnglishExam
python
class Exam:
    def score(self):
        return 0

class MathExam(Exam):
    def score(self):
        return 95

class EnglishExam(Exam):
    def score(self):
        return 88

