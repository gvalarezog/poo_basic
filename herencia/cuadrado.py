from herencia.color import Color
from herencia.figura_geometrica import FiguraGeometrica


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, alto=lado, ancho=lado)
        Color.__init__(self, color=color)

    def area(self):
        return (self.ancho * self.alto)/4


    def __str__(self):
        return f'Cuadrado [lado={self.alto}, color= {self.color}]'

if __name__ == '__main__':
    c1 = Cuadrado(lado=9, color="Rojo")
    print(c1)