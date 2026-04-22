# File: 12.py
import re   
text = "<p>Hello</p>"

def task12(text):
    return re.sub(r"\<\/?\w{1}\>", "", text)
        
print(task12(text))
