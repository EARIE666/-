# File: 02.py
import re   
text = "There are 12 apples and 5 bananas"

def task2(text):
    match = re.findall(r"\d+", text)
    return match
        
print(task2(text))
