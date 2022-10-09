
from Doador import Doador
from Receptor import Receptor
from Livros import Livro

import random

from Bookstory import Bookstory



book = Bookstory()


def inserir_doador():
    id = random.randint(000,999)
    nome = input('Nome: ') 
    sobreNome = input('Sobrenome: ')
    nomeRua = input('Rua: ')
    numeroDaRua = input('numero da rua: ')
    cep = input('Cep: ') 
    bairro = input('Bairro: ')
    email = input('Email: ')
    tel = input('Telefone: ')
    senha = input('Crie uma senha: ')



    return book.cadastrar_Doador(id, nome, sobreNome,nomeRua, numeroDaRua, cep, bairro, email, tel,senha)

def inserir_receptor():
    id = random.randint(000,999)
    nome = input('Nome: ')
    sobreNome = input('Sobrenome: ')
    nomeRua = input('Rua: ')
    numeroDaRua = input('numero da rua: ')
    cep = input('Cep: ') 
    bairro = input('Bairro: ')
    email = input('Email: ')
    tel = input('Telefone: ')
    senha = input('Crie um senha: ')

    return book.cadastrar_Receptor(id, nome, sobreNome,nomeRua, numeroDaRua, cep, bairro, email, tel,senha)

def inserir_livro():
    idlivro = random.randint(000,999)
    autor = input('Autor: ')
    titulo = input('Titulo: ')
    quantidade = input('Quantidade de Paginas: ')
    data = input('data de lançamento: ')
    tempoDeUso = input('Tempo de uso: ')
    versao = input('Versão do Livro: ')
    volume = input('Volume: ')

    return book.cadastrar_livro(idlivro,autor,titulo,quantidade, data, tempoDeUso,versao, volume)


def procurar_livro():
    id = int(input('informe o ID livro: '))

    return book.buscar_livro(id)


while True:
    print('1 - Inserir um doardor\n'
          '2 - Inserir um Recptor\n'
          '3 - Inserir um Livro\n'
          '4 - Procurar um livro\n'
          '0 - Sair\n' )
    opc = int(input('informa a opção desejada:'))
    if opc == 1:
        inserir_doador()
    if opc == 2:
        inserir_receptor()
    if opc == 3:
        inserir_livro()
    if opc == 4:
        procurar_livro()
    if opc == 0:
        break