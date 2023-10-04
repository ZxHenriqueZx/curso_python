# (Parte 3) Threads - Executando processamentos em paralelo
from threading import Thread, Lock
from time import sleep
class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire()
        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            self.lock.release()
            return

        sleep(1)

        print(f'Você comprou {quantidade} ingressos!!')
        self.estoque -= quantidade
        print(f'Ingressos restantes: {self.estoque}!!')

        self.lock.release()

estoque_1 = Ingressos(15)
for i in range(1, 20):
    t = Thread(target=estoque_1.comprar, args=(i,))
    t.start()
