class DefaultValueDescriptor:
    def __init__(self, default='default'):
        self.default = default
        self._value = None

    def __get__(self, instance, owner):
        if self._value is None:
            return self.default
        return self._value

    def __set__(self, instance, value):
        self._value = value


class MyClass:
    attr = DefaultValueDescriptor()


obj = MyClass()
print(obj.attr)  # default
obj.attr = "test"
print(obj.attr)  # test
