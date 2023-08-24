# Classes decoradoras (Decorator classes)
class Multiplicar:
    def __init__(self, multi):
        self.multi = multi

    def __call__(self, func):
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self.multi
        return interna


@Multiplicar(5)
def soma(x,y):
    return x + y

soma1 = soma(5, 5)
print(soma1)
