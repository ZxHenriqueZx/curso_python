# (Parte 2) Threads - Executando processamentos em paralelo
from time import sleep
from threading import Thread

def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)

t = Thread(target=vai_demorar, args=('Hello World', 10))
t.start()

while t.is_alive():
    print('Esperando Thread!')
    sleep(3)

