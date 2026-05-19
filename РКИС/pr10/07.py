
# ================== Задача 7 — Переопределение строки ==================
class Person:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Person: {self.name}"

# Проверка задачи 7
print("\n=== Задача 7 ===")
p = Person("Alice")
print(p)


