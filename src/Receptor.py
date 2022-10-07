from Pessoa import Pessoa

class Receptor(Pessoa):

    def __init__(self, nome, sobreNome, endereco, email,telefone, senha):
        super().__init__(nome, sobreNome)
        self._endereco = endereco
        self._email = email
        self._telefone = telefone
        self._senha =senha
       
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
    def endereco(self):
        return self._endereco
    
    @endereco.setter
    def endereco(self, end):
        self._endereco = end
        return self._endereco
    
    def get_dados_receptor(self):
        print('Dados do Doador:\n')
        print(f'Nome: {self._nome}\n Sobre Nome: {self._sobreNome}\nEmail: {self._email}\nEndereco:{self._endereco}\nTelefone:{self._telefone}')