# File: 03.py
import string

def task3():
    with open('input.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Удаляем все знаки пунктуации
    translator = str.maketrans('', '', string.punctuation)
    clean_text = text.translate(translator)
    
    with open('clean.txt', 'w', encoding='utf-8') as f:
        f.write(clean_text)
