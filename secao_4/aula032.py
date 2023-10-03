# (Parte 1) Threads - Executando processamentos em paralelo
from time import sleep
from threading import Thread

class MyThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)

t1 = MyThread('Hello world 1', 7)
t1.start()

t2 = MyThread('Hello world 2', 5)
t2.start()

t3 = MyThread('Hello world 3', 3)
t3.start()

for i in range(10):
    print(i)
    sleep(1)

