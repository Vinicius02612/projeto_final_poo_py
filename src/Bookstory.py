
from Doador import Doador
from Receptor import Receptor
from Livros import Livro


class Bookstory:

    def __init__(self):
        self._dict_Doador = {}
        self._dict_Receptor ={}
        self._dict_Livros  = {}
        self._Relatorio = []
    

    def cadastrar_Doador(self,id, nome, sobreNome,nomeRua, numeroDaRua, cep, bairro, email, tel):
        doador = Doador(id, nome, sobreNome,nomeRua, numeroDaRua, cep, bairro, email, tel)
        if id not in self._dict_Doador.keys():
            self._dict_Doador[id] = doador
            return True ,'Doador cadastrado com sucesso!'
        else:
            return False, 'Doador ja cadastrado!'


    def cadastrar_Receptor(self,id, nome, sobreNome,nomeRua, numeroDaRua, cep, bairro, email, tel):
        receptor = Receptor(id, nome, sobreNome,nomeRua, numeroDaRua, cep, bairro, email, tel)
        if id not in self._dict_Receptor.keys():
            self._dict_Receptor[id] = receptor
            return True, 'Receptor cadastrado com sucesso!'
        else:
            return False, 'Receptor ja cadastrado!'
    
    def cadastrar_livro(self,idlivro,autor,titulo,quantidade, dataLancamento, tempoDeUso,versao, volume):
        livro = Livro(idlivro,autor,titulo,quantidade, dataLancamento, tempoDeUso,versao, volume)

        if idlivro not in self._dict_Livros.keys():
            self._dict_Livros[id] = livro
            return True, 'Livro cadastrado com sucesso!'
        else:
            return False, 'Livro ja cadastrado!'
    
    def buscar_livro(self):
        pass