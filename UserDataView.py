# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_data.ui'
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


class Ui_UserData(object):
    def setupUi(self, UserData):
        if UserData.objectName():
            UserData.setObjectName(u"UserData")
        UserData.setWindowModality(Qt.ApplicationModal)
        UserData.resize(960, 280)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(UserData.sizePolicy().hasHeightForWidth())
        UserData.setSizePolicy(sizePolicy)
        UserData.setMinimumSize(QSize(960, 280))
        UserData.setMaximumSize(QSize(960, 280))
        self.verticalLayout = QVBoxLayout(UserData)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.save_button = QPushButton(UserData)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setMinimumSize(QSize(100, 50))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.save_button.setFont(font)
        self.save_button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 0);")

        self.horizontalLayout_2.addWidget(self.save_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.close_button = QPushButton(UserData)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setMinimumSize(QSize(100, 50))
        self.close_button.setFont(font)
        self.close_button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(227, 0, 0);")

        self.horizontalLayout_2.addWidget(self.close_button)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.gridLayout.addLayout(self.horizontalLayout_2, 6, 0, 1, 2)

        self.ruta_label = QLabel(UserData)
        self.ruta_label.setObjectName(u"ruta_label")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.ruta_label.setFont(font1)
        self.ruta_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.ruta_label, 2, 0, 1, 1)

        self.name_label = QLabel(UserData)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setFont(font1)
        self.name_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.name_label, 0, 0, 1, 1)

        self.label_3 = QLabel(UserData)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)

        self.correo = QLineEdit(UserData)
        self.correo.setObjectName(u"correo")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.correo.sizePolicy().hasHeightForWidth())
        self.correo.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(10)
        self.correo.setFont(font2)

        self.gridLayout.addWidget(self.correo, 0, 4, 1, 1)

        self.servidor = QLineEdit(UserData)
        self.servidor.setObjectName(u"servidor")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.servidor.sizePolicy().hasHeightForWidth())
        self.servidor.setSizePolicy(sizePolicy2)
        self.servidor.setFont(font2)

        self.gridLayout.addWidget(self.servidor, 2, 4, 1, 1)

        self.id_label = QLabel(UserData)
        self.id_label.setObjectName(u"id_label")
        self.id_label.setFont(font1)
        self.id_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.id_label, 1, 0, 1, 1)

        self.line_2 = QFrame(UserData)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFont(font)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 4, 0, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ubicacion = QLineEdit(UserData)
        self.ubicacion.setObjectName(u"ubicacion")
        self.ubicacion.setFont(font2)

        self.horizontalLayout.addWidget(self.ubicacion)

        self.change_directory_button = QPushButton(UserData)
        self.change_directory_button.setObjectName(u"change_directory_button")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.change_directory_button.setFont(font3)
        self.change_directory_button.setStyleSheet(u"color: rgb(0, 0, 255);")

        self.horizontalLayout.addWidget(self.change_directory_button)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)

        self.cedula = QLineEdit(UserData)
        self.cedula.setObjectName(u"cedula")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.cedula.sizePolicy().hasHeightForWidth())
        self.cedula.setSizePolicy(sizePolicy3)
        self.cedula.setFont(font2)

        self.gridLayout.addWidget(self.cedula, 1, 1, 1, 1)

        self.nombre = QLineEdit(UserData)
        self.nombre.setObjectName(u"nombre")
        sizePolicy3.setHeightForWidth(self.nombre.sizePolicy().hasHeightForWidth())
        self.nombre.setSizePolicy(sizePolicy3)
        self.nombre.setFont(font2)

        self.gridLayout.addWidget(self.nombre, 0, 1, 1, 1)

        self.label_5 = QLabel(UserData)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 2, 3, 1, 1)

        self.clave = QLineEdit(UserData)
        self.clave.setObjectName(u"clave")
        sizePolicy2.setHeightForWidth(self.clave.sizePolicy().hasHeightForWidth())
        self.clave.setSizePolicy(sizePolicy2)
        self.clave.setFont(font2)
        self.clave.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.clave, 1, 4, 1, 1)

        self.line = QFrame(UserData)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 0, 2, 7, 1)

        self.label_4 = QLabel(UserData)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 1, 3, 1, 1)

        self.ruta_label_2 = QLabel(UserData)
        self.ruta_label_2.setObjectName(u"ruta_label_2")
        self.ruta_label_2.setFont(font1)
        self.ruta_label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.ruta_label_2, 3, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.p12 = QLineEdit(UserData)
        self.p12.setObjectName(u"p12")
        self.p12.setFont(font2)

        self.horizontalLayout_3.addWidget(self.p12)

        self.change_p12_button = QPushButton(UserData)
        self.change_p12_button.setObjectName(u"change_p12_button")
        self.change_p12_button.setFont(font3)
        self.change_p12_button.setStyleSheet(u"color: rgb(0, 0, 255);")

        self.horizontalLayout_3.addWidget(self.change_p12_button)


        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 1, 1, 1)

        self.label_7 = QLabel(UserData)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_7, 3, 3, 1, 1)

        self.puerto_entrada = QLineEdit(UserData)
        self.puerto_entrada.setObjectName(u"puerto_entrada")
        sizePolicy2.setHeightForWidth(self.puerto_entrada.sizePolicy().hasHeightForWidth())
        self.puerto_entrada.setSizePolicy(sizePolicy2)
        self.puerto_entrada.setFont(font2)

        self.gridLayout.addWidget(self.puerto_entrada, 3, 4, 1, 1)

        self.label = QLabel(UserData)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 4, 3, 1, 1)

        self.puerto_salida = QLineEdit(UserData)
        self.puerto_salida.setObjectName(u"puerto_salida")
        sizePolicy2.setHeightForWidth(self.puerto_salida.sizePolicy().hasHeightForWidth())
        self.puerto_salida.setSizePolicy(sizePolicy2)
        self.puerto_salida.setFont(font2)

        self.gridLayout.addWidget(self.puerto_salida, 4, 4, 1, 1)

        self.ruta_label_3 = QLabel(UserData)
        self.ruta_label_3.setObjectName(u"ruta_label_3")
        self.ruta_label_3.setFont(font1)
        self.ruta_label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.ruta_label_3, 5, 3, 1, 1)

        self.pin = QLineEdit(UserData)
        self.pin.setObjectName(u"pin")
        sizePolicy2.setHeightForWidth(self.pin.sizePolicy().hasHeightForWidth())
        self.pin.setSizePolicy(sizePolicy2)
        self.pin.setFont(font2)
        self.pin.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.pin, 5, 4, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        QWidget.setTabOrder(self.nombre, self.cedula)
        QWidget.setTabOrder(self.cedula, self.ubicacion)
        QWidget.setTabOrder(self.ubicacion, self.change_directory_button)
        QWidget.setTabOrder(self.change_directory_button, self.p12)
        QWidget.setTabOrder(self.p12, self.change_p12_button)
        QWidget.setTabOrder(self.change_p12_button, self.correo)
        QWidget.setTabOrder(self.correo, self.clave)
        QWidget.setTabOrder(self.clave, self.servidor)
        QWidget.setTabOrder(self.servidor, self.puerto_entrada)
        QWidget.setTabOrder(self.puerto_entrada, self.puerto_salida)
        QWidget.setTabOrder(self.puerto_salida, self.pin)
        QWidget.setTabOrder(self.pin, self.save_button)
        QWidget.setTabOrder(self.save_button, self.close_button)

        self.retranslateUi(UserData)

        QMetaObject.connectSlotsByName(UserData)
    # setupUi

    def retranslateUi(self, UserData):
        UserData.setWindowTitle(QCoreApplication.translate("UserData", u"Datos del Usuario", None))
        self.save_button.setText(QCoreApplication.translate("UserData", u"GUARDAR", None))
        self.close_button.setText(QCoreApplication.translate("UserData", u"CANCELAR", None))
        self.ruta_label.setText(QCoreApplication.translate("UserData", u"Carpeta:", None))
        self.name_label.setText(QCoreApplication.translate("UserData", u"Nombre:", None))
        self.label_3.setText(QCoreApplication.translate("UserData", u"Correo:", None))
        self.id_label.setText(QCoreApplication.translate("UserData", u"C\u00e9dula:", None))
        self.change_directory_button.setText(QCoreApplication.translate("UserData", u"Cambiar", None))
        self.label_5.setText(QCoreApplication.translate("UserData", u"Servidor:", None))
        self.label_4.setText(QCoreApplication.translate("UserData", u"Contrase\u00f1a:", None))
        self.ruta_label_2.setText(QCoreApplication.translate("UserData", u"P12:", None))
        self.change_p12_button.setText(QCoreApplication.translate("UserData", u"Cambiar", None))
        self.label_7.setText(QCoreApplication.translate("UserData", u"Puerto Entrada:", None))
        self.label.setText(QCoreApplication.translate("UserData", u"Puerto Salida:", None))
        self.ruta_label_3.setText(QCoreApplication.translate("UserData", u"PIN:", None))
    # retranslateUi

