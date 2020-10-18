import os
import sqlite3
from Key import Key


class User:

    current_directory = os.getcwd()

    def __init__(self, nombre="", cedula="", correo="", servidor="", clave="", puerto_entrada="", puerto_salida="", ubicacion="", codificador="", p12="", pin=""):
        self.nombre = nombre
        self.cedula = cedula
        self.correo = correo
        self.servidor = servidor
        self.clave = clave
        self.puerto_entrada = puerto_entrada
        self.puerto_salida = puerto_salida
        self.ubicacion = ubicacion
        self.codificador = codificador
        self.p12 = p12
        self.pin = pin

    def connect_sqlite(self):
        db_path = os.path.join(self.current_directory, "nico.db")
        conn = sqlite3.connect(db_path)
        return conn

    def get_user_data(self):
        connection = self.connect_sqlite()
        if connection:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT nombre, cedula, correo, servidor, clave, puerto_entrada, puerto_salida, ubicacion, codificador, p12, pin FROM user_data")

            data = cursor.fetchall()

            if data:
                if len(data) > 0:
                    data = data[0]

                    self.nombre = data[0]
                    self.cedula = data[1]
                    self.correo = data[2]
                    self.servidor = data[3]

                    self.puerto_entrada = data[5]
                    self.puerto_salida = data[6]
                    self.ubicacion = data[7]

                    self.codificador = data[8]
                    self.p12 = data[9]

                    key = Key(key=self.codificador)
                    self.clave = key.decrypt_message(data[4])
                    if len(data[10]) > 0:
                        self.pin = key.decrypt_message(data[10])
                    else:
                        self.pin = ""

    def save_user_data(self):
        connection = self.connect_sqlite()
        if connection:
            key = Key()
            key.generate_key()
            self.codificador = key.key
            self.clave = key.encrypt_message(self.clave)
            self.pin = key.encrypt_message(self.pin)
            cursor = connection.cursor()
            cursor.execute("DELETE FROM user_data")
            connection.commit()
            query_str = """INSERT INTO user_data (nombre, cedula, correo, servidor, clave, puerto_entrada, puerto_salida, ubicacion, codificador, p12, pin) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
            cursor.execute(query_str,
                           (self.nombre, self.cedula, self.correo, self.servidor, self.clave, self.puerto_entrada, self.puerto_salida, self.ubicacion, self.codificador, self.p12, self.pin))
            connection.commit()
            return True
        else:
            print("error")
            return False
