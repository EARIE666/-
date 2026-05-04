class SetLoggingDescriptor:
    def __init__(self):
        self._value = None

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        print('Setting value')
        self._value = value


class MyClass:
    attr = SetLoggingDescriptor()


obj = MyClass()
obj.attr = 5
