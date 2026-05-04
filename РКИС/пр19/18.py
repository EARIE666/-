import asyncio

async def async_read_file(filename):
    print(f"Начало чтения файла {filename}")
    await asyncio.sleep(2)  # Имитация задержки чтения
    content = f"Содержимое файла {filename}"
    print(f"Файл {filename} прочитан")
    return content

async def main():
    files = ["file1.txt", "file2.txt", "file3.txt"]
    reads = [async_read_file(f) for f in files]
    results = await asyncio.gather(*reads)
    for content in results:
        print(content)

asyncio.run(main())
