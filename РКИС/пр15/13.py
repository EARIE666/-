# File: 13.py
from datetime import datetime, timedelta

def task13():
    given_date = datetime(2026, 4, 9) # четверг
    days_ahead = 7 - given_date.weekday() # 0 = Пн, значит если сегодня Пн, добавим 7
    if days_ahead <= 0:
        days_ahead += 7
    next_monday = given_date + timedelta(days=days_ahead)
    print(next_monday.date())
