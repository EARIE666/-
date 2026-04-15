# File: 16.py
from datetime import datetime

def task16():
    now = datetime.now()
    # или заданная: now = datetime(2024, 1, 1, 14, 30)
    formatted = now.strftime("%d %B %Y, %H:%M")
    print(formatted)
