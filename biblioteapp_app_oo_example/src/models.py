class Usuario:
    def init(self, nome, email, tipo, id=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.tipo = tipo  

    def str(self):
        return f"{self.nome} ({self.tipo})"


class Aluno(Usuario):
    def init(self, nome, email, id=None):
        super().init(nome, email, "aluno", id=id)


class Professor(Usuario):
    def init(self, nome, email, id=None):
        super().init(nome, email, "professor", id=id)


class Resultado:
    def init(self, aluno_nome, arquivo_csv, id=None):
        self.id = id
        self.aluno_nome = aluno_nome
        self.arquivo_csv = arquivo_csv  

    def str(self):
        return f"Resultado de {self.aluno_nome}"
