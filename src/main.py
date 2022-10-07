from Pessoa import Pessoa
from Doador import Doador
from Receptor import Receptor
from Livros import Livro

dict_Doardor = {}
dict_Receptor = {}
dict_Livros = {}
dict_Relatorio = {}



p = Pessoa('Vinicius', 'Nunes')
d = Doador('Vinicus','Nunes','asdasdas@gmail.com','rua tal','1234567','00009283')
c = Receptor('Jose','de morais', 'asdasdasd@gmail.com',' rua tal','1234-5677','123456')

l = Livro('George.R.R Martin','Game Of Thrones',2,'12/02/2019','2 anos','4','6')


d.get_dados_doador()


c.get_dados_receptor()

l.dados_dos_livros()