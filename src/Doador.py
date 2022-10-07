
from Pessoa import Pessoa


class Doador(Pessoa):
    
    def __init__(self, nome, sobreNome, email, endereco,telefone,senha ):
        super().__init__(nome, sobreNome)
        self._email = email
        self._endereco = endereco
        self._telefone = telefone
        self._senha = senha

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, em):
        self._email = em
        return self._email
    
    @property
    def endereco(self):
        return self._endereco
    

    @endereco.setter
    def endereco(self, end):
        self._endereco = end
        return self._endereco

    @property
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self, senha):
        self._senha = senha
        return self._senha
    
    def get_dados_doador(self):
        print('Dados do Doador:\n')
        print(f'Nome: {self._nome}\n Sobre Nome: {self._sobreNome}\nEmail: {self._email}\nEndereco:{self._endereco}\nTelefone:{self._telefone}')
    
    def __repr__(self):
        return f'Nome: {self._nome}\n Sobre Nome: {self._sobreNome}\nEmail: {self._email}\nEndereco:{self._endereco}\nTelefone:{self._telefone}'