class Vehiculo:
    def __init__(self, FechaDEfabricacion, VIN_chasis, VINMotor):
        self._FechaDEfabricacion = FechaDEfabricacion
        self._VIN_chasis = VIN_chasis
        self._VINMotor = VINMotor

    @property
    def FechaDEfabricacion(self):
        return self._FechaDEfabricacion

    @FechaDEfabricacion.setter
    def FechaDEfabricacion(self, nueva_fecha):
        self._FechaDEfabricacion = 	nueva_fecha

    @property
    def VIN_chasis(self):
        return self._VIN_chasis

    @VIN_chasis.setter
    def VIN_chasis(self, nuevo_vin_chasis):
        self._VIN_chasis = 	nuevo_vin_chasis

    @property
    def VINMotor(self):
        return self._VINMotor

    @VINMotor.setter
    def VINMotor(self, nuevo_vin_motor):
        self._VINMotor = nuevo_vin_motor
