# File: 03.py
import re   
text = "test@example.com"

def task2(text):
    match = re.search(r"\w+\@\w+\.\w+", text, re.I)
    if match:
        return True
    else:
        return False
        
print(task2(text))
