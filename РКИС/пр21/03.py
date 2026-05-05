class WithSlots:
    __slots__ = ('x',)

class WithoutSlots:
    pass

# Объект со slots
ws = WithSlots()
ws.x = 10
try:
    ws.y = 20
    print("Атрибут y добавлен")
except AttributeError:
    print("Со __slots__: нельзя добавить атрибут y")

# Объект без slots
wos = WithoutSlots()
wos.x = 10
wos.y = 20
print(f"Без __slots__: x={wos.x}, y={wos.y}")

print("Вывод: __slots__ запрещает добавление новых атрибутов и экономит память. Без __slots__ атрибуты хранятся в __dict__.")