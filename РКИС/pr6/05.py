
class FlipFlopBell:
    def __init__(self):
        self.flip = True
    
    def ring(self):
        if self.flip:
            print("flip")
        else:
            print("flop")
        self.flip = not self.flip
