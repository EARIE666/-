class CounterDescriptor:
    def __init__(self):
        self._value = None
        self._count = 0

    def __get__(self, instance, owner):
        self._count += 1
        return self._value

    def __set__(self, instance, value):
        self._value = value

    def get_count(self):
        return self._count


class MyClass:
    attr = CounterDescriptor()


obj = MyClass()
obj.attr = 99
print(obj.attr)
print(obj.attr)
print(obj.attr)
print(MyClass.attr.get_count())  # 3
