from clases.conector import Conector

class Clientes:
    def __init__(self):
        self.db = Conector()

    def validar_cliente(self, username, clave):
        sql = "SELECT * FROM clientes WHERE username = %s AND clave = %s"
        values = (username, clave)
        resultado = self.db.select(sql, values)
        return resultado[0] if resultado else None

    def guardar_cliente(self, nombre, apellido, email, username, clave, rol):
        sql = "INSERT INTO clientes (nombre, apellido, email, username, clave, rol) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (nombre, apellido, email, username, clave, rol)
        return self.db.execute_query(sql, values)

    def actualizar_cliente(self, id_cliente, nombre, apellido, username, email, rol, clave=None):
        if clave:  
            sql = "UPDATE clientes SET nombre=%s, apellido=%s, username=%s, email=%s, rol=%s, clave=%s WHERE id=%s"
            values = (nombre, apellido, username, email, rol, clave, id_cliente)
        else: 
            sql = "UPDATE clientes SET nombre=%s, apellido=%s, username=%s, email=%s, rol=%s WHERE id=%s"
            values = (nombre, apellido, username, email, rol, id_cliente)

        return self.db.execute_query(sql, values)

    def eliminar_cliente(self, id_cliente):
        sql = "DELETE FROM clientes WHERE id = %s"
        values = (id_cliente,)
        return self.db.execute_query(sql, values)

    def listar_clientes(self):
        sql = "SELECT id, nombre, apellido, username, email, rol FROM clientes"
        return self.db.select(sql)
