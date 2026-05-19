
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print_message(self, msg):
        pass

class UpperPrinter(Printer):
    def print_message(self, msg):
        print(msg.upper())
