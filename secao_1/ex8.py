"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista_compras = []

while True:

    print('==LISTA DE COMPRA==')
    acao_lista = input('[a]dicionar [r]emover [l]istar [s]air: ').lower()

    if acao_lista == 's':
        break

    if acao_lista == 'a':
        adicionar_lista = input('adicionar: ')
        lista_compras.append(adicionar_lista)
        print(30*'-')
        os.system('clear')

    elif acao_lista == 'r':
        try:
            retirar_lista = int(input('remover[índice]: '))
            lista_compras.pop(retirar_lista)
            print(30*'-')
            os.system('clear')
        except:
            print('Índice inválido!!')
        
    elif acao_lista == 'l':
        lista_numerada = enumerate(lista_compras)
        print(30*'-')
        if len(lista_compras) == 0:
            print('Lista Vazia!')
        for indice, item in lista_numerada:
            print(indice,item)
        print(30*'-')
     
        
    else:
        print('Acão inválida!!')
