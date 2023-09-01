import contas

conta1 = contas.ContaCorrente(1254, 85462, 500)
conta2 = contas.ContaPoupanca(5684, 85429, 100)

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

        def __repr__(self):
            return f'Nome: {self.nome} - Idade: {self.idade}'

class Cliente(Pessoa):
    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade)
        self.conta = conta

if __name__ == '__main__':
    luis = Cliente('Luis', 18, conta1)
    pedro = Cliente('Pedro', 25, conta2)
