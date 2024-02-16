class FiguraGeometrica:
    def __init__(self, alto, ancho):
        self._alto = alto
        self._ancho = ancho

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        self._alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho

    def __str__(self):
        return f"Figura Geometrica: {self.__dict__.__str__()}"


if __name__ == '__main__':
    fg1 = FiguraGeometrica(10, 20)
    print(fg1)
    print(__name__)
