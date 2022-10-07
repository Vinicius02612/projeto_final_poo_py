""" 
O usuário deve cadastrar os livros a serem doados informando informações como: O livro
do Livro, quantidade de paginas, data de lançamento e tempo de uso, versão do livro,
volumes;
 """

class Livro:

    def __init__(self, autor,titulo,quantidade, dataLancamento, tempoDeUso,versao, volume):
        self._autor = autor
        self._titulo = titulo
        self._quantidade = quantidade
        self._data = dataLancamento
        self._tempoDeUso = tempoDeUso
        self._versao = versao
        self._volume = volume
    

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
    

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, dta):
        self._data = dta
        return self._data
    


    @property
    def tempoDeUso(self):
        return self._tempoDeUso
    
    @tempoDeUso.setter
    def tempoDeUso(self, tmp):
        self._tempoDeUso = tmp
        return self._tempoDeUso
    

    @property
    def versao(self):
        return self._versao
    
    @versao.setter
    def versao(self, vrs):
        self._versao = vrs
        return self._versao
    

    def dados_dos_livros(self):
        print(f'\nAutor: {self._autor}\nTitulo: {self._titulo}\nQuantidade: {self._quantidade}\nData de lançamento: {self._data}\nTempo de Uso: {self._tempoDeUso}\nVersão:{self._versao}\nVolume: {self._volume} ')