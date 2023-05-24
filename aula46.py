for i in range(10):
    if i == 2:
        print('i é 2!! continua')
        continue
    
    if i == 4:
        print('i é 4!! para!!')    
        break

    if i == 6:
        print('i é 6!! nunca sera executado')

    for j in range(1, 3):
        print(i , j)
else:
    ('oi')