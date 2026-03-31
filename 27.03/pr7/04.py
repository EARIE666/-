
class StepCounter:
    def __init__(self):
        self.__steps = 0
    
    def walk(self, steps):
        self.__steps += steps			
    
    def reset(self):
        self.__steps = 0
    
    def get_steps(self):
        return self.__steps
