class Timer:
    __slots__ = ('start', 'end')

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def difference(self):
        return self.end - self.start

timer = Timer(10, 35)
print(f"Разница = {timer.difference()}")