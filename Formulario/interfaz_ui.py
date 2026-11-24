
# -*- coding: utf-8 -*-

from PyQt6.QtCore import QCoreApplication, QMetaObject, QRect
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton


class Ui_Form(object):

    def setupUi(self, Form):

        if not Form.objectName():
            Form.setObjectName("Form")

        Form.resize(400, 300)

        self.label = QLabel(Form)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(140, 10, 61, 31))

        self.txtNombre = QLineEdit(Form)
        self.txtNombre.setObjectName("txtNombre")
        self.txtNombre.setGeometry(QRect(120, 60, 113, 22))

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(40, 60, 49, 16))

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(40, 100, 49, 16))

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QRect(40, 140, 49, 16))

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.label_5.setGeometry(QRect(40, 180, 49, 16))

        self.txtApellido = QLineEdit(Form)
        self.txtApellido.setObjectName("txtApellido")
        self.txtApellido.setGeometry(QRect(120, 100, 113, 22))

        self.txtMatricula = QLineEdit(Form)
        self.txtMatricula.setObjectName("txtMatricula")
        self.txtMatricula.setGeometry(QRect(120, 140, 113, 22))

        self.txtTelefono = QLineEdit(Form)
        self.txtTelefono.setObjectName("txtTelefono")
        self.txtTelefono.setGeometry(QRect(120, 180, 113, 22))

        self.btnEnviar = QPushButton(Form)
        self.btnEnviar.setObjectName("btnEnviar")
        self.btnEnviar.setGeometry(QRect(130, 220, 75, 24))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):

        Form.setWindowTitle(
            QCoreApplication.translate("Form", "Form")
        )

        self.label.setText(
            QCoreApplication.translate("Form", "Formulario")
        )

        self.label_2.setText(
            QCoreApplication.translate("Form", "Nombre")
        )

        self.label_3.setText(
            QCoreApplication.translate("Form", "Apellido")
        )

        self.label_4.setText(
            QCoreApplication.translate("Form", "Matricula")
        )

        self.label_5.setText(
            QCoreApplication.translate("Form", "Telefono")
        )

        self.btnEnviar.setText(
            QCoreApplication.translate("Form", "Enviar")
        )
