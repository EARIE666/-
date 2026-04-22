# File: 11.py
import re   
text = "app, banana orange, gra"

def task9(text):
    return re.sub(r"\b\w{3}\b", "***", text)
        
print(task9(text))
