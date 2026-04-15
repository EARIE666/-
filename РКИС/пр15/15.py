# File: 15.py
from datetime import datetime

def task15():
    dates_str = ["2023-05-10", "2020-01-01", "2024-12-31"]
    dates_obj = [datetime.strptime(d, "%Y-%m-%d") for d in dates_str]
    dates_obj.sort()
    for d in dates_obj:
        print(d.date())
