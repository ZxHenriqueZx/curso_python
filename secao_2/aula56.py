arquivo = 'teste.txt'

#with open(arquivo, 'a') as arquivo:
#    arquivo.write('Linha_1\n')
#    arquivo.write('Linha_2\n')

with open(arquivo, 'w', encoding='utf8') as arquivo:
    arquivo.write('Atenção')
