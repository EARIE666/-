
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
