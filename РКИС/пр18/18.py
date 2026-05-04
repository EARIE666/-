def count_errors(filename='app.log'):
    count = 0
    try:
        with open(filename, 'r', encoding='utf-8') as log_file:
            for line in log_file:
                if 'ERROR' in line:
                    count += 1
        print(f"Найдено ошибок: {count}")
        return count
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return 0
    except Exception as e:
        print(f"Ошибка при подсчёте: {e}")
        return 0

# Пример использования
error_count = count_errors()
