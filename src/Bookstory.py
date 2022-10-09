
from Doador import Doador
from Receptor import Receptor
from Livros import Livro

doador =Doador(0,'','','','','','','','','')
receptor =Receptor(0,'','','','','','','','','')
livro = Livro(0,'','','','','','','')
class Bookstory:

    def __init__(self):
        self._dict_Doador = {}
        self._dict_Receptor ={}
        self._dict_Livros  = {}
        self._Relatorio = []
    
    def entrar_no_sistema():
        pass
    def cadastrar_Doador(self,id, nome, sobreNome,nomeRua, numeroDaRua, cep, bairro, email, tel,senha):
        doador.id = id
        doador.nome = nome
        doador.sobreNome = sobreNome
        doador.nomeRua = nomeRua
        doador.numeroDarua = numeroDaRua
        doador.cep = cep
        doador.bairro = bairro
        doador.email = email
        doador.telefone = tel
        doador.senha = senha

        if id not in self._dict_Doador.keys():
            self._dict_Doador[id] = doador
            return True ,'Doador cadastrado com sucesso!'
        else:
            return False, 'Doador ja cadastrado!'


    def cadastrar_Receptor(self,id, nome, sobreNome,nomeRua, numeroDaRua, cep, bairro, email, tel,senha):
        receptor.id = id
        receptor.nome = nome
        receptor.sobreNome = sobreNome
        receptor.nomeRua = nomeRua
        receptor.numeroDarua = numeroDaRua
        receptor.cep = cep
        receptor.bairro = bairro
        receptor.email = email
        receptor.telefone = tel
        receptor.senha = senha

        if id not in self._dict_Receptor.keys():
            self._dict_Receptor[id] = receptor
            return True, 'Receptor cadastrado com sucesso!'
        else:
            return False, 'Receptor ja cadastrado!'
    
    def cadastrar_livro(self,idlivro,autor,titulo,quantidade, dataLancamento, tempoDeUso,versao, volume):
        livro.idlivro = idlivro
        livro.autor = autor
        livro.titulo = titulo
        livro.quantidade = quantidade
        livro.data = dataLancamento
        livro.tempoDeUso = tempoDeUso
        livro.versao = versao
        livro._volume = volume

        if idlivro not in self._dict_Livros.keys():
            self._dict_Livros[id] = livro
            return True, 'Livro cadastrado com sucesso!'
        else:
            return False, 'Livro ja cadastrado!'
    
    def buscar_livro(self, id):
        if id in self._dict_Livros.keys():
            for i in self._dict_Livros.values():
                i.dados_do_livro()
    
    def mostrar_livros(self):
        for i in self._dict_Livros.values():
            i.dados_do_livro()