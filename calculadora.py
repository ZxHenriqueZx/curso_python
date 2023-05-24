while True:
    num_1 = input('Escreva um numero: ')
    operador = input('Escreva o operador (+,-,*,/,): ')
    num_2 = input('Escreva outro numero: ')

    numeros_validos = True
    operador_valido = True
    operador_perm = '+-*/'

    try:
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        
        if operador == '+':
            result = num_1_float + num_2_float
        elif operador == '-':
            result = num_1_float - num_2_float
        elif operador == '/':
            result = num_1_float / num_2_float
        elif operador == '*':
            result = num_1_float * num_2_float

    except:
        numeros_validos = None
    
    if operador not in operador_perm:
        print('O operador esta inválido!!')
        operador_valido = False
        print(25 * '-')
        continue
        
    if numeros_validos is None:
        print('Um dos numeros ou ambos estão inválidos!!')
        print(25 * '-')
        continue

    if numeros_validos and operador_valido:
        print(f'{num_1} {operador} {num_2} = {result:.2f}')

    print(25 * '-')

    sair = input('Quer sair? S/N ').upper()
    if sair == 'S':
        break
    else:
        print(25 * '-')
        continue
