import asyncio

async def async_task(name, delay):
    await asyncio.sleep(delay)
    return f"Задача {name} выполнена за {delay} сек"

async def main():
    results = await asyncio.gather(
        async_task("X", 1),
        async_task("Y", 2),
        async_task("Z", 1.5)
    )
    for result in results:
        print(result)

asyncio.run(main())
