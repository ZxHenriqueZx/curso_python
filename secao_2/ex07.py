# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
from itertools import zip_longest
 
city = ['Salvador', 'Ubatuba', 'Belo Horizonte']
ids = ['BA', 'SP', 'MG', 'RJ']

#MINHA SOLUÇÃO
def join_list(list_1, list_2):
    new_list = []
    for i ,l in enumerate(list_1):
        new_list += tuple( [(l, ids[i])] ) 
         
    print(new_list)

join_one = join_list(city, ids)

def join_list_2(list_1, list_2):
    intervalo = min(len(city), len(ids))
    return [(list_1[l], list_2[l]) for l in range(intervalo)]

join_two = join_list_2(city,ids)

print(join_two)

print(list(zip(city, ids)))
print(list(zip_longest(city, ids)))
