# File: 17.py
import time
from datetime import datetime

def task17():
    now = datetime.now()
    timestamp = int(time.mktime(now.timetuple()))
    print(f"Timestamp: {timestamp}")
    
    back_to_date = datetime.fromtimestamp(timestamp)
    print(f"Обратно: {back_to_date}")
