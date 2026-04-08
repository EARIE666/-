
# Задача 9
class ListProcessor:
    @staticmethod
    def double(numbers):
        return list(map(lambda x: x * 2, numbers))

print(ListProcessor.double([1, 2, 3]))  # [2, 4, 6]

