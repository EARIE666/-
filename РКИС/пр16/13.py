# File: 13.py
import re   
text = "Посетите наш сайт https://google.com и страницу http://example.org для подробностей."

def task13(text):
    return re.findall(r"\w+\:\//\w+\.\w+", text)
        
print(task13(text))
