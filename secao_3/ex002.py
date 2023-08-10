# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

class Motor:
    def __init__(self, nome):
        self.nome = nome

    def ligar(self):
        print(f'O motor {self.nome} ligou...')

class Carro:
    def __init__(self, nome, motor, fabricante):
        self.nome = nome
        self._motor = motor
        self._fabricante = fabricante

    @property
    def ligar_motor(self):
        return self._motor.ligar()

    @ligar_motor.setter
    def definir_motor(self, motor):
        self._motor = motor

    def stats(self):
        print(f'Fabricante: {self._fabricante.nome}\n'
              f'Motor: {self._motor.nome}\n'
              f'Nome: {self.nome}')

motor_1_0 = Motor('Motor 1.0')
motor_2_0 = Motor('Motor 2.0')
volkswagem = Fabricante('Volkswagem')
fusca = Carro('Fusca', motor_1_0, volkswagem)

motor_b58 = Motor('Motor B58')
toyota = Fabricante('Toyota')
supra = Carro('Toyota Supra', motor_b58, toyota)

