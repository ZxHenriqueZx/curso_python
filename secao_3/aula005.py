# Mantendo estados dentro da classe
class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando == True:
            print(f'A câmera {self.nome} JÁ esta filmando!!')
            return

        print(f'A câmera {self.nome} esta filmando...')
        self.filmando = True

    def parar_filmar(self):
        if self.filmando:
            self.filmando = False
            print(f'A camera {self.nome} PAROU de filmar!!')
        else:
            print(f'A câmera {self.nome} NÃO esta filmando')

    def tirar_foto(self):
        if self.filmando:
            print(f'A câmera {self.nome} esta filmando, não é possivel tirar a foto')
            return

        print(f'A câmera {self.nome} TIROU uma foto!!!')

