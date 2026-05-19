
# ================== Задача 9 — Переопределение инкремента ==================
class Counter:
    def __init__(self, value):
        self.value = value
    
    def __iadd__(self, other):
        self.value += other
        return self
    
    def get_value(self):
        return self.value

# Проверка задачи 9
print("\n=== Задача 9 ===")
c = Counter(5)
c += 3
print(c.get_value())


