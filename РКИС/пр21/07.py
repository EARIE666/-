class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return f"({self.x}, {self.y})"

pt = Point(3, 7)
print(pt.get_coords())