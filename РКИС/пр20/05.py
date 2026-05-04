class IntOnlyDescriptor:
    def __init__(self):
        self._value = None

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Value must be int")
        self._value = value


class MyClass:
    attr = IntOnlyDescriptor()


obj = MyClass()
obj.attr = 10
# obj.attr = "hello"  # TypeError
