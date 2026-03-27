class BoundingBox2D:
    def __init__(self):
        self.points = []
    
    def add_point(self, x, y):
        self.points.append((x, y))
    
    def left_x(self):
        return min(x for x, y in self.points)
    
    def right_x(self):
        return max(x for x, y in self.points)
    
    def bottom_y(self):
        return min(y for x, y in self.points)
    
    def top_y(self):
        return max(y for x, y in self.points)
    
    def width(self):
        return self.right_x() - self.left_x()
    
    def height(self):
        return self.top_y() - self.bottom_y()
