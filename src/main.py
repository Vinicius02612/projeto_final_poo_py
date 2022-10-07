
from Doador import Doador
from Receptor import Receptor
from Livros import Livro


import random

dict_Doardor = {}
dict_Receptor = {}
dict_Livros = {}
dict_Relatorio = {}

#criar conta do usuário, aqui o usuário pode se cadastrar com doardor como receptor
# o usuário deve ter um ID de intentificação 


#nome, sobreNome, endereco, email,telefone, senha
def criarConta():
    print('Voce escolheu criar uma conta')
    id = random.randint(000, 999)
    nome =  input('Informe seu nome: ')
    sobreNome = input('Seu sobrenome: ')
    
    


#cadastrar livros
def cadastrarLivros():
    pass

#listar livros cadastrados
def listarLivros():
    pass


def doarLivros(receptor, livro):
    pass


d = Doador('Vinicus','Nunes','asdasdas@gmail.com','rua tal','1234567','00009283')
c = Receptor('Jose','de morais', 'asdasdasd@gmail.com',' rua tal','1234-5677','123456')

l = Livro('George.R.R Martin','Game Of Thrones',2,'12/02/2019','2 anos','4','6')

""" p.get_pessoa() """

d.get_dados_doador()


""" c.get_dados_receptor()

l.dados_dos_livros() """