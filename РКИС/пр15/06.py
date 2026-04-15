# File: 06.py
def task6():
    max_len = 0
    max_line = ""
    with open('input.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n')
            if len(line) > max_len:
                max_len = len(line)
                max_line = line
    print(f"Длина: {max_len}")
    print(f"Строка: {max_line}")
