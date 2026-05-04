import threading
import queue
import time

def worker(q):
    while True:
        task = q.get()
        if task is None:
            break
        print(f"Worker обрабатывает: {task}")
        time.sleep(1)
        q.task_done()

q = queue.Queue()
workers = []

for i in range(3):
    t = threading.Thread(target=worker, args=(q,))
    t.start()
    workers.append(t)

for task in range(10):
    q.put(f"Задача-{task}")

for _ in workers:
    q.put(None)
for t in workers:
    t.join()
