"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# numero_int_input = input('Digite um numero inteiro: ')

# try:
#     numero_int_output = int(numero_int_input)
#     if (numero_int_output % 2) == 0:
#         print(f'O número {numero_int_output} é par!!')
#     else:
#         print(f'O numero {numero_int_output} é ímpar!!')
# except:
#     print('Este não é um numero inteiro!!')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# hora_digitada = input('Digite a hora em numero inteiro: ')

# try:
#     hora_digitada_int = int(hora_digitada)
#     if hora_digitada_int >= 0 and hora_digitada_int<= 11:
#         print('Bom dia!!')
#     elif hora_digitada_int >= 12 and hora_digitada_int <= 17:
#         print('Boa tarde!!')
#     elif hora_digitada_int >= 18 and hora_digitada_int <= 23:
#         print('Boa noite!!')
#     else:
#         print('Horário invalido!')
# except:
#     print('Valor inválido!!')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

first_name = input('Digite seu primeiro nome: ')
letras_nome = len(first_name)

if letras_nome <= 4:
    print('Seu nome é curto!')
elif letras_nome >= 5 and letras_nome <=6:
    print('Seu nome é normal!')
elif letras_nome > 6:
    print('Seu nome é muito grande!')


