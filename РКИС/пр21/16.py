class Temperature:
    __slots__ = ('value',)

    def __init__(self, celsius):
        self.value = celsius

    def to_fahrenheit(self):
        return self.value * 9/5 + 32

temp = Temperature(25)
print(f"{temp.value}°C = {temp.to_fahrenheit()}°F")