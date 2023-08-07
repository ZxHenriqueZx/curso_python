import json
from ex001_a import Pessoa

with open('ex001.json', 'r') as arquivo:
    dados = json.load(arquivo)

p2 = Pessoa(**dados)

