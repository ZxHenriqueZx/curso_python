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

list_global = []
list_history = []
options = ['refazer', 'desfazer', 'clear', 'sair']

def input_user():
    print('---Lista de Tarefas---')
    print(f'comandos: {options[0]}, {options[1]}, {options[2]}, {options[3]}')
    input_user = input('Escreva uma tarefa ou comando: ')
    return input_user

def list_manager(input_user):
    if input_user not in options:
        list_global.append(input_user)

while input_user != 'sair':
    print(30 * '-')
    list_manager(input_user())
    print(list_global)



