

from Doador import Doador
from Receptor import Receptor
from Livros import Livro



import random



dict_Doador = {}
dict_Receptor ={}
dict_Livros  = {}



def inserir_doador():
    id = random.randint(000,999)
    nome = input('Nome: ') 
    sobreNome = input('Sobrenome: ')
    email = input('Email: ')
    tel = input('Telefone: ')
    senha = input('Crie uma senha: ')

    opc =  int(input('Deseja cadastrar um livro? 1 - sim | 2 - nçao '))
    if opc == 1:
        while True:
            cod = random.randint(000,999)
            autor = input('Autor: ')
            titulo = input('Titulo: ')
            quantidadePG = int(input('Quantiade de Paginas: '))
            livro = Livro(cod, autor,titulo,quantidadePG)
            doador = Doador(id, nome, sobreNome,email, tel,senha,livro)
            dict_Doador[id] = doador
            dict_Livros[id] = livro
            newOPC = int(input('Deseja adicionar mais um livro? 1 - sim | 2 - não'))
            if newOPC == 1:
                continue
            if newOPC == 2:
                break
    if opc == 2:
        doador = Doador(id, nome, sobreNome,email, tel,senha)
        dict_Doador[id] = doador
    
    return True, 'Doador cadastrado com sucesso!'


def inserir_receptor():
    id = random.randint(000,999)
    nome = input('Nome: ') 
    sobreNome = input('Sobrenome: ')
    email = input('Email: ')
    tel = input('Telefone: ')
    senha = input('Crie uma senha: ')
    
    receptor = Receptor(id,nome, sobreNome,email,tel,senha, Livro = '')
    dict_Receptor[id] = receptor

    return True, 'Receptor cadastrado com sucesso!'


def doar_um_livro():

    listar_doadores()
    listar_receptores()


    idDoador = int(input('Informe o id do doador: '))
    idReceptor = int(input('Informe o id do receptor: '))
    idLivro = int(input('Informe o ID do livro a ser doado: '))

    if idDoador in dict_Doador:
        dict_Doador[idDoador].doar_livro(dict_Receptor[idReceptor], dict_Livros[idLivro])
        return True ,'Doação realizada com sucesso'
    else:
        return False,'Doador não encotrado'



def listar_doadores():
    for i in dict_Doador.values():
        i.get_dados()

def listar_receptores():
    for i in dict_Receptor.values():
        i.get_dados()


def listar_livros():
    for i in dict_Livros.values():
        i.dados_do_livro()
  


while True:
    print('1 - Inserir um doardor\n'
          '2 - Inserir um Recptor\n'
          '3 - Listar doadores\n'
          '4 - Listar receptores\n'
          '5 - Listar Livro\n'
          '6 - Doar um livro\n'
          '0 - Sair\n' )
    opc = int(input('informa a opção desejada:'))
    if opc == 1:
        inserir_doador()
    if opc == 2:
        inserir_receptor()
    if opc == 3:
        listar_doadores()
    if opc == 4:
        listar_receptores()
    if opc == 5:
        listar_livros()
    if opc == 6:
        doar_um_livro()
    if opc == 0:
        break



