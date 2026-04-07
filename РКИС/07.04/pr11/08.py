
# ================== Задача 8 — Декоратор для проверки аргументов ==================
def check_positive(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg < 0:
                print("Error")
                return
        for val in kwargs.values():
            if val < 0:
                print("Error")
                return
        return func(*args, **kwargs)
    return wrapper

@check_positive
def multiply(a, b):
    print(a * b)

# Проверка задачи 8
print("\n=== Задача 8 ===")
multiply(3, 4)
multiply(3, -1)
