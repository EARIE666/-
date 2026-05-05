class Animal:
    __slots__ = ('type', 'weight')

a = Animal()
a.type = "Собака"
a.weight = 15.5

try:
    a.color = "Коричневый"
except AttributeError as e:
    print(f"Ошибка: {e}")
    print("Объяснение: добавить атрибут 'color' нельзя, так как __slots__ разрешает только 'type' и 'weight'.")