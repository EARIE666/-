# File: 19.py
from datetime import datetime

def task19(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] {message}\n")
