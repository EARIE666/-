import threading
import time

def background_task():
    while True:
        print("Фоновый поток работает...")
        time.sleep(1)

daemon_thread = threading.Thread(target=background_task)
daemon_thread.daemon = True
daemon_thread.start()

time.sleep(5)
print
