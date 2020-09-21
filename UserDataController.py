from UserDataView import Ui_UserData
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QMessageBox
from PySide2.QtWidgets import QFileDialog
from email_validator import validate_email, EmailNotValidError
from User import User


class UserDataController(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_UserData()
        self.ui.setupUi(self)
        self.setup_signals()
        self.nombre = ""
        self.cedula = ""
        self.correo = ""
        self.clave = ""
        self.servidor = ""
        self.puerto_entrada = ""
        self.puerto_salida = ""
        self.ubicacion = ""
        self.p12 = ""
        self.pin = ""
        self.string_list = []
        self.populate_data()

    def setup_signals(self):
        self.ui.close_button.clicked.connect(self.close)
        self.ui.save_button.clicked.connect(self.save_data)
        self.ui.change_directory_button.clicked.connect(self.update_path)
        self.ui.change_p12_button.clicked.connect(self.update_p12_path)

    def populate_data(self):
        current_data = User()
        current_data.get_user_data()
        self.ui.nombre.setText(current_data.nombre)
        self.ui.cedula.setText(current_data.cedula)
        self.ui.correo.setText(current_data.correo)
        self.ui.clave.setText(current_data.clave)
        self.ui.servidor.setText(current_data.servidor)
        self.ui.puerto_entrada.setText(current_data.puerto_entrada)
        self.ui.puerto_salida.setText(current_data.puerto_salida)
        self.ui.ubicacion.setText(current_data.ubicacion)
        self.ui.p12.setText(current_data.p12)
        self.ui.pin.setText(current_data.pin)

    def save_data(self):
        if self.review_data():
            user = User(nombre=self.nombre, cedula=self.cedula, correo=self.correo, clave=self.clave,
                        servidor=self.servidor, puerto_entrada=self.puerto_entrada, puerto_salida=self.puerto_salida, ubicacion=self.ubicacion,
                        p12=self.p12, pin=self.pin)
            result = user.save_user_data()
            if result:
                QMessageBox.information(self, "Éxito", "Cambios guardados")
                self.close()
            else:
                self.send_error_message(
                    self, "Error", "Los cambios no se pudieron guardar. Por favor verificar los datos y que la base de datos este disponible.")

    def update_path(self):
        path_name = QFileDialog.getExistingDirectory(
            self, "Seleccione carpeta de descarga y lectura", "/")
        self.ui.ubicacion.setText(path_name)

    def update_p12_path(self):
        path_name = QFileDialog.getOpenFileName(
            self, "Seleccione el archivo P12", "/", "p12 (*.p12)")
        self.ui.p12.setText(path_name[0])

    def review_data(self):
        self.nombre = self.ui.nombre.text()
        self.cedula = self.ui.cedula.text()
        self.correo = self.ui.correo.text()
        self.clave = self.ui.clave.text()
        self.servidor = self.ui.servidor.text()
        self.puerto_entrada = self.ui.puerto_entrada.text()
        self.puerto_salida = self.ui.puerto_salida.text()
        self.ubicacion = self.ui.ubicacion.text()
        self.p12 = self.ui.p12.text()
        self.pin = self.ui.pin.text()

        self.string_list = [self.nombre, self.cedula, self.correo,
                            self.clave, self.servidor, self.puerto_entrada, self.puerto_salida, self.ubicacion]

        for element in self.string_list:
            if len(element.strip()) <= 0:
                self.send_error_message("Error",
                                        "Los campos no pueden quedar vacíos")
                return False

        try:
            validation = validate_email(self.correo)  # validate and get info
            self.correo = validation["email"]  # replace with normalized form

        except EmailNotValidError as e:
            self.send_error_message("Error", "Correo inválido")
            self.ui.correo.setFocus()
            return False

        return True

    def send_error_message(self, title, text, placeholder=None):
        QMessageBox.critical(self,
                             title,
                             text)

        if placeholder:
            placeholder.setFocus()
