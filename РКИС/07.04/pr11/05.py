
# ================== Задача 5 — Декоратор для логирования ==================
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def say_hello():
    print("Hello!")

# Проверка задачи 5
print("\n=== Задача 5 ===")
say_hello()
