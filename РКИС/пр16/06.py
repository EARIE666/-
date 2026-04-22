# File: 06.py
import re   
text = "Apple and banana are amazing"

def task6(text):
    return re.findall(r"\b[aA]\w+", text)
print(task6(text))
