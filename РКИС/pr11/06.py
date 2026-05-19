
# ================== Задача 6 — Декоратор с аргументами ==================
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hi!")

# Проверка задачи 6
print("\n=== Задача 6 ===")
greet()
