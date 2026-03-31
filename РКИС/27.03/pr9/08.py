
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
