# Context Manager com função - Criando e Usando gerenciadores de contexto
from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('Abrindo...')
        arquivo = open(caminho_arquivo, modo)
        yield arquivo
    except Exception as erro:
        print('Ocorreu este erro:', erro)
    finally:
        print('Fechando...')
        arquivo.close()

with my_open('aula029.txt', 'w') as arquivo:
    arquivo.write('Linha1\n')
    arquivo.write('Linha2\n')
    arquivo.write('Linha3\n')
    arquivo.write('oi', 123)
