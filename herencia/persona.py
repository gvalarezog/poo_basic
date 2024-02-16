#Guillermo Valarezo
class Persona:
    '''
    Crear los objetos de tipo Persona
    '''
    def __init__(self, nombre, genero, ocupacion=None, cedula=None): #metodo que inicializa al objeto de tipo persona (constructor)
        self._nombre = nombre
        self._genero = genero
        self._ocupacion = ocupacion
        self._cedula = cedula
        #agregar un nuevo atributo cedula
        #encapsular todos los atributos con los decoradores

    def __str__(self): #downders son sobre escritos
        return (f'Persona: [nombre: {self._nombre}, genero: {self._genero}, '
                f'ocupación: {self._ocupacion}, cedula: {self._cedula}]')

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula

    def saludar(self):
        print(f'Hola soy {self._nombre}')


if __name__ == '__main__':
    obj_persona1 = Persona('Luis', 'M', 'Estudiante')
    print(obj_persona1.__str__())
    obj_persona2 = Persona(genero='F', ocupacion='Tecnolog', nombre='Maria')
    print(obj_persona2)
    p3 = Persona(nombre='Jose', genero='M')
    print(p3)
    obj_persona1.saludar()
    # p3.cedula = '0123456789'
    print(p3)
    p4 = Persona(cedula='9876543210', nombre='Carlos', genero='M')
    print(p4)
    # p4.cedula = '6541239870'
    print(p4.cedula)

