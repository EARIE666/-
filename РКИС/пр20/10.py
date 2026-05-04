class MaxLengthDescriptor:
    def __init__(self, max_length=10):
        self.max_length = max_length
        self._value = None

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("Value must be string")
        if len(value) > self.max_length:
            raise ValueError(f"String length must not exceed {self.max_length}")
        self._value = value


class MyClass:
    attr = MaxLengthDescriptor(10)


obj = MyClass()
obj.attr = "short"
# obj.attr = "very long string"  # ValueError
