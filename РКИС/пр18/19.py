class SimpleContextManager:

    def __enter__(self):
        print("Start")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("End")
        return False

# Пример использования
with SimpleContextManager():
    print("Выполняется код внутри блока with")
