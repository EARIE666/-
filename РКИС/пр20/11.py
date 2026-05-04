class EmailDescriptor:
    def __init__(self):
        self._value = None

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if '@' not in value:
            raise ValueError("Email must contain '@'")
        self._value = value


class MyClass:
    email = EmailDescriptor()


obj = MyClass()
obj.email = "test@example.com"
# obj.email = "invalid"  # ValueError
