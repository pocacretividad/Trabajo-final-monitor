from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from interfaz_ui import Ui_MainWindow  
class Vista(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador
        self.setupUi(self)
        
        self.loginButton.clicked.connect(self.login)
        self.logoutButton.clicked.connect(self.logout)
        self.agregarButton.clicked.connect(self.agregar_paciente)
        self.buscarButton.clicked.connect(self.buscar_paciente)
        self.table.cellDoubleClicked.connect(self.eliminar_paciente)

    def login(self):
        usuario = self.usuarioInput.text()
        contrasena = self.contrasenaInput.text()
        if self.controlador.verificar_credenciales(usuario, contrasena):
            self.stackedWidget.setCurrentIndex(1)  
            self.actualizar_tabla()
        else:
            QMessageBox.critical(self, "Error", "Usuario o contraseña incorrectos")

    def logout(self):
        self.stackedWidget.setCurrentIndex(0)  

    def agregar_paciente(self):
        nombre = self.nombreInput.text()
        apellido = self.apellidoInput.text()
        edad = self.edadInput.text()
        identificacion = self.identificacionInput.text()
        if self.controlador.agregar_paciente(nombre, apellido, edad, identificacion):
            QMessageBox.information(self, "Éxito", "Paciente agregado correctamente")
            self.actualizar_tabla()
        else:
            QMessageBox.critical(self, "Error", "Identificación ya existente")

    def buscar_paciente(self):
        nombre = self.nombreInput.text()
        pacientes = self.controlador.buscar_pacientes(nombre)
        if not pacientes:
            QMessageBox.information(self, "Mensaje", "Paciente no encontrado.")
            return
        self.table.setRowCount(len(pacientes))
        for i, paciente in enumerate(pacientes):
            for j, dato in enumerate(paciente):
                self.table.setItem(i, j, QTableWidgetItem(str(dato)))

    def eliminar_paciente(self, row, column):
        paciente_id = self.table.item(row, 0).text()
        self.controlador.eliminar_paciente(paciente_id)
        self.table.removeRow(row)

    def actualizar_tabla(self):
        pacientes = self.controlador.obtener_todos_pacientes()
        self.table.setRowCount(0)
        for paciente in pacientes:
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            for i, data in enumerate(paciente):
                self.table.setItem(row_position, i, QTableWidgetItem(str(data)))