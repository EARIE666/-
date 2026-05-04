class SimpleDescriptor:
    def __init__(self):
        self._value = None

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        self._value = value


class MyClass:
    attr = SimpleDescriptor()


obj = MyClass()
obj.attr = 42
print(obj.attr)
