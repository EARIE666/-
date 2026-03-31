
class Printer:
    def print_message(self, msg):
        print(f"Message: {msg}")

class UpperCasePrinter(Printer):
    def print_message(self, msg):
        print(msg.upper())
