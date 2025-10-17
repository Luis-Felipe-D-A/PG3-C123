class Animal:
    def __init__(self, nombre, peso, propietario, fecha_cumpleaños, fecha_ultima_vacuna):
        self._nombre = nombre
        self._peso = peso
        self._propietario = propietario
        self._fecha_cumpleaños = fecha_cumpleaños
        self._fecha_ultima_vacuna = fecha_ultima_vacuna


    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    
    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, nuevo_peso):
        self._peso = nuevo_peso


    @property
    def propietario(self):
        return self._propietario

    @propietario.setter
    def propietario(self, nuevo_propietario):
        self._propietario = nuevo_propietario

    
    @property
    def fecha_cumpleaños(self):
        return self._fecha_cumpleaños

    @fecha_cumpleaños.setter
    def fecha_cumpleaños(self, nueva_fecha):
        self._fecha_cumpleaños = nueva_fecha

    
    @property
    def fecha_ultima_vacuna(self):
        return self._fecha_ultima_vacuna

    @fecha_ultima_vacuna.setter
    def fecha_ultima_vacuna(self, nueva_fecha):
        self._fecha_ultima_vacuna = nueva_fecha
    