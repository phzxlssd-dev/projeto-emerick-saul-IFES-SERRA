import sqlite3
from src.models import Usuario, Aluno, Professor, Resultado


class ResultadoRepository:
    def init(self, db_name="database.db"):
        self.db_name = db_name
        self._create_tables()

    def _connect(self):
        return sqlite3.connect(self.db_name)

    def _create_tables(self):
        with self._connect() as conn:
            cursor = conn.cursor()

            # tabela usuários
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL,
                    tipo TEXT NOT NULL
                )
            """)

            # tabela resultados CSV
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS resultados (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    aluno_nome TEXT NOT NULL,
                    arquivo_csv TEXT NOT NULL
                )
            """)

            conn.commit()
                    #usuários
    def add_usuario(self, usuario):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO usuarios (nome, email, tipo) VALUES (?, ?, ?)",
                (usuario.nome, usuario.email, usuario.tipo)
            )
            conn.commit()

    def get_usuarios(self):
        usuarios = []
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nome, email, tipo FROM usuarios")
            rows = cursor.fetchall()

            for r in rows:
                if r[3] == "aluno":
                    usuarios.append(Aluno(nome=r[1], email=r[2], id=r[0]))
                else:
                    usuarios.append(Professor(nome=r[1], email=r[2], id=r[0]))

        return usuarios

    # ------------- RESULTADOS CSV -------------
    def add_resultado(self, resultado):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO resultados (aluno_nome, arquivo_csv) VALUES (?, ?)",
                (resultado.aluno_nome, resultado.arquivo_csv)
            )
            conn.commit()

    def get_resultados(self):
        resultados = []
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, aluno_nome, arquivo_csv FROM resultados")
            rows = cursor.fetchall()

            for r in rows:
                resultados.append(Resultado(id=r[0], aluno_nome=r[1], arquivo_csv=r[2]))

        return resultados

    def delete_resultado(self, resultado_id):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM resultados WHERE id = ?", (resultado_id,))
            conn.commit()
