# File: 16.py
import re   
text = "213.123.56.132"

def task16(text):
    match = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", text)
    if match:
        return True
    else:
        return False
        
print(task16(text))
