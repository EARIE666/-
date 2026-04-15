# File: 11.py
from datetime import datetime

def task11():
    date_str = "2024-12-31"
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    print(f"День: {date_obj.day}")
    print(f"Месяц: {date_obj.month}")
    print(f"Год: {date_obj.year}")
