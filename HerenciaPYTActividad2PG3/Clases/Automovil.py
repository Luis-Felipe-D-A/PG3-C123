from Clases.Vehiculo import *

class Automovil(Vehiculo):
    def __init__(self, FechaDEfabricacion, VIN_chasis, VINMotor, marca, modelo, precio):
        super().__init__(FechaDEfabricacion, VIN_chasis, VINMotor)
        self._marca = marca
        self._modelo = modelo
        self._precio = precio

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, nueva_fecha):
        self._marca = nueva_fecha

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, nuevo_modelo):
        self._modelo = nuevo_modelo

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio):
        self._precio = nuevo_precio

    def imprimir(self):
        print('Información del Vehiculo')
        print(f'Fecha de Fabricación: {self.FechaDEfabricacion}')
        print(f'VIN del Chasis: {self.VIN_chasis}')
        print(f'VIN del Motor: {self.VINMotor}')
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Precio: ${self.precio:,.2f}')
