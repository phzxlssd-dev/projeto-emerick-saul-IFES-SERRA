from datetime import datetime
from src.models import Book
from src.repository import BookRepository

class LibraryService:
    def __init__(self):
        self.repository = BookRepository()

    def register_book(self, title, author, year):
        # Regra de Negócio: Validação simples
        if not title or not author:
            return "Erro: Título e Autor são obrigatórios."
        
        current_year = datetime.now().year
        if year > current_year:
            return "Erro: O ano não pode ser futuro."

        new_book = Book(title=title, author=author, year=year)
        self.repository.add_book(new_book)
        return "Sucesso: Livro adicionado!"

    def list_books(self):
        return self.repository.get_all()

    def remove_book(self, book_id):
        self.repository.delete_book(book_id)