
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
