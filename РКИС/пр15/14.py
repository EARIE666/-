# File: 14.py
from datetime import datetime

def task14():
    birth_str = input("Введите дату рождения (ГГГГ-ММ-ДД): ")
    birth = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()
    delta = today - birth
    print(f"Возраст в днях: {delta.days}")
