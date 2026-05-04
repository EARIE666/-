import argparse
import sys
import os

def create_files(count, prefix="", extension=".py", digits=2):
    """
    Универсальная функция создания нумерованных файлов
    """
    created = 0
    for i in range(1, count + 1):
        filename = f"{prefix}{i:0{digits}d}{extension}"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"# File: {filename}\n")
        print(f"✓ Created: {filename}")
        created += 1
    return created

def interactive_mode():
    """Интерактивный режим для работы в IDLE"""
    print("=== Генератор Python файлов ===\n")
    
    while True:
        try:
            count = int(input("Сколько файлов создать? "))
            if count <= 0:
                print("Количество должно быть положительным числом")
                continue
            break
        except ValueError:
            print("Ошибка: введите целое число")
    
    prefix = input("Префикс имени (Enter для пропуска): ").strip()
    
    while True:
        try:
            digits = input("Количество цифр в номере (по умолчанию 2): ").strip()
            digits = int(digits) if digits else 2
            if digits <= 0:
                print("Количество цифр должно быть положительным")
                continue
            break
        except ValueError:
            print("Ошибка: введите целое число")
    
    print(f"\nСоздаю {count} файлов...")
    created = create_files(count, prefix=prefix, digits=digits)
    print(f"\nГотово! Создано {created} файлов в папке: {os.getcwd()}")

def main():
    # Проверяем, были ли переданы аргументы командной строки
    if len(sys.argv) > 1:
        # Режим командной строки
        parser = argparse.ArgumentParser(description="Создание нумерованных .py файлов")
        parser.add_argument("count", type=int, help="Количество файлов")
        parser.add_argument("-p", "--prefix", default="", help="Префикс имени файла")
        parser.add_argument("-d", "--digits", type=int, default=2, help="Количество цифр в номере")
        parser.add_argument("-s", "--start", type=int, default=1, help="Начальный номер")
        
        args = parser.parse_args()
        
        for i in range(args.start, args.start + args.count):
            filename = f"{args.prefix}{i:0{args.digits}d}.py"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"# {filename}\n")
            print(f"✓ {filename}")
    else:
        # Интерактивный режим для IDLE
        interactive_mode()

if __name__ == "__main__":
    main()
