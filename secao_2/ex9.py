# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import os
import json

list_global = []
list_history = []
sair = False
options = ['refazer', 'desfazer', 'clear', 'sair']

def input_user():
    global sair
    input_user = input('Escreva uma tarefa ou comando: ')
    if input_user == 'sair':
        sair = True
    return input_user

def list_manager(input_user):
    if input_user not in options:
        list_global.append(input_user)
    elif input_user == 'desfazer':
        if list_global == []:
            print('Nada para desfazer')
            return
        list_history.append(list_global.pop())
    elif input_user == 'refazer':
        if list_history == []:
            print('Nada para refazer')
            return
        list_global.append(list_history.pop(0))
    elif input_user == 'clear':
        os.system('clear')

while sair == False:
        print(30 * '-')
    print('---Lista de Tarefas---')
    print(f'comandos: {options[0]}, {options[1]}, {options[2]}, {options[3]}')
    list_manager(input_user())
    print(30*'-')
    print(f'Lista:', *list_global, sep='\n')

with open('ex9.json', 'w') as arquivo:
    json.dump(list_global, arquivo, indent=2)


