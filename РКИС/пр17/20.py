import random
import os
from datetime import datetime

file_path = 'numbers.txt'

# 1. Генерирует 5 случайных чисел
numbers = [random.randint(1, 100) for _ in range(5)]

# 3. Подготовка даты
current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# 2. Сохраняет их в файл (с датой)
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(f"Дата записи: {current_date}\n")
    f.write("Случайные числа: " + ", ".join(map(str, numbers)) + "\n")

# 4. Проверяет существование файла
if os.path.exists(file_path):
    print(f"Файл {file_path} успешно создан.")
    
    # 5. Читает файл и выводит содержимое
    with open(file_path, 'r', encoding='utf-8') as f:
        print("\nСодержимое файла:")
        print(f.read())
