
# Задача 6
def print_info(**kwargs: str) -> None:
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", city="Paris")


