class RoundDescriptor:
    def __init__(self, precision=2):
        self.precision = precision
        self._value = None

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        self._value = round(value, self.precision)


class MyClass:
    price = RoundDescriptor(2)


obj = MyClass()
obj.price = 3.14159
print(obj.price)  # 3.14
