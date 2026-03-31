
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
