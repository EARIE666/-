class LoggingDescriptor:
    def __init__(self):
        self._value = None

    def __get__(self, instance, owner):
        print('Getting value')
        return self._value

    def __set__(self, instance, value):
        self._value = value


class MyClass:
    attr = LoggingDescriptor()


obj = MyClass()
obj.attr = 10
print(obj.attr)
