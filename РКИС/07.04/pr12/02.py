
# Задача 2 — Перехват ошибки преобразования
def to_int(s):
    try:
        return int(s)
    except ValueError:
        return "Invalid input"

print(to_int("123"))
print(to_int("abc"))


