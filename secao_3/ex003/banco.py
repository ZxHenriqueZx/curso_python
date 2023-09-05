import contas

class Banco:
    def __init__(self, nome, agencias, clientes, contas):
        self.nome = nome
        self.agencias = agencias
        self.clientes = clientes
        self.contas = contas

    def autenticar(self, agencias, clientes, contas):
        for agen in agencias:
            if agen in self.agencias:
                print(f'{agen} esta no nosso banco de dados')
            else:
                print(f'{agen} não esta no nosso banco de dados')

        print()

        for clie in clientes:
            if clie in self.clientes:
                print(f'{clie} esta no nosso banco de dados')
            else:
                print(f'{clie} não esta no nosso banco de dados')

        print()

        for con in contas:
            if con in self.contas:
                print(f'{con} esta no nosso banco de dados')
            else:
                print(f'{con} não esta no nosso banco de dados')

    def autenticar_conta(self, clientes):
        for clie in clientes:
            if isinstance(clie.conta, contas.Conta) and clie.conta in self.contas:
                print(f'Conta:{clie.conta} Válida!!!')
            else:
                print(f'Conta:{clie.conta} Inválida!!!')

if __name__ == '__main__':
    ...
