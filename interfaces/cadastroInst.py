# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastroInst.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CadInst(object):
    def setupUi(self, CadInst):
        CadInst.setObjectName("CadInst")
        CadInst.resize(588, 468)
        CadInst.setStyleSheet("background-color: rgb(167, 167, 167);")
        self.centralwidget = QtWidgets.QWidget(CadInst)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 31, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 47, 13))
        self.label_4.setObjectName("label_4")
        self.entradaNome = QtWidgets.QLineEdit(self.centralwidget)
        self.entradaNome.setGeometry(QtCore.QRect(90, 40, 261, 20))
        self.entradaNome.setObjectName("entradaNome")
        self.entradaEndereco = QtWidgets.QLineEdit(self.centralwidget)
        self.entradaEndereco.setGeometry(QtCore.QRect(90, 80, 261, 20))
        self.entradaEndereco.setObjectName("entradaEndereco")
        self.entradaCnpj = QtWidgets.QLineEdit(self.centralwidget)
        self.entradaCnpj.setGeometry(QtCore.QRect(90, 120, 261, 20))
        self.entradaCnpj.setObjectName("entradaCnpj")
        self.entradaTelefone = QtWidgets.QLineEdit(self.centralwidget)
        self.entradaTelefone.setGeometry(QtCore.QRect(90, 160, 261, 20))
        self.entradaTelefone.setObjectName("entradaTelefone")
        self.btnSalvar = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalvar.setGeometry(QtCore.QRect(280, 250, 75, 23))
        self.btnSalvar.setObjectName("btnSalvar")
        self.btnVoltar = QtWidgets.QPushButton(self.centralwidget)
        self.btnVoltar.setGeometry(QtCore.QRect(20, 250, 75, 23))
        self.btnVoltar.setObjectName("btnVoltar")
        CadInst.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(CadInst)
        self.statusbar.setObjectName("statusbar")
        CadInst.setStatusBar(self.statusbar)

        self.retranslateUi(CadInst)
        QtCore.QMetaObject.connectSlotsByName(CadInst)

    def retranslateUi(self, CadInst):
        _translate = QtCore.QCoreApplication.translate
        CadInst.setWindowTitle(_translate("CadInst", "Cadastrar Instituto"))
        self.label.setText(_translate("CadInst", "Nome"))
        self.label_2.setText(_translate("CadInst", "Endereço"))
        self.label_3.setText(_translate("CadInst", "CNPJ"))
        self.label_4.setText(_translate("CadInst", "Telefone"))
        self.btnSalvar.setText(_translate("CadInst", "Salvar"))
        self.btnVoltar.setText(_translate("CadInst", "Voltar"))
