
# Задача 9 — Использование else
def safe_print_number(s):
    try:
        num = int(s)
    except ValueError:
        print("Error")
    else:
        print(num)

safe_print_number("5")
safe_print_number("abc")

