# File: 20.py
import re

logs = """2026-04-01 ERROR Failed
2026-04-01 INFO OK
2026-04-02 ERROR Crash"""

# 1. Найти только строки с ERROR
error_lines = re.findall(r"^.*ERROR.*$", logs, re.MULTILINE)
print("Строки с ERROR:")
for line in error_lines:
    print(f"  {line}")

# 2. Извлечь даты
dates = re.findall(r"\d{4}-\d{2}-\d{2}", logs)
print(f"\nВсе даты: {dates}")

# 3. Посчитать количество ошибок по датам
from collections import Counter

error_dates = re.findall(r"(\d{4}-\d{2}-\d{2}) ERROR", logs)
counter = Counter(error_dates)

print("\nКоличество ошибок по датам:")
for date, count in counter.items():
    print(f"  {date}: {count}")
