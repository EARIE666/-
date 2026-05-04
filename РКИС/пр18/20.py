class SafeFileManager:
    """Контекстный менеджер для безопасной работы с файлами."""

    def __init__(self, filename, mode='r', encoding='utf-8'):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode, encoding=self.encoding)
            return self.file
        except Exception as e:
            print(f"Ошибка открытия файла {self.filename}: {e}")
            return None

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        print("File closed")
        # Не подавляем исключения
        return False

# Примеры использования

# Чтение файла (успешно)
with SafeFileManager('app.log', 'r') as file:
    if file:
        content = file.read()
        print("Содержимое файла прочитано")

# Попытка открыть несуществующий файл
with SafeFileManager('nonexistent.txt', 'r') as file:
    if file:
        content = file.read()
    else:
        print("Файл не открыт, операция отменена")
