
class PositiveNumber:
    def __init__(self):
        self.__number = 0
    
    def set_number(self, n):
        if n > 0:
            self.__number = n
    
    def get_number(self):
        return self.__number
