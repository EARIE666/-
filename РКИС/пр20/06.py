class PositiveNumberDescriptor:
    def __init__(self):
        self._value = None

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Value must be positive")
        self._value = value


class MyClass:
    attr = PositiveNumberDescriptor()


obj = MyClass()
obj.attr = 42
# obj.attr = -5  # ValueError
