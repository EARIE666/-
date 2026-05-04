import threading
import time

def print_name(name):
    for _ in range(5):
        print(f"Поток {name}")
        time.sleep(0.3)

threads = []
for i in range(3):
    t = threading.Thread(target=print_name, args=(f"Thread-{i+1}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
