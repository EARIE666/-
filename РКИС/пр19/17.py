import asyncio
import time

async def delayed_task(task_id, delay):
    start_time = time.time()
    print(f"Задача {task_id} запущена, задержка: {delay}с")
    await asyncio.sleep(delay)
    end_time = time.time()
    print(f"Задача {task_id} завершена через {end_time - start_time:.2f}с")

async def main():
    tasks = [
        delayed_task(1, 3),
        delayed_task(2, 1),
        delayed_task(3, 2),
        delayed_task(4, 0.5),
        delayed_task(5, 1.5)
    ]
    await asyncio.gather(*tasks)

asyncio.run(main())
