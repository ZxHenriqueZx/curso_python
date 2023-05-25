try:
    num_inteiro_um = int(input('Digite um numero inteiro: '))
    num_inteiro_dois = int(input('Digite o segundo numero inteiro: '))
    num_real = float(input('Digite um numero real: '))

    num_1 = (num_inteiro_um * 2) + (num_inteiro_dois / 2)
    num_2 = (num_inteiro_um * 3) + num_real
    num_3 = num_real ** 3

    print('o produto do dobro do primeiro com'
          f'metade do segundo é {num_1}')
    print(f'a soma do triplo do primeiro com o terceiro é {num_2}')
    print(f'o terceiro elevado ao cubo é {num_3}')

except:
    print('Os valores não são válidos!!')
