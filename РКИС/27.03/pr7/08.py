
class ShoppingList:
    def __init__(self):
        self.__items = []
    
    def add_item(self, item):
        self.__items.append(item)
    
    def get_items(self):
        return self.__items
    
    def clear(self):
        self.__items = []
