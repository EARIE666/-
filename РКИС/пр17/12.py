# File: 12.py
from datetime import datetime, timedelta

def task12():
    start = datetime(2026, 4, 1)
    end = datetime(2026, 4, 15)
    
    current = start
    workdays = 0
    while current <= end:
        if current.weekday() < 5: # Пн-Пт
            workdays += 1
        current += timedelta(days=1)
    print(workdays)
