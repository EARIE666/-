class AgeDescriptor:
    def __init__(self):
        self._value = None

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Age must be int")
        if value < 0 or value > 120:
            raise ValueError("Age must be between 0 and 120")
        self._value = value


class MyClass:
    age = AgeDescriptor()


obj = MyClass()
obj.age = 25
# obj.age = 150  # ValueError
