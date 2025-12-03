class Book:
    def __init__(self, title, author, year, status="Disponível", id=None):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self):
        return f"{self.title} - {self.author} ({self.year})"