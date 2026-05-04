import threading
import queue
import time

def producer(q):
    for i in range(5):
        q.put(f"Задача {i}")
        print(f"Произведено: Задача {i}")
        time.sleep(1)

def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Обработано: {item}")
        q.task_done()
        time.sleep(2)

q = queue.Queue()
pt = threading.Thread(target=producer, args=(q,))
ct = threading.Thread(target=consumer, args=(q,))

pt.start()
ct.start()

pt.join()
q.put(None)
ct.join()
