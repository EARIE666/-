class ComplexDescriptor:
    def __init__(self, min_val=0, max_val=100):
        self.min_val = min_val
        self.max_val = max_val
        self._value = None

    def __get__(self, instance, owner):
        print(f"Getting value: {self._value}")
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Value must be int")
        if value < self.min_val or value > self.max_val:
            raise ValueError(f"Value must be between {self.min_val} and {self.max_val}")
        print(f"Setting value: {value}")
        self._value = value

    def __delete__(self, instance):
        raise AttributeError("Deletion is not allowed")


class MyClass:
    attr = ComplexDescriptor(10, 50)


obj = MyClass()
obj.attr = 25
print(obj.attr)
# obj.attr = 5     # ValueError
# obj.attr = "str" # TypeError
# del obj.attr     # AttributeError
