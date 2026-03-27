#Задача 1: SecretNumber
class SecretNumber:
    def __init__(self):
        self.__number = None
    
    def set_number(self, n):
        self.__number = n
    
    def get_number(self):
        return self.__number
#Задача 2: PositiveNumber
class PositiveNumber:
    def __init__(self):
        self.__number = 0
    
    def set_number(self, n):
        if n > 0:
            self.__number = n
    
    def get_number(self):
        return self.__number
#Задача 3: UserName
class UserName:
    def __init__(self):
        self.__name = ""
    
    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name.upper()
#Задача 4: StepCounter
class StepCounter:
    def __init__(self):
        self.__steps = 0
    
    def walk(self, steps):
        self.__steps += steps
    
    def reset(self):
        self.__steps = 0
    
    def get_steps(self):
        return self.__steps
#Задача 5: BankAccount
class BankAccount:
    def __init__(self):
        self.__balance = 0
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
    
    def get_balance(self):
        return self.__balance
#Задача 6: Temperature
class Temperature:
    def __init__(self):
        self.__celsius = 0
    
    def set_celsius(self, c):
        self.__celsius = c
    
    def get_celsius(self):
        return self.__celsius
    
    def get_fahrenheit(self):
        return self.__celsius * 9/5 + 32
#Задача 7: EmailAccount
class EmailAccount:
    def __init__(self):
        self.__email = ""
    
    def set_email(self, email):
        if '@' in email:
            self.__email = email
    
    def get_email(self):
        return self.__email
#Задача 8: ShoppingList
class ShoppingList:
    def __init__(self):
        self.__items = []
    
    def add_item(self, item):
        self.__items.append(item)
    
    def get_items(self):
        return self.__items
    
    def clear(self):
        self.__items = []
#Задача 9: LimitedCounter
class LimitedCounter:
    def __init__(self, max_value):
        self.__value = 0
        self.__max = max_value
    
    def increment(self):
        if self.__value < self.__max:
            self.__value += 1
    
    def decrement(self):
        if self.__value > 0:
            self.__value -= 1
    
    def get_value(self):
        return self.__value
#Задача 10: Point2D
import math

class Point2D:
    def __init__(self):
        self.__x = 0
        self.__y = 0
    
    def set_coordinates(self, x, y):
        self.__x = x
        self.__y = y
    
    def get_coordinates(self):
        return (self.__x, self.__y)
    
    def distance_from_origin(self):
        return math.sqrt(self.__x**2 + self.__y**2)
