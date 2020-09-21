from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import QAction
from PySide2.QtWidgets import QMenuBar
from PySide2.QtCore import QDate
from PySide2.QtWidgets import QHeaderView
from PySide2.QtWidgets import QFileDialog
from PySide2.QtWidgets import QTableWidgetItem
from PySide2.QtWidgets import QMessageBox
from UserDataController import UserDataController
from ImportDateController import ImportDateController
from CaronteView import Ui_Caronte
from XmlDocument import XmlDocument
import xlsxwriter
from User import User


class Nico(QMainWindow):

    user_data = None

    def __init__(self):
        super().__init__()
        self.ui = Ui_Caronte()
        self.ui.setupUi(self)
        self.setup_menu()
        self.populate_providers()
        self.setup_signals()
        self.setup_table_headers()
        self.clear_data()
        self.user_data = User()
        self.user_data.get_user_data()

    def setup_menu(self):

        # Import
        self.import_action = QAction('Importar Documentos', self)
        self.import_action.triggered.connect(self.open_import)

        # Settings
        self.settings_action = QAction('Configuración', self)
        self.settings_action.triggered.connect(self.open_settings)

        # Close widget
        self.close_action = QAction('Cerrar', self)
        self.close_action.triggered.connect(self.close)
        self.close_action.setEnabled(True)

        self.menubar = QMenuBar(self)

        self.file_menu = self.menubar.addMenu('&Archivo')
        self.file_menu.addAction(self.import_action)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.settings_action)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.close_action)

        self.menubar.setVisible(True)
        self.menubar.setNativeMenuBar(True)
        # self.menubar.adjustSize()

    def open_settings(self):
        self.user_data = UserDataController()
        self.user_data.show()

    def open_import(self):
        self.import_documents = ImportDateController()
        self.import_documents.show()

    def populate_providers(self):
        self.ui.proveedor.addItem("")
        xml_document = XmlDocument()
        provider_list = xml_document.get_provider_list()
        for element in provider_list:
            self.ui.proveedor.addItem(element[0])

    def setup_signals(self):
        self.ui.buscar.clicked.connect(self.search_edocs)
        self.ui.limpiar.clicked.connect(self.clear_data)
        self.ui.exportar.clicked.connect(self.export_data)

    def get_dates(self, from_date, to_date):
        if from_date > to_date:
            return to_date.toPython().strftime("%Y-%m-%d"), from_date.toPython().strftime("%Y-%m-%d")
        elif from_date < to_date:
            return from_date.toPython().strftime("%Y-%m-%d"), to_date.toPython().strftime("%Y-%m-%d")
        else:
            to_date = to_date.addDays(1)
            return from_date.toPython().strftime("%Y-%m-%d"), to_date.toPython().strftime("%Y-%m-%d")

    def search_edocs(self):
        self.ui.tableWidget.setRowCount(0)
        self.document_list = []
        edocs_data = XmlDocument()
        provider_name = self.ui.proveedor.currentText()
        self.start_date, self.end_date = self.get_dates(
            self.ui.fecha_desde.date(), self.ui.fecha_hasta.date())
        doc_number = self.ui.consecutivo.text()
        query_string = " WHERE documento_electronico.fecha BETWEEN ? AND ? "
        query_list = [self.start_date, self.end_date]
        if len(provider_name.strip()) > 0:
            query_string = f"{query_string} AND documento_electronico.proveedor = ? "
            query_list.append(provider_name)
        if len(doc_number.strip()) > 0:
            query_string = f"{query_string} AND documento_electronico.consecutivo LIKE '%{doc_number.strip()}%' "

        self.document_list = edocs_data.get_edoc_data(
            query_string, tuple(query_list))
        if len(self.document_list) > 0:
            self.add_to_table_widget(self.document_list)

    def add_to_table_widget(self, document_list):
        self.ui.tableWidget.setRowCount(len(self.document_list))
        for row_number, row in enumerate(self.document_list):
            for column_number, column in enumerate(row):
                if 7 <= column_number <= 21:
                    self.ui.tableWidget.setItem(
                        row_number, column_number, QTableWidgetItem("{0:,.2f}".format(float(column))))
                else:
                    self.ui.tableWidget.setItem(
                        row_number, column_number, QTableWidgetItem(column))

        self.ui.tableWidget.resizeColumnsToContents()

    def export_data(self):
        if len(self.document_list) > 0:
            file_path = QFileDialog.getSaveFileName(
                self, "Guardar Archivo Excel", "/", filter="xlsx (*.xlsx)")
            book = xlsxwriter.Workbook(file_path[0])
            sheet1 = book.add_worksheet("Documentos Recibidos")
            sheet1.write_string(0, 0, self.user_data.nombre)
            sheet1.write_string(1, 0, self.user_data.cedula)
            sheet1.write_string(
                4, 0, f"Documentos Recibidos desde: {self.start_date} hasta: {self.end_date}")

            for num, element in enumerate(self.header_list):
                sheet1.write_string(8, num, element)

            text_format = book.add_format({'num_format': '@'})
            currency_format = book.add_format({'num_format': '#,##0.00'})

            row_counter = 9

            for row_number, row in enumerate(self.document_list):
                for column_number, column in enumerate(row):
                    if column is None:
                        column = ""
                    if 7 <= column_number <= 21:
                        sheet1.write_number(
                            row_number + row_counter, column_number, column, currency_format)
                    else:
                        sheet1.write_string(
                            row_number + row_counter, column_number, column, text_format)

            try:
                book.close()
                QMessageBox.information(
                    self, "Exito", "Archivo guardado en: {}".format(file_path[0]))
            except:
                QMessageBox.warning(self, "Error", "El archivo no pudo ser almacenado."
                                                   "\nRevise que no se encuentre en uso en este momento.")
        else:
            QMessageBox.warning(self, "Error", "No hay datos para exportar.")

    def clear_data(self):
        self.ui.fecha_desde.setDate(QDate.currentDate())
        self.ui.fecha_hasta.setDate(QDate.currentDate())
        self.ui.tableWidget.setRowCount(0)
        self.ui.proveedor.setCurrentIndex(0)
        self.document_list = []

    def setup_table_headers(self):
        self.header_list = ["Proveedor", "Cedula", "Tipo Documento", "Clave", "Consecutivo",
                            "Fecha", "Moneda", "Gravado", "Exento", "Exonerado",
                            "SubTotal", "Descuento", "IVA 0%", "IVA 1%", "IVA 2%",
                            "IVA 4%", "IVA 8%", "IVA 13%", "Otros Impuestos", "Total Impuesto",
                            "Otros", "Total", "Resp. Hacienda", "Detalle"]

        self.headers_length = len(self.header_list)
        self.ui.tableWidget.setColumnCount(self.headers_length)
        self.ui.tableWidget.setHorizontalHeaderLabels(self.header_list)
        self.ui.tableWidget.resizeColumnsToContents()


def main():
    from PySide2.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    account_widget = Nico()
    account_widget.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
