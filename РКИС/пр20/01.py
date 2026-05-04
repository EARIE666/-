import asyncio

async def simple_async_function():
    print("Начало выполнения")
    await asyncio.sleep(1)
    print("Сообщение после задержки")

asyncio.run(simple_async_function())
