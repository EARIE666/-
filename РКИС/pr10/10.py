
# ================== Задача 10 — Комплексное переопределение ==================
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"

# Проверка задачи 10
print("\n=== Задача 10 ===")
v1 = Vector2D(1, 2)
v2 = Vector2D(3, 4)
v3 = v1 + v2
v4 = v2 - v1
print(v3)
print(v4)
