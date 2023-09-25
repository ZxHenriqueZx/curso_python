# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template.
import locale
import string
from datetime import datetime

locale.setlocale(locale.LC_ALL, '')

def converte_brl(numero):
    brl = 'R$ ' + locale.currency(numero, symbol=False, grouping=True)
    return brl

data = datetime(2023, 9, 28)
dados = {
    'nome': 'Luis',
    'valor': converte_brl(1_589_563),
    'data': data.strftime('%d/%m/%Y'),
    'empresa': 'L. H.',
    'telefone': '+55 (11)96307-4872'
        }


with open('aula021.txt', 'r') as file:
    texto = file.read()
    template = string.Template(texto)
    print(template.substitute(dados))
