from persona import Persona

class Empleado(Persona):
    def __init__(self, nombre, cedula, genero, ocupacion, sueldo):
        Persona.__init__(self, nombre=nombre, genero=genero, ocupacion=ocupacion, cedula=cedula)
        self._sueldo = sueldo

    def __str__(self):
        return f'Empleado[ Sueldo: {self._sueldo}], {super().__str__()}'

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

if __name__=='__main__':
    e1 = Empleado('Carlos', '1234567890', 'M', 'Tegnolog', 1500)
    print(e1)
    e1.cedula = '09876543210'
    print(e1)