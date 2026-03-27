
class EvenOddSumTracker:
    def __init__(self):
        self.even_sum_val = 0
        self.odd_sum_val = 0
    
    def add_number(self, n):
        if n % 2 == 0:
            self.even_sum_val += n
        else:
            self.odd_sum_val += n
    
    def even_sum(self):
        return self.even_sum_val
    
    def odd_sum(self):
        return self.odd_sum_val
