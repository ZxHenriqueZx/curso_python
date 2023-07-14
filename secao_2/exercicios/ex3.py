while True:
    preco_hora = input('Valor da hora R$')
    horas_trabalhadas = input('Quantas horas trabalhadas: ')

    try:
        salario = float(preco_hora) * float(horas_trabalhadas)
        print(f'O seu salário deste mês é de R${salario:.2f}')
        break
    except:
        print('Os valores estão inválidos!')
        continue