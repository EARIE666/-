# File: 04.py
import re   
text = "Hell1o world Python"

def task4(text):
    return re.sub(r"\s", "_", text)
print(task4(text))
