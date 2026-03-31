
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
