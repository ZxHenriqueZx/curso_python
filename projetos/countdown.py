import time

tempo = input('Escreva o tempo em segundos: ')

if tempo.isdigit():
    tempo = int(tempo)
else:
    print('Isto não é um número!!!')

while tempo > 0:
    minutos, segundos = divmod(tempo,60)
    timer = '{:02d}:{:02d}'.format(minutos, segundos)
    print(timer, end='\r')
    time.sleep(1)
    tempo -= 1 

