# File: 17.py
import re

log = "2024-01-15 10:30:45 INFO Пользователь вошёл в систему"

pattern = r"(\d{4}-\d{2}-\d{2})\s+\d{2}:\d{2}:\d{2}\s+(\w+)\s+(.+)"

match = re.search(pattern, log)

if match:
    date = match.group(1)
    level = match.group(2)
    message = match.group(3)
    
    print(f"Дата: {date}")
    print(f"Уровень: {level}")
    print(f"Сообщение: {message}")
