
import math

class Point2D:
    def __init__(self):
        self.__x = 0
        self.__y = 0
    
    def set_coordinates(self, x, y):
        self.__x = x
        self.__y = y
    
    def get_coordinates(self):
        return (self.__x, self.__y)
    
    def distance_from_origin(self):
        return math.sqrt(self.__x**2 + self.__y**2)
