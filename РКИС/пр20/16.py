class CelsiusDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__.get('_celsius', 0)

    def __set__(self, instance, value):
        instance.__dict__['_celsius'] = value
        instance.__dict__['_fahrenheit'] = value * 9 / 5 + 32


class FahrenheitDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__.get('_fahrenheit', 32)

    def __set__(self, instance, value):
        instance.__dict__['_fahrenheit'] = value
        instance.__dict__['_celsius'] = (value - 32) * 5 / 9


class Temperature:
    celsius = CelsiusDescriptor()
    fahrenheit = FahrenheitDescriptor()


t = Temperature()
t.celsius = 100
print(t.fahrenheit)

t.fahrenheit = 32
print(t.celsius)
