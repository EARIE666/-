# File: 09.py
import re   
password = "abcdefg2"

def task9(password):
    if re.search(r"\d", password) and re.search(r"\w", password) and len(password) >= 8:
        return True
    else:
        return False
        
print(task9(password))
