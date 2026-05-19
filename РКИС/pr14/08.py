
# Задача 8
def average(*args: float) -> float:
    return sum(args) / len(args) if args else 0.0

print(average(2, 4, 6))


