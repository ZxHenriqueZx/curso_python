from convert_currency import ConvertCurrency

api_key = '75a93ef9071673d199a9'
conv_curr = ConvertCurrency(api_key)

print('===CONVERSOR DE MOEDAS====')
while True:
    print(30*'-')
    option_user = input('Ver moedas disponíveis(1)\nConverter moedas(2)\nSair(3)\n:')
    print(30*'-')
    if option_user.isdigit() is not True:
        print('Escreva umas das opções!!')
        continue
    else:
        option_user = int(option_user)
    if option_user == 3:
        break
    if option_user not in range(1,3):
        print('Escreva uma das opções disponíveis!!')
        continue
    
    def converter(moeda_um, moeda_dois, amount=1):
        print(conv_curr.transform_currency(moeda_um, amount, moeda_dois))

    if option_user == 1:
        conv_curr.show()
    
    if option_user == 2:
        moe_ini = input('Escreva a primeira moeda(ex:USD): ')
        moe_fin = input('Escreva a segunda moeda(ex:BRL): ')
        valor = float(input('Escreva o valor a ser convertido: '))
        converter(moe_ini, moe_fin, valor)
        

#print(conv_curr.transform_currency('USD', 50, 'BRL'))
