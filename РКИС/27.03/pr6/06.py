class MinMaxNumberFinder:
    def __init__(self):
        self.numbers = []
    
    def add_number(self, n):
        self.numbers.append(n)
    
    def min_numbers(self):
        if not self.numbers:
            return []
        min_val = min(self.numbers)
        return [x for x in self.numbers if x == min_val]
    
    def max_numbers(self):
        if not self.numbers:
            return []
        max_val = max(self.numbers)
        return sorted(set([x for x in self.numbers if x != max_val]))
