import abc

class Pessoa(abc.ABC):

    def __init__(self, nome, sobreNome):
        self._nome = nome
        self._sobreNome = sobreNome
    

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

    def __repr__(self) -> str:
       return f'Nome: {self._nome}\nSobre Nome: {self._sobreNome}'