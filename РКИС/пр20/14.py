class OneTimeAssignmentDescriptor:
    def __init__(self):
        self._value = None
        self._assigned = False

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if self._assigned:
            raise AttributeError("Value already assigned and cannot be changed")
        self._value = value
        self._assigned = True


class MyClass:
    attr = OneTimeAssignmentDescriptor()


obj = MyClass()
obj.attr = 100
# obj.attr = 200  # AttributeError
