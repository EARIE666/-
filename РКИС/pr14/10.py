
# Задача 10
def process(a: int, b: int, *args: int, **kwargs: int) -> int:
    return a + b + sum(args) + sum(kwargs.values())

print(process(1, 2, 3, 4, x=5, y=6))
