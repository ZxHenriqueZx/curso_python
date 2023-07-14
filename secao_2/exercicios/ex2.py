while True:
    metro = input('Escreva um valor em metros: ')

    try:
        metro_float = float(metro)
        centimetro = metro_float * 100
        print(f'Esse valor {metro_float:.2f}m em centímetros é '
              f'{centimetro:.2f}cm')
        break
    except:
        print('Este não é um valor válido!!')
        continue