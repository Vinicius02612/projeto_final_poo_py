
from Doador import Doador
from Receptor import Receptor
from Livros import Livro

class Bookstory:

    def __init__(self):
        self._dict_Doador = {}
        self._dict_Receptor ={}
        self._dict_Livros  = {}
        self._Relatorio = []
    
    def entrar_no_sistema():
        pass
    def cadastrar_Doador(self,id, nome, sobreNome, email, tel,senha):
        doador = Doador(id, nome, sobreNome, email, tel,senha)

        if id not in self._dict_Doador.keys():
            self._dict_Doador[id] = doador
            return True ,'Doador cadastrado com sucesso!'
        else:
            return False, 'Doador ja cadastrado!'


    def cadastrar_Receptor(self,id, nome, sobreNome, email, tel,senha):
        receptor = Receptor(id, nome, sobreNome, email, tel,senha)

        if id not in self._dict_Receptor.keys():
            self._dict_Receptor[id] = receptor
            return True, 'Receptor cadastrado com sucesso!'
        else:
            return False, 'Receptor ja cadastrado!'
    
    def cadastrar_livro(self,idlivro,autor,titulo,quantidadePg):
        livro = Livro(idlivro,autor,titulo,quantidadePg)
        self._dict_Livros[id] = livro


    def doar_livro(self, doador, livro, receptor):


        pass

    def listar_doardor(self):
        for i in self._dict_Doador.values():
            i.get_dados()

    def listar_receptor(self):
        for i in self._dict_Receptor.values():
            i.get_dados()

    def buscar_livro(self, id):
            for id ,i in self._dict_Livros.items():
                print(f'{id} : {i}')

            
    
    def mostrar_livros(self):
        for i in self._dict_Livros.values():
            i.dados_do_livro()
    


    def __str__(self) -> str:
        return f'{self._dict_Doador}\n {self._dict_Receptor}\, {self._dict_Livros}\n'