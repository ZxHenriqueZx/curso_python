# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.endereco = []

    def inserir_ende(self, rua, numero):
        self.endereco.append(Endereco(rua, numero))

    def listar_enderecos(self):
        for e in self.endereco:
            print(e.rua, e.num)

    def __del__(self):
        print()
        print('apagando...', self.nome)

class Endereco:
    def __init__(self, rua, num):
        self.rua = rua
        self.num = num

    def __del__(self):
        print()
        print('apagando...', self.rua, self.num)


cliente = Cliente('João')
cliente.inserir_ende('Rua Pedro', 557)
cliente.inserir_ende('Rua sei la', 58)
cliente.listar_enderecos()
