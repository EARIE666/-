
class CounterButton:
    def __init__(self):
        self._count = 0
    
    def press(self):
        self._count += 1
    
    def count(self):
        return self._count
    
    def reset(self):
        self._count = 0
