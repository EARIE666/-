# File: 07.py
import re   
text = "+37112345678" #: +371XXXXXXXX (Латвия)

def task7(text):
    match = re.search(r"\+\d{11}$", text)
    if match:
        return True
    else:
        return False
        
print(task7(text))
