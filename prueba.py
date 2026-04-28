#pip install mysql-connector-python
import mysql.connector
from mysql.connector import Error

config = {
    "host":'localhost', #o '127.0.0.1'
    "user":"root",
    "password":"",
    "db":"prueba_pyhton"
}
conexion = None
try:
    conexion = mysql.connector.connect(**config)
    if conexion.is_connected():
        print("Conexión exitosa")
        name = input("Ingresa tu nombre: ")
        last_name = input("Ingresa tu apellido: ")
        email = input("Ingresa tu email: ")
        password = input("Ingresa tu password: ")
        #Insertar datos
        sql = "INSERT INTO users values (%s,%s,%s,%s,%s,%s)"
        valores = ((0,name,last_name,email,password,'defaul.jpg'))
        cursor = conexion.cursor()
        cursor.execute(sql,valores)
        conexion.commit()
        print("Registro insertado correctamente")
        #Consultar datos
        sql = "select * from users order by id DESC"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        for fila in resultado:
            print("-"*50)
            print(f"Email: {fila[3]}, Nombre: {fila[1]}, Id: {fila[0]}")
            print("-"*50)
except Error as e:
    print(f"ERROR: {e}")
finally:
    if conexion and conexion.is_connected():
        cursor.close()
        conexion.close()