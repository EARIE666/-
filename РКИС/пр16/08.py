# File: 08.py
import re   
text = "Dates: 2024-01-01 and 2025-12-31" # YYYY-MM-DD.

def task8(text):
    return re.findall(r"\d{4}\-\d{2}\-\d{2}", text)
        
print(task8(text))
