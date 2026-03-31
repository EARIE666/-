
class Calculator:
    def calculate(self, x, y):
        return x + y

class SafeCalculator(Calculator):
    def calculate(self, x, y):
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            return x + y
        return "Error"
