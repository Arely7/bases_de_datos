import mysql.connector
from mysql.connector import Error

class Conexion:
    def __init__(self):
        self.config = {
            "host":'localhost', #o '127.0.0.1'
            "user":"root",
            "password":"",
            "db":"prueba_pyhton"
        }
        self.conexion = None
        self.cursor = None

    def conectar(self):
        try:
            self.conexion = mysql.connector.connect(**self.config)
            if self.conexion.is_connected():
                print("Conexión exitosa")
                self.cursor = self.conexion.cursor()
        except Error as e:
            print(f"ERROR: {e}")

    #sirve para insertar, modificar o eliminar
    def insertar(self,sql,valores):
            self.cursor.execute(sql,valores)
            self.conexion.commit()
    #sirve para seleccionar
    def seleccionar(self,sql):
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
            return resultado