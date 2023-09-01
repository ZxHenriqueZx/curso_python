import pessoa_cliente
import contas


class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []

    def get_cliente(self, cliente):
        self.clientes.append(cliente)

    def get_contas(self, conta):
        self.contas.append(conta)

if __name__ == '__main__':
    conta1 = contas.ContaCorrente(2564, 856425, 100)
    conta2 = contas.ContaPoupanca(1544, 8456923, 500)
    luis = pessoa_cliente.Cliente('Luis', 18, conta1)
    pedro = pessoa_cliente.Cliente('Pedro', 25, conta2)
    itau = Banco()

