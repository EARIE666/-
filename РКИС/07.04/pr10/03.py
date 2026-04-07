
# ================== Задача 3 — Переопределение умножения ==================
class Multiplier:
    def __init__(self, value):
        self.value = value
    
    def __mul__(self, other):
        return Multiplier(self.value * other.value)
    
    def get_value(self):
        return self.value

# Проверка задачи 3
print("\n=== Задача 3 ===")
a = Multiplier(4)
b = Multiplier(5)
c = a * b
print(c.get_value())


