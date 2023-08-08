# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

# def duplicar(num):
#     return num * 2 

# def triplicar(num):
#     return num * 3

# def quadruplicar(num):
#     return num * 4

# print(quadruplicar(10))
# num1 = triplicar(8)
# num2 = duplicar(22)
# print(num1)
# print(num2)

# def multiplicar(numero):
#     vezes_2 = numero * 2
#     vezes_3 = numero * 3
#     vezes_4 = numero * 4
#     print(f'dobro de {numero} é {vezes_2}\n'
#           f'triplo de {numero} é {vezes_3}\n'
#           f'quadruplo de {numero} é {vezes_4}')

# multiplicar(5)

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador

    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)

print(triplicar(10))
print(duplicar(10)) 
