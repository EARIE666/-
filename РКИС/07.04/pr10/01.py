# ================== Задача 1 — Переопределение сложения ==================
class NumberWrapper:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        return NumberWrapper(self.value + other.value)
    
    def get_value(self):
        return self.value

# Проверка задачи 1
print("=== Задача 1 ===")
a = NumberWrapper(5)
b = NumberWrapper(10)
c = a + b
print(c.get_value())


