from herencia.cuadrado import Cuadrado
from rectangulo import Rectangulo

def mostrar_area(figuras_geometricas):
    for figura_geometrica in figuras_geometricas:
        print(figura_geometrica.area())

r1 = Rectangulo(ancho=9, color="Rojo", alto=2)
r2 = Rectangulo(ancho=5, color="Azul", alto=6)
r3 = Rectangulo(ancho=6, color="Naranja", alto=10)
r4 = Rectangulo(ancho=7, color="Verde", alto=12)

c1 = Cuadrado(lado=9, color="Amarillo")
c2 = Cuadrado(lado=8, color="Rosa")
c3 = Cuadrado(lado=3, color="Cafe")
c4 = Cuadrado(lado=5, color="Negro")

rectangulos = list()
rectangulos.append(r1)
rectangulos.append(r2)
rectangulos.append(r3)
rectangulos.append(r4)

cuadrados = list()
cuadrados.append(c1)
cuadrados.append(c2)
cuadrados.append(c3)
cuadrados.append(c4)

# print(rectangulos)
# print(cuadrados)
mostrar_area(rectangulos)
mostrar_area(cuadrados)
print('*'.center(50,'x'))
lista_figuras_geometricas = list()
lista_figuras_geometricas.append(r1)
lista_figuras_geometricas.append(c1)
lista_figuras_geometricas.append(r2)
lista_figuras_geometricas.append(c2)
lista_figuras_geometricas.append(r3)
lista_figuras_geometricas.append(c3)
lista_figuras_geometricas.append(r4)
lista_figuras_geometricas.append(c4)

mostrar_area(lista_figuras_geometricas)


