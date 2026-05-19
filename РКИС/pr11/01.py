
# ================== Задача 1 — Переопределение метода ==================
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")

# Проверка задачи 1
print("=== Задача 1 ===")
animals = [Dog(), Cat(), Animal()]
for a in animals:
    a.speak()
