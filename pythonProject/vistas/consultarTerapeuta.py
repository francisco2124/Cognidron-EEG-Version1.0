# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'consultarTerapeuta.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import vistas.images

class Ui_Consultar_Terapeuta(object):
    def setupUi(self, Consultar_Terapeuta):
        Consultar_Terapeuta.setObjectName("Consultar_Terapeuta")
        Consultar_Terapeuta.resize(675, 683)
        Consultar_Terapeuta.setMinimumSize(QtCore.QSize(674, 683))
        self.btnEliminar = QtWidgets.QPushButton(Consultar_Terapeuta)
        self.btnEliminar.setGeometry(QtCore.QRect(480, 180, 71, 28))
        self.btnEliminar.setObjectName("btnEliminar")
        self.btnConsultar = QtWidgets.QPushButton(Consultar_Terapeuta)
        self.btnConsultar.setGeometry(QtCore.QRect(300, 180, 71, 28))
        self.btnConsultar.setObjectName("btnConsultar")
        self.btnModificar = QtWidgets.QPushButton(Consultar_Terapeuta)
        self.btnModificar.setGeometry(QtCore.QRect(390, 180, 71, 28))
        self.btnModificar.setObjectName("btnModificar")
        self.label_2 = QtWidgets.QLabel(Consultar_Terapeuta)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(Consultar_Terapeuta)
        self.frame.setGeometry(QtCore.QRect(0, 0, 681, 81))
        self.frame.setStyleSheet("background-color: rgb(200, 198, 223);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(0, 10, 481, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("\n"
"font: 75 19pt \"Times New Roman\";")
        self.label_3.setObjectName("label_3")
        self.label_23 = QtWidgets.QLabel(self.frame)
        self.label_23.setGeometry(QtCore.QRect(560, 0, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("image: url(:/newPrefix/terapeuta.png);")
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.label = QtWidgets.QLabel(Consultar_Terapeuta)
        self.label.setGeometry(QtCore.QRect(0, 80, 681, 631))
        self.label.setMinimumSize(QtCore.QSize(10, 10))
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(210, 220, 220), stop:1 rgba(100, 130, 190));\n"
"\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(Consultar_Terapeuta)
        self.frame_2.setGeometry(QtCore.QRect(0, 80, 681, 12))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 14))
        self.frame_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(214, 225, 229), stop:1 rgba(109, 130, 198));\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.btnBuscarbaciente = QtWidgets.QPushButton(Consultar_Terapeuta)
        self.btnBuscarbaciente.setGeometry(QtCore.QRect(150, 180, 31, 31))
        self.btnBuscarbaciente.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBuscarbaciente.setIcon(icon)
        self.btnBuscarbaciente.setObjectName("btnBuscarbaciente")
        self.cbfiltrar = QtWidgets.QComboBox(Consultar_Terapeuta)
        self.cbfiltrar.setGeometry(QtCore.QRect(10, 180, 131, 31))
        self.cbfiltrar.setObjectName("cbfiltrar")
        self.cbfiltrar.addItem("")
        self.cbfiltrar.addItem("")
        self.tableView_2 = QtWidgets.QTableWidget(Consultar_Terapeuta)
        self.tableView_2.setGeometry(QtCore.QRect(30, 250, 621, 401))
        self.tableView_2.setMinimumSize(QtCore.QSize(200, 200))
        self.tableView_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableView_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView_2.setDragEnabled(False)
        self.tableView_2.setRowCount(0)
        self.tableView_2.setColumnCount(5)
        self.tableView_2.setObjectName("tableView_2")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableView_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(85, 255, 127))
        self.tableView_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 248, 53))
        self.tableView_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 170, 127))
        self.tableView_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 170, 0))
        self.tableView_2.setHorizontalHeaderItem(4, item)
        self.btnRefrescar = QtWidgets.QPushButton(Consultar_Terapeuta)
        self.btnRefrescar.setGeometry(QtCore.QRect(570, 180, 71, 28))
        self.btnRefrescar.setObjectName("btnRefrescar")
        self.label.raise_()
        self.btnEliminar.raise_()
        self.btnConsultar.raise_()
        self.btnModificar.raise_()
        self.label_2.raise_()
        self.frame.raise_()
        self.frame_2.raise_()
        self.btnBuscarbaciente.raise_()
        self.cbfiltrar.raise_()
        self.tableView_2.raise_()
        self.btnRefrescar.raise_()

        self.retranslateUi(Consultar_Terapeuta)
        QtCore.QMetaObject.connectSlotsByName(Consultar_Terapeuta)

    def retranslateUi(self, Consultar_Terapeuta):
        _translate = QtCore.QCoreApplication.translate
        Consultar_Terapeuta.setWindowTitle(_translate("Consultar_Terapeuta", "Gestionar terapeuta"))
        self.btnEliminar.setText(_translate("Consultar_Terapeuta", "Eliminar"))
        self.btnConsultar.setText(_translate("Consultar_Terapeuta", "Consultar"))
        self.btnModificar.setText(_translate("Consultar_Terapeuta", "Modificar"))
        self.label_2.setText(_translate("Consultar_Terapeuta", "Buscar terapeuta: "))
        self.label_3.setText(_translate("Consultar_Terapeuta", "Gestionar terapeutas"))
        self.cbfiltrar.setItemText(0, _translate("Consultar_Terapeuta", "Paciente"))
        self.cbfiltrar.setItemText(1, _translate("Consultar_Terapeuta", "Terapeuta"))
        item = self.tableView_2.horizontalHeaderItem(0)
        item.setText(_translate("Consultar_Terapeuta", "Usuario"))
        item = self.tableView_2.horizontalHeaderItem(1)
        item.setText(_translate("Consultar_Terapeuta", "Nombre"))
        item = self.tableView_2.horizontalHeaderItem(2)
        item.setText(_translate("Consultar_Terapeuta", "Paterno"))
        item = self.tableView_2.horizontalHeaderItem(3)
        item.setText(_translate("Consultar_Terapeuta", "Materno"))
        item = self.tableView_2.horizontalHeaderItem(4)
        item.setText(_translate("Consultar_Terapeuta", "Contacto"))
        self.btnRefrescar.setText(_translate("Consultar_Terapeuta", "Refrescar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Consultar_Terapeuta = QtWidgets.QDialog()
    ui = Ui_Consultar_Terapeuta()
    ui.setupUi(Consultar_Terapeuta)
    Consultar_Terapeuta.show()
    sys.exit(app.exec_())

