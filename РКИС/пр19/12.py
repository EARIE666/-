import threading
import time

def download_file(file_id):
    print(f"Начало загрузки файла {file_id}")
    time.sleep(2)  # Имитация загрузки
    print(f"Файл {file_id} загружен")

threads = []
for i in range(3):
    t = threading.Thread(target=download_file, args=(i+1,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
