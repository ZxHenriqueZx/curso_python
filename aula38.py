QTD_LINHA = 5 
QTD_COLUNA = 5

linha = 1
while linha <= QTD_LINHA:
    coluna = 1

    while coluna <= QTD_COLUNA:
        print(f'{linha=} {coluna=}')
        coluna += 1
    
    linha += 1

print('Acabou')