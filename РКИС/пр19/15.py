import asyncio

async def task(name, delay):
    print(f"Задача {name} началась")
    await asyncio.sleep(delay)
    print(f"Задача {name} завершена")

async def main():
    await asyncio.gather(
        task("A", 1),
        task("B", 2),
        task("C", 1.5)
    )

asyncio.run(main())
