# File: 05.py
def task5():
    with open('data.csv', 'r', encoding='utf-8') as f_in:
        lines = f_in.readlines()
    
    with open('filtered.csv', 'w', encoding='utf-8') as f_out:
        f_out.write(lines[0]) # заголовок
        for line in lines[1:]:
            name, age = line.strip().split(',')
            if int(age) > 25:
                f_out.write(line)
