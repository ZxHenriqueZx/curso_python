import json
import random 

dd = open("datas_dicas.json", encoding="utf8")
datas_dicas = json.load(dd)

datas_random = random.choice(list(datas_dicas.keys()))

def exibir(data):
    data_escolhida = datas_dicas[data]
    print(30*'-')
    print(f'Qual é a data desse acontecimento?\n{data_escolhida}')
    print(30*'-')
    
print('--JOGO DE ADIVINHACÃO DE DATAS--')
exibir(datas_random)

qtd_tentativas = 5
win = False

while qtd_tentativas > 0 and win is not True: 
    user_data = input('Data(DD/MM/AAAA): ')
    data_certa = ''
    if user_data.isdigit() and len(user_data) == 8:
        for num in range(8):
            if user_data[num] == datas_random[num]:
                data_certa += user_data[num]
            else:
                data_certa += 'x'

        if data_certa == datas_random:
            win = True
    else:
        print('Escreva um valor válido (DDMMAAAA), somente 8 numeros!!')
        continue
    
    print(f'Resposta--------> {data_certa}')
    qtd_tentativas -= 1
    if qtd_tentativas == 0:
        print('VOCÊ UTRAPASSOU O NUMERO DE TENTATIVAS')

if win == True:
    print('PARABÉNS VOCÊ ACERTOU A DATA CORRETA!!!')
else:
    print('INFELIZMENTE NÃO FOI DESTA VEZ!!!')

