# File: 18.py
from datetime import datetime

def task18():
    deadline = datetime(2026, 3, 1)
    now = datetime.now()
    if now > deadline:
        print("Дедлайн просрочен!")
    else:
        print("Еще есть время.")
