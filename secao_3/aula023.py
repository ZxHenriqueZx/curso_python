# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.
# Sobrecarga de métodos (overload)  🐍 = ❌
# Sobreposição de métodos (override) 🐍 = ✅

from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, msg) -> None:
        self.mensagem = msg

    @abstractmethod
    def enviar(self) -> bool: ...

class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print(f'Email: {self.mensagem}')
        return True

class NotificacaoSms(Notificacao):
    def enviar(self) -> bool:
        print(f'Sms: {self.mensagem}')
        return True

def notificar(msg: Notificacao):
    notificacao_enviada = msg.enviar()
    print(notificacao_enviada)

    if notificacao_enviada:
        print('Enviou!')
    else:
        print('Não enviou!')

email = NotificacaoEmail('testando email')
sms = NotificacaoSms('Page sua conta da claro')

