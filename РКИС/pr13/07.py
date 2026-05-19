
# Задача 7
class Person:
    def __init__(self, name):
        self.name = name
    
    @classmethod
    def from_string(cls, s):
        return cls(s)

p = Person.from_string("Alice")
print(p.name)  # Alice

