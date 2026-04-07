
# Задача 5 — Пользовательское исключение
def check_age(age):
    try:
        if age < 0:
            raise ValueError
        return "OK"
    except ValueError:
        return "Invalid age"

print(check_age(20))
print(check_age(-5))


