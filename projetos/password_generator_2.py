import random 
import string

def gerador_senha(tamanho_senha):
    ascii_opcoes = string.ascii_letters
    digitos_opcoes = string.digits
    pontos_opcoes = string.punctuation
    opcoes = ascii_opcoes + digitos_opcoes + pontos_opcoes
    
    tamanho_senha = input('Tamanho da Senha(numero de caracteres): ')
    if tamanho_senha.isdigit():
        tamanho_senha = int(tamanho_senha)
    else:
        print('Escreva um numero inteiro')
        exit()

    senha_random = ''
    for i in range(0,tamanho_senha):
        indice_random = random.choice(opcoes)
        senha_random += indice_random 
    
    return f'Senha: {senha_random}'


senha_1 = gerador_senha()
senha_2 = gerador_senha()

print(senha_1)
print(senha_2)
      
