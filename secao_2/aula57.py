import os

arquivos = 'teste.txt'

with open(arquivos, 'w+', encoding='utf8') as arquivo:
    arquivo.write('Criado\n')
 
#os.rename(arquivos, 'teste1.txt')
os.remove(arquivos)
#os.unlink(arquivos)
