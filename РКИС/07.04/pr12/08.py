
# Задача 8 — Вложенные try/except
def process_data(a, b):
    try:
        a_num = float(a)
        b_num = float(b)
        try:
            return a_num / b_num
        except ZeroDivisionError:
            return "Division by zero"
    except ValueError:
        return "Conversion error"

print(process_data("10", "2"))
print(process_data("10", "0"))
print(process_data("a", "2"))


