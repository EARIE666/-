import os

if os.path.exists('data.txt'):
    file_size = os.path.getsize('data.txt')
    print(f"Размер файла: {file_size} байт")
