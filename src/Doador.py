
from Pessoa import Pessoa


class Doador(Pessoa):
    
    def __init__(self, id,nome, sobreNome, email,telefone,senha,Livro = ''):
        super().__init__(nome, sobreNome, email,telefone)
        self._id = id
        self._livro = Livro
        self._senha = senha

    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
        return self._id
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, em):
        self._email = em
        return self._email



    @property
    def email(self):
        return super()._email
    
    @email.setter
    def email(self, email):
        super()._email = email



    @property
    def telefone(self):
        return super()._telefone

    @telefone.setter
    def telefone(self, telefone):
        super()._telefone = telefone
        return super()._telefone
    
    @property
    def livro(self):
        return self._livro

    @livro.setter
    def livro(self, livro):
        self._livro = livro
        return self._livro


    @property
    def senha(self):
        return super()._senha
    
    @senha.setter
    def senha(self, snh):
        super()._senha = snh
        return super()._senha
    
    @property
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self, senha):
        self._senha = senha
        return self._senha
    
    def doar_livro(self, recebe, lvr):
        recebe._livro += lvr

    
    def get_dados(self):
        print('Dados do Receptor:\n')
        print(
            f'ID: {self._id}\n'
            f'Nome: {self._nome}\n'
            f'Sobre Nome: {self._sobreNome}\n'
            f'email:{self._email}\n'
            f'Telefone:{self._telefone}\n'
            f'Livros: {self._livro}\n'
        )
    
    """ def __repr__(self):
        return f'Nome: {self._nome}\n Sobre Nome: {self._sobreNome}\nEmail: {self._email}\nEndereco:{self._endereco}\nTelefone:{self._telefone}' """