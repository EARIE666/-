import threading
import time

def delayed_task(name, delay):
    print(f"{name} начал выполнение")
    time.sleep(delay)
    print(f"{name} завершил выполнение")

t1 = threading.Thread(target=delayed_task, args=("Быстрый поток", 0.5))
t2 = threading.Thread(target=delayed_task, args=("Медленный поток", 2))

t1.start()
t2.start()

t1.join()
t2.join()
