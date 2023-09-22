# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário

from pathlib import Path
import csv

caminho_csv = Path(__file__).parent / 'aula016.csv'

with open(caminho_csv, 'r') as file:
    leitor = csv.reader(file)

    for linha in leitor:
        print(linha[0])

with open(caminho_csv, 'r') as file:
    leitor = csv.DictReader(file)

    for linha in leitor:
        print(linha['Idade'])
