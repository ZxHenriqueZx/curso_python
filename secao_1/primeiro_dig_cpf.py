"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

#MINHA SOLUÇÃO

# CPF = '238.656.668-41'
# digitos, *resto = CPF.split('-')

# digitos = digitos.split('.')

# num_1, num_2, num_3 = digitos
# novo_digitos = num_1 + num_2 + num_3


# soma = 0
# i = iter(range(10,2,-1)) 


# for num in novo_digitos:
#     num = int(num)
#     try:
#         multiplicador = next(i)
#     except StopIteration:
#         break
#     soma += num * multiplicador
    

# mult_por_dez = soma * 10 
# primeiro_digito_cpf = mult_por_dez % 11

# if primeiro_digito_cpf > 9:
#     primeiro_digito_cpf = 0
# else:
#     primeiro_digito_cpf = primeiro_digito_cpf

# print(primeiro_digito_cpf)



cpf = '238656668'.replace('.', '')\
    .replace('-', '')\
    .replace(' ', '')

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

print(primeiro_digito, segundo_digito)