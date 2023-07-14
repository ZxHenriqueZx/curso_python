import random

cpf = ''

for i in range(9):
    cpf += str(random.randint(0, 9))

numeros_1 = cpf[:9]
contador_1 = 10
contador_2 = 11
soma_1 = 0 
soma_2 = 0

for num_1 in numeros_1:
    num_1 = int(num_1)
    soma_1 += num_1 * contador_1
    contador_1 -= 1

primeiro_digito = (soma_1 * 10) % 11
numeros_2 = numeros_1 + str(primeiro_digito)

for num_2 in numeros_2:
    num_2 = int(num_2)
    soma_2 += num_2 * contador_2
    contador_2 -= 1


segundo_digito = (soma_2 * 10) % 11

primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

print(f'{cpf}{primeiro_digito}{segundo_digito}')