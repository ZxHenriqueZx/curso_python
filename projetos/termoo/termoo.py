import json
import random 

dd = open("datas_dicas.json", encoding="utf8")
datas_dicas = json.load(dd)

datas_random = random.choice(list(datas_dicas.keys()))
#print(datas_dicas[datas_random])

def exibir(data):
    data_escolhida = datas_dicas[data]
    print(30*'-')
    print(f'Qual é a data desse acontecimento?\n{data_escolhida}')
    print(30*'-')
    
print('--JOGO DE ADIVINHACÃO DE DATAS--')
exibir(datas_random)

user_data = input('Data(DD/MM/AAAA): ')

