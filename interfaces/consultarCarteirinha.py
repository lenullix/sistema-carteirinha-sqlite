# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'consultarCarteirinha.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_consultarCarteirinha(object):
    def setupUi(self, consultarCarteirinha):
        consultarCarteirinha.setObjectName("consultarCarteirinha")
        consultarCarteirinha.resize(600, 600)
        consultarCarteirinha.setStyleSheet("background-color: rgb(167, 167, 167);")
        self.centralwidget = QtWidgets.QWidget(consultarCarteirinha)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 191, 16))
        self.label.setObjectName("label")
        self.entradaCPF = QtWidgets.QLineEdit(self.centralwidget)
        self.entradaCPF.setGeometry(QtCore.QRect(240, 20, 251, 20))
        self.entradaCPF.setObjectName("entradaCPF")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(60, 180, 461, 191))
        self.widget.setStyleSheet("\n"
"background-color: rgb(209, 209, 209);")
        self.widget.setObjectName("widget")
        self.labelNome = QtWidgets.QLabel(self.widget)
        self.labelNome.setGeometry(QtCore.QRect(40, 50, 401, 21))
        self.labelNome.setObjectName("labelNome")
        self.labelCurso = QtWidgets.QLabel(self.widget)
        self.labelCurso.setGeometry(QtCore.QRect(40, 100, 221, 16))
        self.labelCurso.setObjectName("labelCurso")
        self.labelAno = QtWidgets.QLabel(self.widget)
        self.labelAno.setGeometry(QtCore.QRect(280, 100, 161, 16))
        self.labelAno.setObjectName("labelAno")
        self.labelCodigo = QtWidgets.QLabel(self.widget)
        self.labelCodigo.setGeometry(QtCore.QRect(40, 150, 221, 16))
        self.labelCodigo.setObjectName("labelCodigo")
        self.labelValidade = QtWidgets.QLabel(self.widget)
        self.labelValidade.setGeometry(QtCore.QRect(280, 150, 161, 16))
        self.labelValidade.setObjectName("labelValidade")
        self.labelInstituto = QtWidgets.QLabel(self.widget)
        self.labelInstituto.setGeometry(QtCore.QRect(110, 10, 231, 31))
        self.labelInstituto.setAlignment(QtCore.Qt.AlignCenter)
        self.labelInstituto.setObjectName("labelInstituto")
        self.btnConsultar = QtWidgets.QPushButton(self.centralwidget)
        self.btnConsultar.setGeometry(QtCore.QRect(240, 60, 75, 23))
        self.btnConsultar.setObjectName("btnConsultar")
        self.btnVoltar = QtWidgets.QPushButton(self.centralwidget)
        self.btnVoltar.setGeometry(QtCore.QRect(240, 390, 75, 23))
        self.btnVoltar.setObjectName("btnVoltar")
        self.labelMensagem = QtWidgets.QLabel(self.centralwidget)
        self.labelMensagem.setGeometry(QtCore.QRect(130, 120, 361, 20))
        self.labelMensagem.setText("")
        self.labelMensagem.setObjectName("labelMensagem")
        consultarCarteirinha.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(consultarCarteirinha)
        self.statusbar.setObjectName("statusbar")
        consultarCarteirinha.setStatusBar(self.statusbar)

        self.retranslateUi(consultarCarteirinha)
        QtCore.QMetaObject.connectSlotsByName(consultarCarteirinha)

    def retranslateUi(self, consultarCarteirinha):
        _translate = QtCore.QCoreApplication.translate
        consultarCarteirinha.setWindowTitle(_translate("consultarCarteirinha", "MainWindow"))
        self.label.setText(_translate("consultarCarteirinha", "CPF do aluno ou código da carteirinha:"))
        self.labelNome.setText(_translate("consultarCarteirinha", "Nome"))
        self.labelCurso.setText(_translate("consultarCarteirinha", "Curso"))
        self.labelAno.setText(_translate("consultarCarteirinha", "Ano Inicio"))
        self.labelCodigo.setText(_translate("consultarCarteirinha", "Codigo Carteirinha"))
        self.labelValidade.setText(_translate("consultarCarteirinha", "Validade"))
        self.labelInstituto.setText(_translate("consultarCarteirinha", "Inst"))
        self.btnConsultar.setText(_translate("consultarCarteirinha", "Consultar"))
        self.btnVoltar.setText(_translate("consultarCarteirinha", "Voltar"))