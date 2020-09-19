# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ImportDocuments.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_ImportDateDialog(object):
    def setupUi(self, ImportDateDialog):
        if ImportDateDialog.objectName():
            ImportDateDialog.setObjectName(u"ImportDateDialog")
        ImportDateDialog.resize(557, 447)
        self.verticalLayout = QVBoxLayout(ImportDateDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(ImportDateDialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setInputMethodHints(Qt.ImhNone)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.dateinput_button = QDateEdit(ImportDateDialog)
        self.dateinput_button.setObjectName(u"dateinput_button")
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(15)
        self.dateinput_button.setFont(font1)
        self.dateinput_button.setAlignment(Qt.AlignCenter)
        self.dateinput_button.setProperty("showGroupSeparator", True)
        self.dateinput_button.setCalendarPopup(True)

        self.verticalLayout.addWidget(self.dateinput_button)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.import_button = QPushButton(ImportDateDialog)
        self.import_button.setObjectName(u"import_button")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.import_button.setFont(font2)
        self.import_button.setStyleSheet(u"color: rgb(85, 0, 255);")

        self.gridLayout.addWidget(self.import_button, 0, 1, 1, 1)

        self.close_button = QPushButton(ImportDateDialog)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setFont(font2)
        self.close_button.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout.addWidget(self.close_button, 0, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 4, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.progress_bar = QProgressBar(ImportDateDialog)
        self.progress_bar.setObjectName(u"progress_bar")
        font3 = QFont()
        font3.setPointSize(10)
        self.progress_bar.setFont(font3)
        self.progress_bar.setValue(24)
        self.progress_bar.setTextVisible(False)

        self.verticalLayout.addWidget(self.progress_bar)

        self.progress_text = QTextEdit(ImportDateDialog)
        self.progress_text.setObjectName(u"progress_text")
        self.progress_text.setReadOnly(True)

        self.verticalLayout.addWidget(self.progress_text)

        self.progress_bar.raise_()
        self.label.raise_()
        self.dateinput_button.raise_()
        self.progress_text.raise_()

        self.retranslateUi(ImportDateDialog)

        QMetaObject.connectSlotsByName(ImportDateDialog)
    # setupUi

    def retranslateUi(self, ImportDateDialog):
        ImportDateDialog.setWindowTitle(QCoreApplication.translate("ImportDateDialog", u"Importar Documentos", None))
        self.label.setText(QCoreApplication.translate("ImportDateDialog", u"Seleccione la fecha de inicio de importaci\u00f3n de correos", None))
        self.import_button.setText(QCoreApplication.translate("ImportDateDialog", u"Importar", None))
        self.close_button.setText(QCoreApplication.translate("ImportDateDialog", u"Cerrar", None))
    # retranslateUi

