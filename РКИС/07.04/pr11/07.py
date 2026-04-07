
# ================== Задача 7 — Комбинированная перегрузка ==================
class Adder:
    def add(self, a, b=None):
        if b is None:
            return a + 10
        return a + b

# Проверка задачи 7
print("\n=== Задача 7 ===")
a = Adder()
print(a.add(5))
print(a.add(3, 4))
