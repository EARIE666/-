#Задача 1: TinyHorn
class TinyHorn:
    def play(self):
        print("toot")
Задача 2: CounterButton
class CounterButton:
    def __init__(self):
        self._count = 0
    
    def press(self):
        self._count += 1
    
    def count(self):
        return self._count
    
    def reset(self):
        self._count = 0
#Задача 3: SeeSaw
class SeeSaw:
    def __init__(self):
        self.left_weight = 0
        self.right_weight = 0
    
    def add_left(self, weight):
        self.left_weight += weight
    
    def add_right(self, weight):
        self.right_weight += weight
    
    def balance(self):
        if self.left_weight > self.right_weight:
            return 'L'
        elif self.right_weight > self.left_weight:
            return 'R'
        else:
            return '='
#Задача 4: NumberDivider
class NumberDivider:
    def __init__(self):
        self.divisible_list = []
        self.not_divisible_list = []
    
    def add_number(self, n):
        if n % 3 == 0:
            self.divisible_list.append(n)
        else:
            self.not_divisible_list.append(n)
    
    def divisible(self):
        return self.divisible_list
    
    def not_divisible(self):
        return self.not_divisible_list
#Задача 5: FlipFlopBell
class FlipFlopBell:
    def __init__(self):
        self.flip = True
    
    def ring(self):
        if self.flip:
            print("flip")
        else:
            print("flop")
        self.flip = not self.flip
#Задача 6: MinMaxNumberFinder
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
#Задача 7: BoundingBox2D
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
#Задача 8: WordCaseSeparator
class WordCaseSeparator:
    def __init__(self):
        self.upper_words = []
        self.lower_words = []
    
    def add_word(self, word):
        if word and word[0].isupper():
            self.upper_words.append(word)
        elif word and word[0].islower():
            self.lower_words.append(word)
    
    def upper_case_words(self):
        return self.upper_words
    
    def lower_case_words(self):
        return self.lower_words
#Задача 9: EvenOddSumTracker
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
#Задача 10: AlternatingCounter
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

