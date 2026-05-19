
# Задача 6
class Validator:
    @staticmethod
    def is_positive(n):
        return n > 0

print(Validator.is_positive(5))   # True
print(Validator.is_positive(-3))  # False

