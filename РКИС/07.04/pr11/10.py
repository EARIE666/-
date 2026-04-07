
# ================== Задача 10 — Перегрузка + декоратор + наследование ==================
def log_call(func):
    def wrapper(*args, **kwargs):
        print("Function called")
        return func(*args, **kwargs)
    return wrapper

class Calculator:
    def calculate(self, x, y=None):
        if y is None:
            return x * x
        return x + y

class AdvancedCalculator(Calculator):
    def calculate(self, x, y=None):
        result = super().calculate(x, y)
        return result + 10

# Проверка задачи 10
print("\n=== Задача 10 ===")
calc = AdvancedCalculator()
calc.calculate = log_call(calc.calculate)
print(calc.calculate(5))     # квадрат 5 = 25 + 10 = 35
print(calc.calculate(2, 3))  # сумма 2+3 = 5 + 10 = 15
