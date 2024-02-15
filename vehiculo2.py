

class Vehiculo:
    def __init__(self, marca, modelo, pais_origen, ano_fabricacion, tipo_combustible, chasis, cilindraje):
        self._marca = marca
        self.__modelo = modelo
        self._pais_origen = pais_origen
        self._ano_fabricacion = ano_fabricacion
        self._tipo_combustible = tipo_combustible
        self._chasis = chasis
        self._cilindraje = cilindraje

    def __str__(self):
        return (f"Marca: {self._marca}, Modelo: {self.__modelo}, País de origen: {self._pais_origen}, Año de fabricación: {self._ano_fabricacion}, Tipo de combustible: {self._tipo_combustible}, Chasis: {self._chasis}, Cilindraje: {self._cilindraje}")

    # def get_marca(self):
    #     return self.__marca
    #
    # def set_marca(self, marca):
    #     self.__marca = marca

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

if __name__ == '__main__':
    mi_vehiculo = Vehiculo("Toyota", "Corolla", "Japón", 2020, "Gasolina", "1234567890", 1800)
    print(mi_vehiculo)
    # mi_vehiculo._marca = 'Chery'
    # mi_vehiculo.__modelo = 'Tigo1'
    print(mi_vehiculo)
    # mi_vehiculo.set_marca('Nissan')
    mi_vehiculo.marca = 'Nissan'
    mi_vehiculo.modelo = 'Xtrail'
    print(mi_vehiculo)
