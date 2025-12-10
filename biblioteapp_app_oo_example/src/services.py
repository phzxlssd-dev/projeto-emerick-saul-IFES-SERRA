import os
import pandas as pd
from datetime import datetime
from src.models import Aluno, Professor, Resultado
from src.repository import ResultadoRepository


class SistemaService:
    def init(self):
        self.repo = ResultadoRepository()

        # Pasta para armazenar uploads CSV
        self.upload_path = "uploads"
        os.makedirs(self.upload_path, exist_ok=True)

    # ---------- Usuários ----------
    def cadastrar_aluno(self, nome, email):
        aluno = Aluno(nome, email)
        self.repo.add_usuario(aluno)
        return "Aluno cadastrado com sucesso!"

    def cadastrar_professor(self, nome, email):
        prof = Professor(nome, email)
        self.repo.add_usuario(prof)
        return "Professor cadastrado com sucesso!"

    def listar_usuarios(self):
        return self.repo.get_usuarios()

    # ---------- Resultados CSV ----------
    def enviar_resultado_csv(self, aluno_nome, arquivo_streamlit):
        file_path = os.path.join(self.upload_path, arquivo_streamlit.name)
        with open(file_path, "wb") as f:
            f.write(arquivo_streamlit.getbuffer())

        resultado = Resultado(aluno_nome, file_path)
        self.repo.add_resultado(resultado)
        return "Arquivo CSV enviado com sucesso!"

    def listar_resultados(self):
        return self.repo.get_resultados()

    def remover_resultado(self, resultado_id):
        self.repo.delete_resultado(resultado_id)
        return "Resultado removido!"
