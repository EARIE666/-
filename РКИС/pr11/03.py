# ================== Задача 3 — Переопределение конструктора ==================
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position

# Проверка задачи 3
print("\n=== Задача 3 ===")
e = Employee("Alice", 30, "Teacher")
print(e.name, e.age, e.position)
