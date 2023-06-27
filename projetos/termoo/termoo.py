import json
import random 

dd = open("datas_dicas.json", encoding="utf8")
datas_dicas = json.load(dd)

datas_random = random.choice(list(datas_dicas.keys()))
#print(datas_dicas[datas_random])

print('--JOGO DE ADIVINHACÃO DE DATAS--')
 
user_data = input('Data(DD/MM/AAAA): ')
