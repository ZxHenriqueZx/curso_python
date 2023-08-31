import contas
from abc import ABC

conta1 = contas.ContaCorrente(1254, 85462, 500)

class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Cliente(Pessoa):
    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade)
        self.conta = conta

if __name__ == '__main__':
    luis = Cliente('Luis', 18, conta1)
