from PySide2.QtWidgets import QDialog
from PySide2.QtCore import Signal
from PySide2.QtCore import QDate
from PySide2.QtCore import QThreadPool
from PySide2.QtCore import QRunnable
from PySide2.QtCore import QObject
from PySide2.QtGui import QTextCursor
from PySide2 import QtCore
from PySide2.QtWidgets import QMessageBox

import sys
import os
import subprocess
import time
import traceback
import imaplib
import email
import base64

from ImportDateView import Ui_ImportDateDialog
from EmailDownload import EmailDownload
from XmlFinder import XmlFinder
from User import User


class ImportDateController(QDialog):
    from_date = Signal(str)
    start_date = QDate.currentDate().toPython().strftime("%d-%b-%Y")
    current_process = None

    def __init__(self):
        super().__init__()
        self.started = False
        self.current_user = User()
        self.current_user.get_user_data()
        self.ui = Ui_ImportDateDialog()
        self.ui.setupUi(self)
        self.ui.date_start.setDate(QDate.currentDate())
        self.ui.date_end.setDate(QDate.currentDate().addDays(1))
        self.setModal(True)
        self.threadpool = QThreadPool()
        self.setup_signals()

    def setup_signals(self):
        self.ui.progress_bar.setRange(0, 1)
        self.ui.import_button.clicked.connect(self.send_date_signal)
        self.ui.close_button.clicked.connect(self.close)

    def get_start_end_date(self):
        start_date = self.ui.date_start.date()
        end_date = self.ui.date_end.date()
        if start_date > end_date:
            return end_date.toPython().strftime("%d-%b-%Y"), start_date.toPython().strftime("%d-%b-%Y")
        elif start_date == end_date:
            end_date.addDays(1)

        return start_date.toPython().strftime("%d-%b-%Y"), end_date.toPython().strftime("%d-%b-%Y")

    def send_date_signal(self):
        self.ui.import_button.setEnabled(False)
        self.ui.close_button.setEnabled(False)
        self.start_date, self.end_date = self.get_start_end_date()
        self.ui.progress_text.clear()
        if len(self.current_user.servidor) > 0:
            self.ui.progress_text.append(
                f"IMPORTANDO DOCUMENTOS DESDE: {self.start_date} HASTA: {self.end_date}\n")
            self.run()
        else:
            QMessageBox.critical(self, "ERROR", "Los datos del correo no están registrados. Por favor actualice la información.")        
            self.close()

    def run(self):
        """ Call process """
        if not self.started:
            self.started = True
            self.run_threaded_process(
                self.import_documents, self.progress_function, self.finished_function)

    def run_threaded_process(self, process, progress_function, finished_function):
        worker = Worker(process)
        self.threadpool.start(worker)
        worker.signals.finished.connect(self.finished_function)
        worker.signals.progress.connect(self.progress_function)
        self.ui.progress_bar.setRange(0, 0)
        return

    def progress_function(self, text_output):
        self.ui.progress_text.append(f"{text_output}")

    def finished_function(self):
        self.ui.progress_bar.setRange(0, 1)
        self.ui.progress_text.append(
            """\n\n\n======================\n|     PROCESO FINALIZADO      |\n======================""")
        self.ui.progress_text.moveCursor(QTextCursor.End)
        self.ui.import_button.setEnabled(True)
        self.ui.close_button.setEnabled(True)
        self.started = False

    def import_documents(self, progress_callback):

        # Descargar del correo

        mail_downloader = EmailDownload(self.ui.progress_text)
        if mail_downloader.connection:
            mail_downloader.get_mail_data(self.start_date, self.end_date)

            # Buscar y procesar xml

            xml_finder = XmlFinder(self.ui.progress_text)
        return


class Worker(QRunnable):

    def __init__(self, current_function, *args, **kwargs):
        super().__init__()
        self.current_function = current_function
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        self.kwargs['progress_callback'] = self.signals.progress

    @QtCore.Slot()
    def run(self):
        try:
            result = self.current_function(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            excemption_type, value = sys.exc_info()[:2]
            self.signals.error.emit(
                (excemption_type, value, traceback.format_exc()))

        else:
            self.signals.result.emit(result)

        finally:
            self.signals.finished.emit()


class WorkerSignals(QObject):
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(str)


def main():
    from PySide2.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    bill_widget = ImportDateController()
    bill_widget.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
