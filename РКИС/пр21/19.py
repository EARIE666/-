class Order:
    __slots__ = ('items',)

    def __init__(self, items):
        self.items = items

    def total_cost(self):
        return sum(self.items)

order = Order([150, 200, 350, 100])
print(f"Общая стоимость = {order.total_cost()}")