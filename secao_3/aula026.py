# Exemplo de uso de dunder methods (métodos mágicos)
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r})'

    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)

    def __gt__(self, other):
        sum_self = self.x + self.y
        sum_other = other.x + other.y
        print(sum_self)
        print(sum_other)
        return sum_self > sum_other

if __name__ == '__main__':
    p1 = Ponto(50, 50)
    p2 = Ponto(10, 10)
    p3 = p1 + p2
    print('P1 é maior que P2?', p1 > p2)
    print('P2 é maior que P1?', p2 > p1)

