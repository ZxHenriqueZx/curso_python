from functions import *

print(50*'-')
print('QUAL É A DATA DE VENCIMENTO?')
print(50*'-')

data_user = input('')
if len(data_user) == 10:
    print(verificacao_val(data_user))
else:
    print('Escreva um valor válido:(dd-mm-aaaa)')
