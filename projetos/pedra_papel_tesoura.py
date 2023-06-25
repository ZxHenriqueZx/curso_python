import random
import os

user_points = 0 
computer_points = 0 

while True:
    print(30*'-')
    user_choice = input('0)Pedra\n1)Papel\n2)Tesoura\n3)Quit\nEscolha: ')
    os.system('clear')
    if user_choice == '3':
        break
    print(30*'-')
    if user_choice.isdigit():
        user_choice = int(user_choice)
    else:
        print('Escreva um numero válido!!')
    
    computer_choice = random.randint(0,2)
    
    if user_choice == 0 and computer_choice == 2:
        print('PEDRA X TESOURA : VENCEU')
        user_points += 1
    elif user_choice == 0 and computer_choice == 1:
        print('PEDRA X PAPEL : PERDEU')
        computer_points += 1
    elif user_choice == 1 and computer_choice == 0:
        print('PAPEL X PEDRA : VENCEU')
        user_points += 1
    elif user_choice == 1 and computer_choice == 2:
        print('PAPEL X TESOURA : PERDEU')
        computer_points += 1
    elif user_choice == 2 and computer_choice == 1:
        print('TESOURA X PAPEL : VENCEU')
        user_points += 1
    elif user_choice == 2 and computer_choice == 0:
        print('TESOURA X PEDRA : PERDEU')
        computer_points += 1
    else:
        print('EMPATE')
    
print(f'Pontos:\nVocê = {user_points}\nComputador = {computer_points}')

