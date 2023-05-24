valor_1 = input('Digite o primeiro valor: ')
valor_2 = input('Digite o segundo valor: ')

valor_1_int = int(valor_1)
valor_2_int = int(valor_2)

if valor_1_int > valor_2_int:
    print(f'O primeiro valor {valor_1} é maior que o segundo valor {valor_2}')
elif valor_2_int > valor_1_int:
    print(f'O segundo valor {valor_2} é maior que o primeiro valor {valor_1}')
elif valor_1_int == valor_2_int:
    print('Os valores são iguais!')

