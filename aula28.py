# Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis
# Mutáveis [] {} set()
# Imutáveis () "" 0 0.0 None False range(0, 10)

lista = [0]
dicionario = {0:0}
conjunto = set()
tupla = ()
string = ""
inteiro = 0
flutuante = 0.0
nada = None 
falso = False
intervalo = range(0)

def falsy(valor):
    return 'falsy' if not valor else 'truthy'

print(lista, falsy(lista))
print(dicionario, falsy(dicionario))
print(conjunto, falsy(conjunto))
print(tupla, falsy(tupla))
print(string, falsy(string))
print(inteiro, falsy(inteiro))
print(flutuante, falsy(flutuante))
print(nada, falsy(nada))
print(falso, falsy(falso))
print(intervalo, falsy(intervalo))
