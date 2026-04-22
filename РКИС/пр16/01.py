# File: 01.py
import re   
text = "I love Python programming"

def task1(text):
    match = re.search("python", text, re.I)
    if match:
        return True
    else:
        return False
        
print(task1(text))
