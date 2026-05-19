
# ================== Задача 5 — Переопределение сравнения ==================
class ComparableNumber:
    def __init__(self, value):
        self.value = value
    
    def __lt__(self, other):
        return self.value < other.value
    
    def get_value(self):
        return self.value

# Проверка задачи 5
print("\n=== Задача 5 ===")
a = ComparableNumber(5)
b = ComparableNumber(10)
print(a < b)
print(b < a)


