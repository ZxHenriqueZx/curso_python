"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

lista_a = ['Luis', 'Henrique']
lista_b = lista_a.copy()

lista_a[0] = 'Pedro'

print(lista_a)
print(lista_b)