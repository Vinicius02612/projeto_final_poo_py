from abc import ABC, abstractmethod

class Pessoa(ABC):

    def __init__(self, nome, sobreNome,nomeRua,numeroDarua, cep,bairro , email,telefone):
        self._nome = nome
        self._sobreNome = sobreNome
        self._nomeRua = nomeRua
        self._numeroRua = numeroDarua
        self._cep = cep
        self._bairro = bairro
        self._email = email
        self._telefone = telefone


    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, n):
        self._nome = n
        return self._nome


        
    @property
    def sobreNome(self):
        return self._sobreNome
    
    @sobreNome.setter
    def sobreNome(self, sn):
        self._sobreNome = sn
        return self._sobreNome
    
    @property
    def nomeRua(self):
        return self._nomeRua
    
    @nomeRua.setter
    def nomeRua(self, nr):
        self._nomeRua = nr
        return self._nomeRua
    
    @property
    def numeroDarua(self):
        return self._numeroRua
    
    @numeroDarua.setter
    def numeroRua(self, num_rua):
        self._numeroRua = num_rua
        return self._numeroRua

    @property
    def cep(self):
        return self._cep
    
    @cep.setter
    def cep(self, cep):
        self._cep = cep
        return self._cep

    @property
    def bairro(self):
        return self._bairro

    @bairro.setter
    def bairro(self, brr):
        self._bairro = brr
        return self._bairro


    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email



    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone
        return self._telefone

    @property
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self, snh):
        self._senha = snh
        return self._senha

    @abstractmethod
    def get_dados(self):
        print(f'Nome: {self._nome}\nSobre Nome: {self._sobreNome}')

    def __repr__(self) -> str:
       return f'{self._nome}\n{self._sobreNome}'