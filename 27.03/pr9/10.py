
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
