from multiprocessing import Process
import time

def calculate_sum(start, end, name):
    total = sum(range(start, end + 1))
    print(f"Процесс {name}: сумма от {start} до {end} = {total}")

if __name__ == '__main__':
    p1 = Process(target=calculate_sum, args=(1, 50000, "A"))
    p2 = Process(target=calculate_sum, args=(50001, 100000, "B"))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
