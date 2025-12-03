import sqlite3
from src.models import Book

class BookRepository:
    def __init__(self, db_name="database.db"):
        self.db_name = db_name
        self._create_table()

    def _connect(self):
        return sqlite3.connect(self.db_name)

    def _create_table(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL,
                    year INTEGER,
                    status TEXT
                )
            """)
            conn.commit()

    def add_book(self, book: Book):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO books (title, author, year, status) VALUES (?, ?, ?, ?)",
                           (book.title, book.author, book.year, book.status))
            conn.commit()

    def get_all(self):
        books = []
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, title, author, year, status FROM books")
            rows = cursor.fetchall()
            for row in rows:
                # Reconstrói o objeto Book a partir do banco
                books.append(Book(id=row[0], title=row[1], author=row[2], year=row[3], status=row[4]))
        return books

    def delete_book(self, book_id):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
            conn.commit()