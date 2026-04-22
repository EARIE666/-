# File: 01.py
import re   
text = "I love Python programming"
match = re.search("python", text, re.I)

def task1(text):
    if match:
        return "Да"
    else:
        return "Нет"
        
print(task1(text))
