import random 
import string

def gerador_senha(tamanho_senha = 8):
    ascii_opcoes = string.ascii_letters
    digitos_opcoes = string.digits
    pontos_opcoes = string.punctuation
    opcoes = ascii_opcoes + digitos_opcoes + pontos_opcoes
    senha_random = ''

    tamanho_senha = input('Qual sera o tamanho da senha(escreva um numero int): ')
    if tamanho_senha.isdigit():
        tamanho_senha = int(tamanho_senha)
    else:
        print('Não é valido')
        exit()

    while tamanho_senha > 0:
        indice_random = random.randint(0,len(opcoes) - 1)
        senha_random += opcoes[indice_random]
        tamanho_senha -= 1
    
    return f'SENHA: {senha_random}'
    
senha_1 = gerador_senha()
senha_2 = gerador_senha()

print(senha_1)
print(senha_2)
