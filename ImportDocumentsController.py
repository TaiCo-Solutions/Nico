from PySide2.QtWidgets import QDialog
from ImportDateView import Ui_ImportDateDialog
from PySide2.QtCore import Signal
from PySide2.QtCore import QDate


class ImportDocumentsController(QDialog):
    from_date = Signal(str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_ImportDateDialog()
        self.ui.setupUi(self)
        self.ui.dateinput_button.setDate(QDate.currentDate())
        self.setModal(True)
        self.setup_signals()

    def setup_signals(self):
        self.ui.import_dialog_button.accepted.connect(self.send_date_signal)
        self.ui.import_dialog_button.rejected.connect(self.close)

    def send_date_signal(self):
        self.from_date.emit(self.ui.dateinput_button.date().toPython().strftime("%d-%b-%Y"))
        self.close()


def main():
    from PySide2.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    bill_widget = ImportDocumentsController()
    bill_widget.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
