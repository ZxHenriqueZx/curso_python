from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, num, saldo):
        self._agencia = agencia
        self._num = num
        self._saldo = saldo

    @abstractmethod
    def sacar(self): ...

    def depositar(self, valor):
        self._saldo += valor
        self.noti(f'Depositado: +R${valor}')

    def noti(self, msg=''):
        return print(f'O seu saldo é {self._saldo:.2f} {msg}')

class ContaCorrente(Conta):
    def __init__(self, agencia, num, saldo):
        super().__init__(agencia, num, saldo)
        self._limite = -1000

    def sacar(self, valor):
        if valor < self._limite:
            self.noti('Não foi possivel sacar: Limite Excedido!!')
        else:
            self._saldo -= valor
            self.noti(f'Sacado: -R${valor}')

    def __repr__(self):
        return 'Conta Corrente'

class ContaPoupanca(Conta):
    def __init__(self, agencia, num, saldo):
        super().__init__(agencia, num, saldo)
        self._limite = 0

    def sacar(self, valor):
        if valor < self._limite:
            print(self.noti('Não foi possivel sacar: Limite Excedido!!'))
        else:
            self._saldo -= valor
            self.noti(f'Sacado: -R${valor}')

if __name__ == '__main__':
    c1 = ContaCorrente(8562, 12583312, 250)
    c2 = ContaPoupanca(7621, 58423658, 1000)

