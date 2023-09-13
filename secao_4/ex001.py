# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

total_deve = 1000000
parcela = round(total_deve / 60, 2)
months = relativedelta(months=0)

fmt = '%d/%m/%Y'
date_start = datetime(2020, 12, 20)
delta = relativedelta(months=60)
date_end = date_start + delta

for i in range(1, 61):
    data = datetime.strftime(date_start + months, fmt)
    print(f'{i}x - {data} - Parcela: R${parcela:,}')
    months += relativedelta(months=1)

