
# ================== Задача 8 — Переопределение отрицания ==================
class BooleanWrapper:
    def __init__(self, value):
        self.value = value
    
    def __bool__(self):
        return self.value
    
    def __invert__(self):
        return BooleanWrapper(not self.value)

# Проверка задачи 8 (используем not)
print("\n=== Задача 8 ===")
b = BooleanWrapper(True)
print(not b)
c = BooleanWrapper(False)
print(not c)


