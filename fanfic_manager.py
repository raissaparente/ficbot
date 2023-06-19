import time
from time import sleep

from livros_comparacao import livros

class Fanfic:
    def __init__(self):
        """casatro obrigatorio basico"""
        self.titulo = input('TITULO: ')
        self.autor = input('AUTOR(A): ')
        self.wordcount = float(input('CONTAGEM DE PALAVRAS: '))
        self.paginas = self.wordcount / 310

    def cadastro_adicional(self):
        """realiza cadastro avancado opcional"""
        self.site = input('SITE: ')
        self.fandom = input('FANDOM: ')
        self.genero = input('GENERO: ')
        self.ship = input('SHIP: ')

    def consulta(self, item):
        match item:
            case 1:
                return 'titulo', self.titulo
            case 2:
                return 'autor', self.autor
            case 3:
                return 'contagem de palavras', self.wordcount
            case 4:
                return 'site', self.site
            case 5:
                return 'fandom', self.fandom
            case 6:
                return 'gênero', self.genero
            case 7:
                return 'ship', self.ship

    def compare_livro(self):
        """compara tamanho de fanfic com livros publicados usando os dicionarios em livros_comparacao"""
        for item in livros:
            if item['wc_maximo'] > self.wordcount > item['wc_minimo']:
                return item['titulo'], item['autor']

def delay():
    "atrasa o terminal"
    time.sleep(0.5)