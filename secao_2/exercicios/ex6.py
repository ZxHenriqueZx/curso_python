while True:
    try:
        valor_hora = float(input('Valor da hora R$'))
        horas_trabalhadas = float(input('Horas trabalhadas: '))
        salario = valor_hora * horas_trabalhadas

        print(f'+ Salário Bruto: R${salario:.2f}\n'
              f'- IR (11%): R${salario * 0.11}\n'
              f'- INSS (8%): R${salario * 0.08}\n'
              f'- Sindicato (5%): R${salario * 0.05}\n'
              f'= Salário Liquido: R${salario - (salario * 0.24)}')
        break
    except:
        print('dados inválidos!!')
        continue
