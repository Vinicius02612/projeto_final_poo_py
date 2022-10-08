from Pessoa import Pessoa

class Receptor(Pessoa):

    def __init__(self,id, nome, sobreNome, nomeRua,numeroDarua, cep,bairro , email,telefone):
        super().__init__(nome, sobreNome, nomeRua,numeroDarua, cep,bairro , email,telefone)
        self._id = id
    
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
    def nomeRua(self):
        return super()._nomeRua
    
    @nomeRua.setter
    def nomeRua(self, nr):
        super()._nomeRua = nr
        return self._nomeRua
    


    @property
    def numeroDarua(self):
        return super()._numeroRua
    
    @numeroDarua.setter
    def numeroRua(self, num_rua):
        super()._numeroRua = num_rua
        return self._numeroRua


    @property
    def cep(self):
        return super()._cep
    
    @cep.setter
    def cep(self, cep):
        super()._cep = cep
        return self._cep


    @property
    def bairro(self):
        return super()._bairro

    @bairro.setter
    def bairro(self, brr):
        super()._bairro = brr
        return super()._bairro



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
    def senha(self):
        return super()._senha
    
    @senha.setter
    def senha(self, snh):
        super()._senha = snh
        return super()._senha
    

    def get_dados_receptor(self):
        print('Dados do Doador:\n')
        print(
            f'ID: {self._id}\n'
            f'Nome: {self._nome}\n'
            f'Sobre Nome: {self._sobreNome}\n'
            f'Nome da Rua: {self._nomeRua}\n'
            f'Numero da Rua:{self._numeroRua}\n'
            f'Cep:{self._cep}\n'
            f'Bairro:{self._bairro}\n'
            f'email:{self._email}\n'
            f'Telefone:{self._telefone}\n'
        )
    