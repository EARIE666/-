class ChangeLogDescriptor:
    def __init__(self):
        self._value = None

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        old = self._value
        print(f"Old value: {old}, New value: {value}")
        self._value = value


class MyClass:
    attr = ChangeLogDescriptor()


obj = MyClass()
obj.attr = 10
obj.attr = 20
