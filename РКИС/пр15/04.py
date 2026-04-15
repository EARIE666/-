# File: 04.py
def task4():
    total_age = 0
    count = 0
    with open('data.csv', 'r', encoding='utf-8') as f:
        next(f) # Пропускаем заголовок
        for line in f:
            name, age = line.strip().split(',')
            total_age += int(age)
            count += 1
    if count > 0:
        print(total_age / count)
