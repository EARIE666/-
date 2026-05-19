
class Logger:
    def log(self, data):
        print(f"Log: {data}")

class ListLogger(Logger):
    def log(self, data):
        print(f"List log: {data}")

class DictLogger(Logger):
    def log(self, data):
        print(f"Dict log: {data}")
