arquivo = "teste.txt"

with open(arquivo, 'w+') as arquivo:
    arquivo.write('Linha_1\n')
    arquivo.write('Linha_2\n')
    arquivo.writelines(('Linha_3\n', 'Linha_4'))

    arquivo.seek(0, 0)
    print(arquivo.read())
    
    arquivo.seek(0, 0)
    print(arquivo.readline())
    arquivo.seek(0, 0)
    print(arquivo.readlines())
