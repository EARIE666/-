# File: 14.py
import re   
text = "hello hello world"

def task14(text):
    return re.findall(r"\b(\w+)\s+\1\b", text)
        
print(task14(text))
