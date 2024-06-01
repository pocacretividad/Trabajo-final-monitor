import sqlite3

class Modelo:
    def __init__(self):
        self.conexion = sqlite3.connect('pacientes.db')
        self.crear_tabla()

    def crear_tabla(self):
        with self.conexion:
            self.conexion.execute("""
                CREATE TABLE IF NOT EXISTS pacientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    apellido TEXT NOT NULL,
                    edad INTEGER NOT NULL,
                    identificacion TEXT NOT NULL UNIQUE
                )
            """)

    def agregar_paciente(self, nombre, apellido, edad, identificacion):
        try:
            with self.conexion:
                self.conexion.execute("INSERT INTO pacientes (nombre, apellido, edad, identificacion) VALUES (?, ?, ?, ?)",
                                      (nombre, apellido, edad, identificacion))
            return True
        except sqlite3.IntegrityError:
            return False

    def eliminar_paciente(self, id):
        with self.conexion:
            self.conexion.execute("DELETE FROM pacientes WHERE id = ?", (id,))

    def buscar_pacientes(self, nombre):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM pacientes WHERE nombre LIKE ?", (nombre + '%',))
        return cursor.fetchall()
    
    def obtener_todos_pacientes(self):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM pacientes")
        return cursor.fetchall()