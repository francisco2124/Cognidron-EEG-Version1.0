# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'terapia.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import  vistas.images

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1204, 709)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 10, 351, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(170, 90, 151, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(380, 80, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(530, 90, 61, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(600, 90, 111, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(360, 170, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(890, 90, 151, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(820, 30, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(560, 30, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.btnEnviarIstruccion = QtWidgets.QPushButton(Dialog)
        self.btnEnviarIstruccion.setGeometry(QtCore.QRect(20, 270, 161, 31))
        self.btnEnviarIstruccion.setObjectName("btnEnviarIstruccion")
        self.btnActivarDrone = QtWidgets.QPushButton(Dialog)
        self.btnActivarDrone.setGeometry(QtCore.QRect(20, 660, 161, 31))
        self.btnActivarDrone.setStyleSheet("background-color: rgb(116, 147, 198);")
        self.btnActivarDrone.setObjectName("btnActivarDrone")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 520, 41, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 520, 41, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(80, 470, 41, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 520, 41, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(80, 570, 41, 28))
        self.pushButton_7.setObjectName("pushButton_7")
        self.btnActivarEmotiv = QtWidgets.QPushButton(Dialog)
        self.btnActivarEmotiv.setGeometry(QtCore.QRect(20, 170, 161, 31))
        self.btnActivarEmotiv.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.btnActivarEmotiv.setObjectName("btnActivarEmotiv")
        self.btnElevarDrone = QtWidgets.QPushButton(Dialog)
        self.btnElevarDrone.setGeometry(QtCore.QRect(20, 420, 161, 31))
        self.btnElevarDrone.setObjectName("btnElevarDrone")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(560, 0, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(480, 120, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(610, 120, 81, 31))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(710, 120, 171, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(710, 0, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.btnResumen = QtWidgets.QPushButton(Dialog)
        self.btnResumen.setGeometry(QtCore.QRect(890, 120, 31, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnResumen.setFont(font)
        self.btnResumen.setObjectName("btnResumen")
        self.btnDetener = QtWidgets.QPushButton(Dialog)
        self.btnDetener.setGeometry(QtCore.QRect(990, 120, 61, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnDetener.setFont(font)
        self.btnDetener.setObjectName("btnDetener")
        self.btnPausar = QtWidgets.QPushButton(Dialog)
        self.btnPausar.setGeometry(QtCore.QRect(940, 120, 31, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnPausar.setFont(font)
        self.btnPausar.setObjectName("btnPausar")
        self.btbCapturarObservaciones = QtWidgets.QPushButton(Dialog)
        self.btbCapturarObservaciones.setGeometry(QtCore.QRect(20, 220, 161, 31))
        self.btbCapturarObservaciones.setObjectName("btbCapturarObservaciones")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(200, 120, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.comboBox_4 = QtWidgets.QComboBox(Dialog)
        self.comboBox_4.setGeometry(QtCore.QRect(330, 120, 121, 31))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.labelComandosMentales = QtWidgets.QLabel(Dialog)
        self.labelComandosMentales.setGeometry(QtCore.QRect(210, 650, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.labelComandosMentales.setFont(font)
        self.labelComandosMentales.setObjectName("labelComandosMentales")
        self.labelEventoDrone = QtWidgets.QLabel(Dialog)
        self.labelEventoDrone.setGeometry(QtCore.QRect(470, 650, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.labelEventoDrone.setFont(font)
        self.labelEventoDrone.setObjectName("labelEventoDrone")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(300, 290, 251, 281))
        self.label_11.setStyleSheet("image: url(:/newPrefix/EjerElevar.png);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(230, 210, 471, 431))
        self.label_12.setStyleSheet("background-color: rgb(162, 175, 188);")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.progressBar_2 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_2.setGeometry(QtCore.QRect(970, 653, 171, 21))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.progressBar_3 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_3.setGeometry(QtCore.QRect(710, 650, 171, 23))
        self.progressBar_3.setProperty("value", 24)
        self.progressBar_3.setObjectName("progressBar_3")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(670, 650, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(910, 650, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(830, 520, 120, 80))
        self.groupBox.setObjectName("groupBox")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 20, 95, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 50, 95, 20))
        self.radioButton_4.setObjectName("radioButton_4")
        self.comboBox_5 = QtWidgets.QComboBox(Dialog)
        self.comboBox_5.setGeometry(QtCore.QRect(830, 610, 121, 21))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.btnResumen_2 = QtWidgets.QPushButton(Dialog)
        self.btnResumen_2.setGeometry(QtCore.QRect(890, 430, 51, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnResumen_2.setFont(font)
        self.btnResumen_2.setObjectName("btnResumen_2")
        self.btnResumen_3 = QtWidgets.QPushButton(Dialog)
        self.btnResumen_3.setGeometry(QtCore.QRect(840, 430, 51, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnResumen_3.setFont(font)
        self.btnResumen_3.setObjectName("btnResumen_3")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(840, 470, 104, 41))
        self.textEdit.setObjectName("textEdit")
        self.progressBar_4 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_4.setGeometry(QtCore.QRect(730, 220, 81, 331))
        self.progressBar_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar_4.setStyleSheet("QProgressBar::chunk \"\n"
"                                            \"{\"\n"
"                                            \"background-color: orange;\"\n"
"                                            \"}\n"
"\n"
"")
        self.progressBar_4.setProperty("value", 24)
        self.progressBar_4.setTextVisible(True)
        self.progressBar_4.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_4.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar_4.setObjectName("progressBar_4")
        self.label_12.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.comboBox.raise_()
        self.label_3.raise_()
        self.radioButton.raise_()
        self.radioButton_2.raise_()
        self.label_4.raise_()
        self.comboBox_2.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.btnEnviarIstruccion.raise_()
        self.btnActivarDrone.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.btnActivarEmotiv.raise_()
        self.btnElevarDrone.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.comboBox_3.raise_()
        self.progressBar.raise_()
        self.label_9.raise_()
        self.btnResumen.raise_()
        self.btnDetener.raise_()
        self.btnPausar.raise_()
        self.btbCapturarObservaciones.raise_()
        self.label_10.raise_()
        self.comboBox_4.raise_()
        self.labelComandosMentales.raise_()
        self.labelEventoDrone.raise_()
        self.label_11.raise_()
        self.progressBar_2.raise_()
        self.progressBar_3.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.groupBox.raise_()
        self.comboBox_5.raise_()
        self.btnResumen_2.raise_()
        self.btnResumen_3.raise_()
        self.textEdit.raise_()
        self.progressBar_4.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Terapia"))
        self.label.setText(_translate("Dialog", "Inicia una Terapia "))
        self.label_2.setText(_translate("Dialog", "Seleciona un paciente:"))
        self.comboBox.setItemText(0, _translate("Dialog", "Paciente x"))
        self.comboBox.setItemText(1, _translate("Dialog", "Paciente y"))
        self.comboBox.setItemText(2, _translate("Dialog", "Paciente z"))
        self.label_3.setText(_translate("Dialog", "Tipo de Tratamiento:"))
        self.radioButton.setText(_translate("Dialog", "Libre"))
        self.radioButton_2.setText(_translate("Dialog", "NeuroFeedback"))
        self.label_4.setText(_translate("Dialog", "Seleciona un ejercicio:"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Elevar drone"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Decender Drone"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "Modo libre"))
        self.label_5.setText(_translate("Dialog", "Martes 17 de Noviembre del 2020"))
        self.label_6.setText(_translate("Dialog", "Terapeuta: nombre xxxxxxxxxxx"))
        self.btnEnviarIstruccion.setText(_translate("Dialog", "Mostrar Istrucciones"))
        self.btnActivarDrone.setText(_translate("Dialog", "Obtener Control"))
        self.pushButton_3.setText(_translate("Dialog", "_"))
        self.pushButton_4.setText(_translate("Dialog", "<"))
        self.pushButton_5.setText(_translate("Dialog", "^"))
        self.pushButton_6.setText(_translate("Dialog", ">"))
        self.pushButton_7.setText(_translate("Dialog", "v"))
        self.btnActivarEmotiv.setText(_translate("Dialog", "Activar Emotiv"))
        self.btnElevarDrone.setText(_translate("Dialog", "Elevar Drone"))
        self.label_7.setText(_translate("Dialog", "Numero de terapia: "))
        self.label_8.setText(_translate("Dialog", "Establecer tiempo: "))
        self.comboBox_3.setItemText(0, _translate("Dialog", "1 Minuto"))
        self.comboBox_3.setItemText(1, _translate("Dialog", "2 Minuto"))
        self.comboBox_3.setItemText(2, _translate("Dialog", "3 Minuto"))
        self.comboBox_3.setItemText(3, _translate("Dialog", "4 Minutom"))
        self.comboBox_3.setItemText(4, _translate("Dialog", "5 Minuto"))
        self.label_9.setText(_translate("Dialog", "X_1"))
        self.btnResumen.setText(_translate("Dialog", ">"))
        self.btnDetener.setText(_translate("Dialog", "Detener"))
        self.btnPausar.setText(_translate("Dialog", "l l"))
        self.btbCapturarObservaciones.setText(_translate("Dialog", "Capturar observaciones"))
        self.label_10.setText(_translate("Dialog", "Seleciona un Perfil:"))
        self.comboBox_4.setItemText(0, _translate("Dialog", "Monica"))
        self.comboBox_4.setItemText(1, _translate("Dialog", "Francisco"))
        self.comboBox_4.setItemText(2, _translate("Dialog", "Monica 2"))
        self.comboBox_4.setItemText(3, _translate("Dialog", "Heiler"))
        self.comboBox_4.setItemText(4, _translate("Dialog", "Antonio"))
        self.labelComandosMentales.setText(_translate("Dialog", "Estado de los comandos mentales"))
        self.labelEventoDrone.setText(_translate("Dialog", "Evento del Drone"))
        self.label_13.setText(_translate("Dialog", "BCI"))
        self.label_14.setText(_translate("Dialog", "Robot"))
        self.groupBox.setTitle(_translate("Dialog", "Tipo de Ejercicio"))
        self.radioButton_3.setText(_translate("Dialog", "Inivitorio"))
        self.radioButton_4.setText(_translate("Dialog", "Exivitorio"))
        self.comboBox_5.setItemText(0, _translate("Dialog", "Beta Low"))
        self.comboBox_5.setItemText(1, _translate("Dialog", "Theta"))
        self.comboBox_5.setItemText(2, _translate("Dialog", "Beta High"))
        self.comboBox_5.setItemText(3, _translate("Dialog", "Gama"))
        self.comboBox_5.setItemText(4, _translate("Dialog", "Alfa"))
        self.btnResumen_2.setText(_translate("Dialog", ">"))
        self.btnResumen_3.setText(_translate("Dialog", "<"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

