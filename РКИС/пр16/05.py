# File: 05.py
import re   
text = "abc123def45"

def task5(text):
    return re.sub(r"\d", "", text)
print(task5(text))
