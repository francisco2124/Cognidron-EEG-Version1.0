# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editParametros.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import vistas.images

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(445, 245)
        Dialog.setMinimumSize(QtCore.QSize(434, 245))
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(100, 90, 281, 22))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 81, 21))
        self.label_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 140, 281, 22))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 81, 21))
        self.label_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(0, 0, 611, 271))
        self.label_10.setMinimumSize(QtCore.QSize(100, 100))
        self.label_10.setStyleSheet("background-color: rgb(116, 147, 198);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.frame_4 = QtWidgets.QFrame(Dialog)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 601, 51))
        self.frame_4.setStyleSheet("background-color: rgb(200, 198, 223);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        self.label_5.setGeometry(QtCore.QRect(150, 50, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("\n"
"font: 75 19pt \"Times New Roman\";")
        self.label_5.setObjectName("label_5")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setGeometry(QtCore.QRect(140, 90, 621, 10))
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 14))
        self.frame_5.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(214, 225, 229), stop:1 rgba(109, 130, 198));\n"
"")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("\n"
"font: 75 19pt \"Times New Roman\";")
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setGeometry(QtCore.QRect(380, 0, 51, 41))
        self.label.setStyleSheet("image: url(:/newPrefix/wifi.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.frame_6 = QtWidgets.QFrame(Dialog)
        self.frame_6.setGeometry(QtCore.QRect(0, 50, 621, 8))
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 8))
        self.frame_6.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(214, 225, 229), stop:1 rgba(109, 130, 198));\n"
"")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(180, 190, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(180, 255, 199);\n"
"background-color: rgb(200, 198, 223);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_10.raise_()
        self.lineEdit.raise_()
        self.label_2.raise_()
        self.lineEdit_2.raise_()
        self.label_3.raise_()
        self.frame_4.raise_()
        self.frame_6.raise_()
        self.pushButton_4.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Actualizar Parametros"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Ingresa client ID"))
        self.label_2.setText(_translate("Dialog", "Cliente Id:"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Ingresa secret id"))
        self.label_3.setText(_translate("Dialog", "Secret Id:"))
        self.label_5.setText(_translate("Dialog", "Cambiar Contraseña"))
        self.label_4.setText(_translate("Dialog", "Configuración de parámetros (Emotiv Epoc +)"))
        self.pushButton_4.setText(_translate("Dialog", "Actualizar"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

