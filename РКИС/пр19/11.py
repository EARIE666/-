from multiprocessing import Pool
import time

def heavy_calculation(n):
    return sum(i * i for i in range(n))

if __name__ == '__main__':
    with Pool(4) as pool:
        results = pool.map(heavy_calculation, [10000] * 4)
    print("Расчёты завершены")
