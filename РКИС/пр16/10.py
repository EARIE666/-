# File: 10.py
import re   
text = "apple, banana orange,grape"

def task10(text):
    return re.findall(r"\b\w+", text)
        
print(task10(text))
