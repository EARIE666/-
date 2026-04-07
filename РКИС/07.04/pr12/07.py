
# Задача 7 — Индекс вне диапазона
def get_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index error"

print(get_element([1, 2, 3], 1))
print(get_element([1, 2, 3], 5))


