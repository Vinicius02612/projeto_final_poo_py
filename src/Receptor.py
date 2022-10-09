from Pessoa import Pessoa

class Receptor(Pessoa):

    def __init__(self,id, nome, sobreNome,email, telefone, senha,Livro = ''):
        super().__init__(nome, sobreNome,  email,telefone)
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
    def nome(self):
        return super().nome
    
    @nome.setter
    def nome(self, nome):
        super().nome = nome
        return super().nome
    

    @property
    def sobreNome(self):
        return super().sobreNome
    
    @sobreNome.setter
    def sobreNome(self, SBnome):
        super().sobreNome = SBnome
        return super().sobreNome
    

    
    @property
    def email(self):
        return super()._email
    
    @email.setter
    def email(self, email):
        super()._email = email


    
    @property
    def livro(self):
        return self._livro

    @livro.setter
    def livro(self, livro):
        self._livro = livro
        return self._livro

    @property
    def telefone(self):
        return super()._telefone

    @telefone.setter
    def telefone(self, telefone):
        super()._telefone = telefone
        return super()._telefone

    @property
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self, snh):
        self._senha = snh
        return self._senha
    


    def get_dados(self):
        print('Dados do Doador:\n')
        print(
            f'ID: {self._id}\n'
            f'Nome: {self._nome}\n'
            f'Sobre Nome: {self._sobreNome}\n'
            f'email:{self._email}\n'
            f'Telefone:{self._telefone}\n'
            f'\tLivro: {self._livro}\n'
        )
    
    def __str__(self) -> str:
        return super().__str__()
    