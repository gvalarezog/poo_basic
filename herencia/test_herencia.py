from herencia.cuadrado import Cuadrado
from rectangulo import Rectangulo

tipo_figura = input('Ingrese C para Cuadrado o R para Rectangulo: ')
color = input('Ingrese el color: ')


if tipo_figura.upper() == 'C':
    lado = float(input('Ingrese el largo del lado: '))
    c1 = Cuadrado(lado=lado, color=color)
    print(c1)
elif tipo_figura.upper() == 'R':
    ancho = float(input('Ingrese el ancho: '))
    alto = float(input('Ingrese el alto: '))
    r1 = Rectangulo(ancho=ancho, alto=alto, color=color)
    print(r1)
else:
    print('Opción no valida')

