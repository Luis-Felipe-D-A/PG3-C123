import mysql.connector

class Conector:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "tecnar_app_py2"

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            return self.cursor
        except mysql.connector.Error as error:
            print(error)

    def close(self):  
        self.cursor.close()
        self.connection.close()

    # Ejecutar consultas SQL Tipo SELECT
    def select(self, sql, values=None):
        try:
            self.cursor = self.connect()
            self.cursor.execute(sql, values or ())
            result = self.cursor.fetchall()
            self.close()  
            return result
        except mysql.connector.Error as error:
            print(error)
            return False

    # Ejecutar consultas de INSERT, UPDATE y DELETE
    def execute_query(self, sql, values=None):
        try:
            self.cursor = self.connect()
            self.cursor.execute(sql, values or ())
            self.connection.commit()
            self.close()  
            return True
        except mysql.connector.Error as error:
            print(error)
            return False