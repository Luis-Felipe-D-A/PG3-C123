
class Usuario:

    usuarios = []

    def __init__(self, nombre, apellidos, email, nickname, clave):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.nickname = nickname
        self.clave = clave

    @classmethod
    def guardarUsuario(cls, nombre, apellidos, email, nickname, clave):
        """
        Guarda un nuevo usuario en la lista global de usuarios.
        """
        usuario = Usuario(nombre, apellidos, email, nickname, clave)
        cls.usuarios.append(usuario)
        return usuario

    @classmethod
    def validarUsuario(cls, nickname, clave):
        """
        Valida credenciales de login.
        Devuelve el objeto Usuario si es correcto, None si falla.
        """
        for usuario in cls.usuarios:
            if usuario.nickname == nickname and usuario.clave == clave:
                return usuario
        return None

    @classmethod
    def getUsuarios(cls):
        """
        Devuelve la lista de usuarios registrados.
        """
        return cls.usuarios
