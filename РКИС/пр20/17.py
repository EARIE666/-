class CachedProperty:
    def __init__(self, func):
        self.func = func
        self.name = func.__name__

    def __get__(self, instance, owner):
        if instance is None:
            return self
        value = self.func(instance)
        instance.__dict__[self.name] = value
        return value


class Example:
    @CachedProperty
    def expensive_calculation(self):
        print("Calculating...")
        return 42


obj = Example()
print(obj.expensive_calculation)
print(obj.expensive_calculation)
