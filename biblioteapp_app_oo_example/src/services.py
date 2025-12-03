from datetime import datetime
from src.models import Pessoa, Aluno, Professor
from src.repository import UserRepository 

class UserService:
    """
    Camada de Serviço responsável pela Lógica de Negócios e Validações
    para o registro de Pessoas (Alunos/Professores).
    """
    def __init__(self):
      
        self.repository = UserRepository()

    def register_user(self, nome, email, tipo, **kwargs):
        """
        Registra um novo usuário (Aluno ou Professor) após validações.
        **kwargs recebe os campos específicos (matricula, curso, codigo_servidor, etc.).
        """
       
        if not nome or not email or not tipo:
            return "Erro: Nome, Email e Tipo (Aluno/Professor) são obrigatórios."
        
       
        if 'year' in kwargs and kwargs['year'] is not None:
            try:
            
                year = int(kwargs['year'])
                current_year = datetime.now().year
                if year > current_year:
                    return f"Erro: O ano ({year}) não pode ser futuro."
            except ValueError:
                return "Erro: O ano deve ser um valor numérico válido."
                
       
        
        new_user = None
        
        if tipo.lower() == 'aluno':
            
            if 'matricula' not in kwargs or 'curso' not in kwargs:
                 return "Erro: Matrícula e Curso são obrigatórios para Alunos."
                 
            new_user = Aluno(
                nome=nome,
                email=email,
                matricula=kwargs['matricula'],
                curso=kwargs['curso'],
                ano_ingresso=kwargs.get('year'),
                status=kwargs.get('status', 'Ativo')
            )
            
        elif tipo.lower() == 'professor':
         
            if 'codigo_servidor' not in kwargs or 'departamento' not in kwargs:
                return 
                
            new_user = Professor(
                nome=nome,
                email=email,
                codigo_servidor=kwargs['codigo_servidor'],
                departamento=kwargs['departamento'],
                cargo=kwargs.get('cargo', 'Padrão'),
                status=kwargs.get('status', 'Ativo')
            )

        if new_user:
            self.repository.add_user(new_user)
            return f"Sucesso: {tipo} {nome} adicionado(a)!"
        else:
            return 


    def list_users(self):
       
        return self.repository.get_all_users()

    def remove_user(self, user_id):
  
        self.repository.delete_user(user_id)
        return 

    def professor_view_students(self):
       
        return self.repository.get_students_data()
