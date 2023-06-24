import random 

user_points = 0 
computer_points = 0 

while True:
    user_choice = input('0)Pedra\n1)Papel\n2)Tesoura\nEscolha: ')

    if user_choice.isdigit():
        user_choice = int(user_choice)
    else:
        print('Escreva um numero válido!!')
    
    computer_choice = random.randint(0,2)

     
    print(computer_choice)
    break

