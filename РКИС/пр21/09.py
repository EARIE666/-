import math

class Circle:
    __slots__ = ('radius',)

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

circle = Circle(3)
print(f"Площадь круга = {circle.area():.2f}")