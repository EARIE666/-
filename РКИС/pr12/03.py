
# Задача 3 — Обработка нескольких исключений
def safe_operation(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        return "Type error"

print(safe_operation(10, 2))
print(safe_operation(5, 0))
print(safe_operation(5, "a"))


