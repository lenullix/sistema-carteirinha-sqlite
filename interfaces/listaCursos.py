# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listaCursos.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_listaCursos(object):
    def setupUi(self, listaCursos):
        listaCursos.setObjectName("listaCursos")
        listaCursos.resize(600, 600)
        listaCursos.setStyleSheet("background-color: rgb(167, 167, 167);")
        self.centralwidget = QtWidgets.QWidget(listaCursos)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 111, 16))
        self.label.setObjectName("label")
        self.tabelaCursos = QtWidgets.QTableWidget(self.centralwidget)
        self.tabelaCursos.setGeometry(QtCore.QRect(10, 60, 581, 391))
        self.tabelaCursos.setObjectName("tabelaCursos")
        self.tabelaCursos.setColumnCount(3)
        self.tabelaCursos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaCursos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaCursos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaCursos.setHorizontalHeaderItem(2, item)
        self.btnVoltar = QtWidgets.QPushButton(self.centralwidget)
        self.btnVoltar.setGeometry(QtCore.QRect(270, 460, 75, 23))
        self.btnVoltar.setObjectName("btnVoltar")
        listaCursos.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(listaCursos)
        self.statusbar.setObjectName("statusbar")
        listaCursos.setStatusBar(self.statusbar)

        self.retranslateUi(listaCursos)
        QtCore.QMetaObject.connectSlotsByName(listaCursos)

    def retranslateUi(self, listaCursos):
        _translate = QtCore.QCoreApplication.translate
        listaCursos.setWindowTitle(_translate("listaCursos", "MainWindow"))
        self.label.setText(_translate("listaCursos", "Lista de Cursos"))
        item = self.tabelaCursos.horizontalHeaderItem(0)
        item.setText(_translate("listaCursos", "New Column"))
        item = self.tabelaCursos.horizontalHeaderItem(1)
        item.setText(_translate("listaCursos", "Código do Curso"))
        item = self.tabelaCursos.horizontalHeaderItem(2)
        item.setText(_translate("listaCursos", "Instituto"))
        self.btnVoltar.setText(_translate("listaCursos", "Voltar"))
