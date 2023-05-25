while True:
    try:
        nota_1 = float(input('Escreva sua nota do 1°Bimestre: '))
        nota_2 = float(input('Escreva sua nota do 2°Bimestre: '))
        nota_3 = float(input('Escreva sua nota do 3°Bimestre: '))
        nota_4 = float(input('Escreva sua nota do 4°Bimestre: '))
        soma = nota_1 + nota_2 + nota_3 + nota_4

        print(f'A média das suas notas é de: {soma / 4:.2f}')
        break
    except:
        print('A nota esta inválida!!')
        print(30 * '-')
        continue
    