class Product:
    __slots__ = ('name', '_price')

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Цена не может быть отрицательной!")
        self._price = value

prod = Product("Телефон", 50000)
print(f"{prod.name} стоит {prod.price}")

try:
    prod.price = -100
except ValueError as e:
    print(f"Ошибка: {e}")