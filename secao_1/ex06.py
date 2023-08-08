"""
Iterando strings com while
"""

nome = input('Escreva seu nome: ')
letras_nome = len(nome)

capt_letra = 0
novo_nome = ''
while capt_letra < letras_nome:
    letra = nome[capt_letra]
    novo_nome += '*' +letra 
    capt_letra +=1

novo_nome += '*'

print(novo_nome)
    
