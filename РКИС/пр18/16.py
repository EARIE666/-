from datetime import datetime

def write_log(message, filename='app.log'):

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f'[{timestamp}] {message}\n'
    with open(filename, 'a', encoding='utf-8') as log_file:
        log_file.write(log_entry)

# Пример использования
write_log('Приложение запущено')
write_log('Произошла ошибка подключения')
