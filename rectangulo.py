from herencia.color import Color
from herencia.figura_geometrica import FiguraGeometrica


class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, alto=alto, ancho=ancho)
        Color.__init__(self, color=color)

    def area(self):
        return (self._alto * self._ancho)/2

    def __str__(self):
        return f"Rectagunlo: [ancho={self.ancho}, alto={self.alto}, color={self.color}]"

if __name__ == '__main__':
    r1 = Rectangulo(ancho=9, color="Rojo", alto=5)
    print(r1)