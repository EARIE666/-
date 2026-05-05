class Rectangle:
    __slots__ = ('width', 'height')

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(5, 8)
print(f"Площадь = {rect.area()}")