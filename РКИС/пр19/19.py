import asyncio

async def producer(queue, items):
    for item in items:
        await queue.put(item)
        print(f"Producer: добавлен {item}")
        await asyncio.sleep(0.5)

async def consumer(queue, consumer_id):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"Consumer {consumer_id}: обработан {item}")
        queue.task_done()
        await asyncio.sleep(1)

async def main():
    queue = asyncio.Queue()
    items = ["данные1", "данные2", "данные3", "данные4", "данные5"]

    producer_task = asyncio.create_task(producer(queue, items))
    consumer_tasks = [
        asyncio.create_task(consumer(queue, i)) for i in range(2)
    ]

    await producer_task
    await queue.join()

    for _ in consumer_tasks:
        await queue.put(None)
    await asyncio.gather(*consumer_tasks)

asyncio.run(main())
