
# ================== Задача 2 — Перегрузка метода с разными аргументами ==================
class Multiplier:
    def multiply(self, a, b=None):
        if b is None:
            return a * a
        return a * b

# Проверка задачи 2
print("\n=== Задача 2 ===")
m = Multiplier()
print(m.multiply(5))
print(m.multiply(2, 3))
