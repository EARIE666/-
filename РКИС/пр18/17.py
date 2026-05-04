def read_error_logs(filename='app.log'):

    try:
        with open(filename, 'r', encoding='utf-8') as log_file:
            for line in log_file:
                if 'ERROR' in line:
                    print(line.rstrip())
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")

# Пример использования
read_error_logs()
