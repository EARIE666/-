class NumberListDescriptor:
    def __init__(self):
        self._value = []

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, list):
            raise TypeError("Value must be a list")
        if not all(isinstance(item, (int, float)) for item in value):
            raise TypeError("All elements must be numbers")
        self._value = value


class MyClass:
    numbers = NumberListDescriptor()


obj = MyClass()
obj.numbers = [1, 2.5, 3]
# obj.numbers = [1, "hello"]  # TypeError
