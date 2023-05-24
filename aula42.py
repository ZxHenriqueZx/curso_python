frase = 'O Python é uma linguagem de programação' \
    'multiparadigima.' \
    'Python foi criado por Guido van Rossum.'


i = 0 
letra_que_apareceu_mais = ''
qtd_letra_mais_apareceu = 0
while i < len(frase):
    letra_atual = frase[i]
    cont_atual_letras = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue

    if qtd_letra_mais_apareceu < cont_atual_letras:
        qtd_letra_mais_apareceu = cont_atual_letras
        letra_que_apareceu_mais = letra_atual
    
    i += 1

print(f'A letra que mais apareceu foi "{letra_que_apareceu_mais}"\n'
      f'Ela apareceu {qtd_letra_mais_apareceu}x')