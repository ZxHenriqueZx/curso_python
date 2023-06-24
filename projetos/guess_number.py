import random 

numero_teto = input('Escolha o numero teto para o desafio: ')

if numero_teto.isdigit():
    numero_teto = int(numero_teto)
else:
    print('Escreva um numero inteiro!!!')
    exit()

numero_random = random.randint(0, numero_teto)    

qtd_tentativas = 0
while True:
    numero_usuario = input('Tente Adivinhar: ')
    qtd_tentativas += 1
    if numero_usuario.isdigit():
        numero_usuario = int(numero_usuario)
    else:
        print('Escreva um numero inteiro!!!')
        continue

    if numero_usuario == numero_random:
        print(f'Parabéns você acertou o numero secreto {numero_random}!!!\n'
              f'{qtd_tentativas} tentativas')
        break
    elif numero_usuario > numero_random:
        print('Chute um numero mais baixo!!!')
        print(30*'-')
    elif numero_usuario < numero_random:
        print('Chute um numero mais alto!!!')
        print(30*'-')
    else:
        print(30*'-')
        print('Tente novamente!!')
        print(30*'-')
