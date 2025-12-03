class Pessoa:
    def __init__(self, nome, email, tipo, status="Disponível",id=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.tipo = tipo
        self.status = status

    def __str__(self):
        return f"{self.nome} - {self.email} - {self.id} ({self.status})"
