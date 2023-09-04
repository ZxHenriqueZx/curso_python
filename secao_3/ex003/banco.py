import pessoa_cliente
import contas


class Banco:
    def __init__(self, nome, agencias, clientes):
        self.nome = nome
        self.agencias = agencias
        self.clientes = clientes

    def autenticar(self, agencias, clientes):
        ...

if __name__ == '__main__':
    ...
