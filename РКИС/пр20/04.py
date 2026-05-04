class PrivateStorageDescriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class MyClass:
    attr = PrivateStorageDescriptor('_hidden_attr')


obj = MyClass()
obj.attr = 100
print(obj.attr)
print(obj.__dict__)
