class StringOnlyDescriptor:
    def __init__(self):
        self._value = None

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("Value must be string")
        self._value = value


class MyClass:
    attr = StringOnlyDescriptor()


obj = MyClass()
obj.attr = "hello"
# obj.attr = 123  # TypeError
