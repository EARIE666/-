# File: 10.py
def task10():
    with open('input.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    unique_lines = list(dict.fromkeys(lines)) # сохраняет порядок
    
    with open('unique.txt', 'w', encoding='utf-8') as f:
        f.writelines(unique_lines)
