class Book:
    __slots__ = ('title', 'author')

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        print(f"{self.title} - {self.author}")

book = Book("Война и мир", "Л.Н. Толстой")
book.info()