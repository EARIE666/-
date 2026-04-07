
# ================== Задача 9 — Переопределение + декоратор ==================
def excited(func):
    def wrapper(*args, **kwargs):
        print("Let's go!")
        return func(*args, **kwargs)
    return wrapper

class Worker:
    def work(self):
        print("Working...")

class Teacher(Worker):
    def work(self):
        print("Teaching...")

# Проверка задачи 9
print("\n=== Задача 9 ===")
t = Teacher()
t.work = excited(t.work)
t.work()
