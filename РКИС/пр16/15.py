# File: 15.py
import re   
text = "Сделайте первую букву каждого слова заглавной с помощью re."

def task15(text):
    return re.sub(r"\b\w", lambda m: m.group().upper(), text)
        
print(task15(text))
