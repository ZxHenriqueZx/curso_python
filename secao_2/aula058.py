import json

pessoa = {
    'nome': 'Luis',
    'sobrenome': 'Henrique',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

#with open('aula58.json', 'w') as arquivo:
#    json.dump(pessoa, arquivo, indent=2)

with open('aula58.json', 'r') as arquivo:
    pessoa_2 = json.load(arquivo)

print(pessoa_2)
