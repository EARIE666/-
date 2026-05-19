
# ================== Задача 2 — Переопределение вычитания ==================
class NumberWrapperSub:
    def __init__(self, value):
        self.value = value
    
    def __sub__(self, other):
        return NumberWrapperSub(self.value - other.value)
    
    def get_value(self):
        return self.value

# Проверка задачи 2
print("\n=== Задача 2 ===")
a = NumberWrapperSub(10)
b = NumberWrapperSub(3)
c = a - b
print(c.get_value())


