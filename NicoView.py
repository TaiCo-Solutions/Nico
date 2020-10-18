# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'caronte.ui'
##
# Created by: Qt User Interface Compiler version 5.14.1
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Nico(object):
    def setupUi(self, Caronte):
        if Caronte.objectName():
            Caronte.setObjectName(u"Caronte")
        Caronte.resize(1065, 788)
        self.centralwidget = QWidget(Caronte)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(
            10, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.fecha_desde = QDateEdit(self.centralwidget)
        self.fecha_desde.setObjectName(u"fecha_desde")
        font = QFont()
        font.setPointSize(10)
        self.fecha_desde.setFont(font)
        self.fecha_desde.setCalendarPopup(True)

        self.gridLayout.addWidget(self.fecha_desde, 1, 1, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)

        self.proveedor = QComboBox(self.centralwidget)
        self.proveedor.setObjectName(u"proveedor")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.proveedor.sizePolicy().hasHeightForWidth())
        self.proveedor.setSizePolicy(sizePolicy)
        self.proveedor.setFont(font)

        self.gridLayout.addWidget(self.proveedor, 0, 3, 1, 1)

        self.consecutivo = QLineEdit(self.centralwidget)
        self.consecutivo.setObjectName(u"consecutivo")
        self.consecutivo.setFont(font)

        self.gridLayout.addWidget(self.consecutivo, 0, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.fecha_hasta = QDateEdit(self.centralwidget)
        self.fecha_hasta.setObjectName(u"fecha_hasta")
        self.fecha_hasta.setFont(font)
        self.fecha_hasta.setCalendarPopup(True)

        self.gridLayout.addWidget(self.fecha_hasta, 1, 3, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.buscar = QPushButton(self.centralwidget)
        self.buscar.setObjectName(u"buscar")
        self.buscar.setFont(font1)
        self.buscar.setStyleSheet(u"color: rgb(255, 85, 0);")

        self.horizontalLayout.addWidget(self.buscar)

        self.limpiar = QPushButton(self.centralwidget)
        self.limpiar.setObjectName(u"limpiar")
        self.limpiar.setFont(font1)
        self.limpiar.setStyleSheet(u"color: rgb(0, 85, 127);")

        self.horizontalLayout.addWidget(self.limpiar)

        self.exportar = QPushButton(self.centralwidget)
        self.exportar.setObjectName(u"exportar")
        self.exportar.setFont(font1)
        self.exportar.setStyleSheet(u"color: rgb(0, 170, 127);")

        self.horizontalLayout.addWidget(self.exportar)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)

        Caronte.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Caronte)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1065, 26))
        Caronte.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Caronte)
        self.statusbar.setObjectName(u"statusbar")
        Caronte.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.consecutivo, self.proveedor)
        QWidget.setTabOrder(self.proveedor, self.fecha_desde)
        QWidget.setTabOrder(self.fecha_desde, self.fecha_hasta)
        QWidget.setTabOrder(self.fecha_hasta, self.buscar)
        QWidget.setTabOrder(self.buscar, self.limpiar)
        QWidget.setTabOrder(self.limpiar, self.exportar)
        QWidget.setTabOrder(self.exportar, self.tableWidget)

        self.retranslateUi(Caronte)

        QMetaObject.connectSlotsByName(Caronte)
    # setupUi

    def retranslateUi(self, Caronte):
        Caronte.setWindowTitle(QCoreApplication.translate(
            "Caronte", u"NICO: Descarga de Documentos Electrónicos por Correo v0.1", None))
        self.label_2.setText(QCoreApplication.translate(
            "Caronte", u"Proveedor", None))
        self.label_3.setText(
            QCoreApplication.translate("Caronte", u"Desde", None))
        self.label_4.setText(
            QCoreApplication.translate("Caronte", u"Hasta", None))
        self.label.setText(QCoreApplication.translate(
            "Caronte", u"N\u00famero", None))
        self.buscar.setText(QCoreApplication.translate(
            "Caronte", u"Buscar", None))
        self.limpiar.setText(QCoreApplication.translate(
            "Caronte", u"Limpiar", None))
        self.exportar.setText(QCoreApplication.translate(
            "Caronte", u"Exportar", None))
    # retranslateUi
