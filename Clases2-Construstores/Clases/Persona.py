class Persona:
    # Constructor de la clase
    def __init__(self, nombre, apellido):
        self._nombre = nombre
        self._apellido = apellido

    # Método GET
    @property
    def nombre(self):
        return self._nombre

    # Método SET
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    # Método GET
    @property
    def apellido(self):
        return self._apellido

    # Método_SET
    @apellido.setter
    def apellido(self, nuevo_apellido):
        self._apellido = nuevo_apellido
