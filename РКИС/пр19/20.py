import asyncio
import random

async def worker(worker_id, task_queue):
    while True:
        task = await task_queue.get()
        if task is None:
            print(f"Worker {worker_id}: завершает работу")
            break

        delay = random.uniform(1, 3)
        print(f"Worker {worker_id}: начал задачу {task} (задержка: {delay:.2f}с)")
        await asyncio.sleep(delay)
        print(f"Worker {worker_id}: завершил задачу {task}")
        task_queue.task_done()

async def main():
    task_queue = asyncio.Queue()

    workers = [
        asyncio.create_task(worker(i, task_queue)) for i in range(3)
    ]

    for task_id in range(10):
        await task_queue.put(f"Task-{task_id}")

    await task_queue.join()

    for _ in workers:
        await task_queue.put(None)
    await asyncio.gather(*workers)

asyncio.run(main())
