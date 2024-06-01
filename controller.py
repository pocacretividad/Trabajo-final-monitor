import sys
from PyQt5 import QtWidgets
from model import Modelo
from view import Vista

class Controlador:
    def __init__(self):
        self.modelo = Modelo()
        self.app = QtWidgets.QApplication(sys.argv)
        self.vista = Vista(self)
        self.vista.show()
        sys.exit(self.app.exec_())

    def verificar_credenciales(self, usuario, contrasena):
        return usuario == "admin123" and contrasena == "contrasena123"

    def agregar_paciente(self, nombre, apellido, edad, identificacion):
        return self.modelo.agregar_paciente(nombre, apellido, edad, identificacion)

    def buscar_pacientes(self, nombre):
        return self.modelo.buscar_pacientes(nombre)

    def obtener_todos_pacientes(self):
        return self.modelo.obtener_todos_pacientes()

    
if __name__ == "__main__":
    Controlador()
    
    #pyuic5 -o interfaz_ui.py interfaz.ui
    
    #integrantes:
    #Huber Londoño, Juan Manuel Loaiza, Juan Sebastian Castro 
    
    