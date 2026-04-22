# File: 18.py
import re

card = "1234 5678 9012 3456"

# Заменяем все цифры кроме последних 4 на *
result = re.sub(r"\d(?=.*\d{4})", "*", card)

print(result)  # **** **** **** 3456
