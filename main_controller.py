import sys
from PyQt6 import QtWidgets, uic
from conexion import Conexion

class MainController(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui",self)
        self.conexion = Conexion()
        self.conexion.conectar()
        self.btn_insertar.connect(self.add_user)
    
    def add_user(self):
        name = self.txt_nombre.text()
        last = self.txt_apellido.text()
        email = self.txt_email.text()
        passw = self.txt_password.text()
        passw_confirm = self.txt_confirmar.text()

        if name.strip() == "" or last.strip() == "" or email.strip() == "" or passw.strip() == "" or passw_confirm.strip() == "":
            QtWidgets.QMessageBox.warning(self, "Favor de llenar todos los campos")
        elif passw.strip() != passw_confirm.strip():
            QtWidgets.QMessageBox.warning(self,"Las contraseñas no coinciden")
        else:
            sql = "INSERT INTO users values (%s,%s,%s,%s,%s,%s)"
            valores = ((0,name,last,email,passw,'defaul.jpg'))