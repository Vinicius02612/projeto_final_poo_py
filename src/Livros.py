""" 
O usuário deve cadastrar os livros a serem doados informando informações como: O livro
do Livro, quantidade de paginas, data de lançamento e tempo de uso, versão do livro,
volumes;
 """

class Livro:

    def __init__(self, idlivro,autor,titulo,quantidade):
        self._idlivro = idlivro
        self._autor = autor
        self._titulo = titulo
        self._quantidade = quantidade

    
    @property
    def idlivro(self):
        return self._idlivro

    @idlivro.setter
    def idlivro(self, lvr):
        self._idlivro = lvr
        return self._idlivro
    
    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, atr):
        self._autor = atr
        return self._autor
    
    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo
        return self._titulo
    
    @property
    def quantidade(self):
        return self._quantidade
    
    @quantidade.setter
    def quantidade(self, qntd):
        self._quantidade = qntd
        return self._quantidade


    def dados_do_livro(self):
        print(
            f'\nID: {self.idlivro}\n'
            f'Autor: {self._autor}\n'
            f'Titulo: {self._titulo}\n'
            f'Quantidade de paginas: {self._quantidade}\n'
        )

    def __str__(self):
        return f'\nID: {self.idlivro}\nAutor: {self._autor}\nTitulo: {self._titulo}\nQuantidade: {self._quantidade}\n'