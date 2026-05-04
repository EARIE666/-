import threading
from multiprocessing import Process
import time

def cpu_intensive_task(n):
    total = 0
    for i in range(n):
        total += i ** 2
    return total

def test_threads():
    threads = []
    start_time = time.time()

    for _ in range(2):
        t = threading.Thread(target=cpu_intensive_task, args=(100000,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    thread_time = time.time() - start_time
    print(f"Время с потоками: {thread_time:.2f} сек")

def test_processes():
    processes = []
    start_time = time.time()

    for _ in range(2):
        p = Process(target=cpu_intensive_task, args=(100000,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    process_time = time.time() - start_time
    print(f"Время с процессами: {process_time:.2f} сек")

test_threads()
test_processes()
