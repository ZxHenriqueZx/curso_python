QUILO_PEIXE_KG = 50
MULTA_PEIXE = 4

while True:
    try:
        quilo_peixe = float(input('Escreva valor em kg: '))
    except:
        print('Os dado estão inválidos!!')
        continue

    if quilo_peixe > QUILO_PEIXE_KG:
        excedente = quilo_peixe - QUILO_PEIXE_KG
        multa = excedente * MULTA_PEIXE
        print(f'Você pescou {quilo_peixe}kg de peixe\nteve um excedente de '
              f'{excedente}kg\ne ira pagar uma multa de R${multa} reais')
        break
    else:
        print('Sua pescada esta dentro do limite!')
        break
