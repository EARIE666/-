
# Задача 6 — Обработка списка
def safe_sum(lst):
    total = 0
    for item in lst:
        try:
            total += item
        except TypeError:
            continue
    return total

print(safe_sum([1, 2, "a", 3]))


