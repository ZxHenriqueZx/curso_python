"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
lista_c = [x + y for x, y in zip(lista_a, lista_b)]

def sum_list(l1, l2):
    diff = min(len(l1), len(l2))
    new_list = [(l2[l] + l1[l]) for l in range(diff)]
    return new_list 

soma_a_b = sum_list(lista_a, lista_b)
print(soma_a_b)
print(lista_c)
