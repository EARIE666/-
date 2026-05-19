
class AlternatingCounter:
    def __init__(self):
        self.a_count = 0
        self.b_count = 0
        self.next_is_a = True
    
    def count(self):
        if self.next_is_a:
            self.a_count += 1
        else:
            self.b_count += 1
        self.next_is_a = not self.next_is_a
        return (self.a_count, self.b_count)
    
    def reset(self):
        self.a_count = 0
        self.b_count = 0
        self.next_is_a = True
