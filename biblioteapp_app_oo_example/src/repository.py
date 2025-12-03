import sqlite3
from src.models import Pessoa

class PessoaRepository:
   
    def __init__(self, db_name="database.db"):
        self.db_name = db_name
        self._create_table()

    def _connect(self):
        return sqlite3.connect(self.db_name)

    def _create_table(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Registro (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    tipo TEXT NOT NULL,
                    status TEXT
                )
            """)
            conn.commit()

    def add_pessoa(self, pessoa: Pessoa): 
        with self._connect() as conn:
            cursor = conn.cursor()
         
            cursor.execute("INSERT INTO Registro (name, email, tipo, status) VALUES (?, ?, ?, ?)",
                           
                           (pessoa.name, pessoa.email, pessoa.tipo, pessoa.status))
            conn.commit()

    def get_all(self):
        pessoas = []
        with self._connect() as conn:
            cursor = conn.cursor()
            
            cursor.execute("SELECT id, name, email, tipo, status FROM Registro")
            rows = cursor.fetchall()
            for row in rows:
               
                pessoas.append(Pessoa(id=row[0], name=row[1], email=row[2], tipo=row[3], status=row[4]))
        return pessoas

    def delete_pessoa(self, pessoa_id): 
        with self._connect() as conn:
            cursor = conn.cursor()
            
            cursor.execute("DELETE FROM Registro WHERE id = ?", (pessoa_id,))
            conn.commit()
