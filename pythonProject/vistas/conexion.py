# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'conexion.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import vistas.images

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(691, 747)
        Dialog.setMinimumSize(QtCore.QSize(691, 747))
#        Dialog.setSizeGripEnabled(True)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 201, 21))
        self.label_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.btnEvaluarConexion = QtWidgets.QPushButton(Dialog)
        self.btnEvaluarConexion.setGeometry(QtCore.QRect(220, 110, 111, 31))
        self.btnEvaluarConexion.setObjectName("btnEvaluarConexion")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(360, 110, 41, 31))
        self.label_4.setStyleSheet("background-color: rgb(41, 226, 69);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.cbAF3 = QtWidgets.QCheckBox(Dialog)
        self.cbAF3.setGeometry(QtCore.QRect(130, 210, 81, 20))
        self.cbAF3.setObjectName("cbAF3")
        self.cbF7 = QtWidgets.QCheckBox(Dialog)
        self.cbF7.setGeometry(QtCore.QRect(430, 170, 81, 20))
        self.cbF7.setObjectName("cbF7")
        self.cbF3 = QtWidgets.QCheckBox(Dialog)
        self.cbF3.setGeometry(QtCore.QRect(30, 170, 81, 20))
        self.cbF3.setObjectName("cbF3")
        self.cbFC5 = QtWidgets.QCheckBox(Dialog)
        self.cbFC5.setGeometry(QtCore.QRect(620, 170, 81, 20))
        self.cbFC5.setObjectName("cbFC5")
        self.cbT7 = QtWidgets.QCheckBox(Dialog)
        self.cbT7.setGeometry(QtCore.QRect(330, 210, 81, 20))
        self.cbT7.setObjectName("cbT7")
        self.cbP7 = QtWidgets.QCheckBox(Dialog)
        self.cbP7.setGeometry(QtCore.QRect(520, 210, 81, 20))
        self.cbP7.setObjectName("cbP7")
        self.cb01 = QtWidgets.QCheckBox(Dialog)
        self.cb01.setGeometry(QtCore.QRect(230, 170, 81, 20))
        self.cb01.setObjectName("cb01")
        self.cb02 = QtWidgets.QCheckBox(Dialog)
        self.cb02.setGeometry(QtCore.QRect(330, 170, 81, 20))
        self.cb02.setObjectName("cb02")
        self.cbP8 = QtWidgets.QCheckBox(Dialog)
        self.cbP8.setGeometry(QtCore.QRect(620, 210, 81, 20))
        self.cbP8.setObjectName("cbP8")
        self.cbT8 = QtWidgets.QCheckBox(Dialog)
        self.cbT8.setGeometry(QtCore.QRect(430, 210, 81, 20))
        self.cbT8.setObjectName("cbT8")
        self.cbFC6 = QtWidgets.QCheckBox(Dialog)
        self.cbFC6.setGeometry(QtCore.QRect(30, 210, 81, 20))
        self.cbFC6.setObjectName("cbFC6")
        self.cbF4 = QtWidgets.QCheckBox(Dialog)
        self.cbF4.setGeometry(QtCore.QRect(130, 170, 81, 20))
        self.cbF4.setObjectName("cbF4")
        self.cbAF4 = QtWidgets.QCheckBox(Dialog)
        self.cbAF4.setGeometry(QtCore.QRect(230, 210, 81, 20))
        self.cbAF4.setObjectName("cbAF4")
        self.cbF8 = QtWidgets.QCheckBox(Dialog)
        self.cbF8.setGeometry(QtCore.QRect(520, 170, 81, 20))
        self.cbF8.setObjectName("cbF8")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(440, 370, 201, 121))
        self.textEdit.setUndoRedoEnabled(False)
        self.textEdit.setAcceptRichText(False)
        self.textEdit.setObjectName("textEdit")
        self.btSelElectrodos = QtWidgets.QPushButton(Dialog)
        self.btSelElectrodos.setGeometry(QtCore.QRect(440, 310, 201, 31))
        self.btSelElectrodos.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.btSelElectrodos.setObjectName("btSelElectrodos")
        self.lbAF3 = QtWidgets.QLabel(Dialog)
        self.lbAF3.setGeometry(QtCore.QRect(150, 400, 51, 31))
        self.lbAF3.setStyleSheet("image: url(:/newPrefix/circuloGris.png);")
        self.lbAF3.setText("")
        self.lbAF3.setObjectName("lbAF3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 280, 411, 471))
        self.label_5.setStyleSheet("image: url(:/newPrefix/img.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 691, 81))
        self.frame.setStyleSheet("background-color: rgb(200, 198, 223);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(0, 10, 601, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("\n"
"font: 75 19pt \"Times New Roman\";")
        self.label_6.setObjectName("label_6")
        self.label_23 = QtWidgets.QLabel(self.frame)
        self.label_23.setGeometry(QtCore.QRect(620, 10, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("image: url(:/newPrefix/wifi.png);")
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(0, 80, 691, 10))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 10))
        self.frame_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(214, 225, 229), stop:1 rgba(109, 130, 198));\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 531, 8))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 8))
        self.frame_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(214, 225, 229), stop:1 rgba(109, 130, 198));\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(0, 90, 701, 691))
        self.label_8.setMinimumSize(QtCore.QSize(480, 610))
        self.label_8.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(210, 220, 220), stop:1 rgba(100, 130, 190));\n"
"\n"
"")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.lbAF4 = QtWidgets.QLabel(Dialog)
        self.lbAF4.setGeometry(QtCore.QRect(220, 400, 61, 31))
        self.lbAF4.setStyleSheet("image: url(:/newPrefix/circuloGris.png);")
        self.lbAF4.setText("")
        self.lbAF4.setObjectName("lbAF4")
        self.lbF3 = QtWidgets.QLabel(Dialog)
        self.lbF3.setGeometry(QtCore.QRect(150, 460, 51, 31))
        self.lbF3.setStyleSheet("image: url(:/newPrefix/circuloGris.png);")
        self.lbF3.setText("")
        self.lbF3.setObjectName("lbF3")
        self.lbF4 = QtWidgets.QLabel(Dialog)
        self.lbF4.setGeometry(QtCore.QRect(220, 460, 61, 31))
        self.lbF4.setStyleSheet("image: url(:/newPrefix/circuloGris.png);")
        self.lbF4.setText("")
        self.lbF4.setObjectName("lbF4")
        self.lbFC6 = QtWidgets.QLabel(Dialog)
        self.lbFC6.setGeometry(QtCore.QRect(270, 460, 41, 41))
        self.lbFC6.setStyleSheet("\n"
"image: url(:/newPrefix/circuloGris.png);")
        self.lbFC6.setText("")
        self.lbFC6.setObjectName("lbFC6")
        self.lb02 = QtWidgets.QLabel(Dialog)
        self.lb02.setGeometry(QtCore.QRect(230, 630, 41, 31))
        self.lb02.setStyleSheet("image: url(:/newPrefix/circuloGris.png);")
        self.lb02.setText("")
        self.lb02.setObjectName("lb02")
        self.lb01 = QtWidgets.QLabel(Dialog)
        self.lb01.setGeometry(QtCore.QRect(160, 630, 41, 31))
        self.lb01.setStyleSheet("image: url(:/newPrefix/circuloGris.png);")
        self.lb01.setText("")
        self.lb01.setObjectName("lb01")
        self.lbP8 = QtWidgets.QLabel(Dialog)
        self.lbP8.setGeometry(QtCore.QRect(260, 580, 51, 31))
        self.lbP8.setStyleSheet("image: url(:/newPrefix/circuloGris.png);")
        self.lbP8.setText("")
        self.lbP8.setObjectName("lbP8")
        self.lbT8 = QtWidgets.QLabel(Dialog)
        self.lbT8.setGeometry(QtCore.QRect(300, 490, 41, 31))
        self.lbT8.setStyleSheet("image: url(:/newPrefix/circuloGris.png);")
        self.lbT8.setText("")
        self.lbT8.setObjectName("lbT8")
        self.lbF8 = QtWidgets.QLabel(Dialog)
        self.lbF8.setGeometry(QtCore.QRect(270, 410, 41, 41))
        self.lbF8.setStyleSheet("image: url(:/newPrefix/circuloGris.png);")
        self.lbF8.setText("")
        self.lbF8.setObjectName("lbF8")
        self.lbT7 = QtWidgets.QLabel(Dialog)
        self.lbT7.setGeometry(QtCore.QRect(80, 490, 51, 31))
        self.lbT7.setStyleSheet("image: url(:/newPrefix/circuloGris.png);")
        self.lbT7.setText("")
        self.lbT7.setObjectName("lbT7")
        self.lbP7 = QtWidgets.QLabel(Dialog)
        self.lbP7.setGeometry(QtCore.QRect(120, 580, 41, 31))
        self.lbP7.setStyleSheet("image: url(:/newPrefix/circuloGris.png);")
        self.lbP7.setText("")
        self.lbP7.setObjectName("lbP7")
        self.lbFC5 = QtWidgets.QLabel(Dialog)
        self.lbFC5.setGeometry(QtCore.QRect(110, 460, 41, 41))
        self.lbFC5.setStyleSheet("image: url(:/newPrefix/circuloGris.png);")
        self.lbFC5.setText("")
        self.lbFC5.setObjectName("lbFC5")
        self.lbF7 = QtWidgets.QLabel(Dialog)
        self.lbF7.setGeometry(QtCore.QRect(110, 410, 41, 41))
        self.lbF7.setStyleSheet("image: url(:/newPrefix/circuloGris.png);")
        self.lbF7.setText("")
        self.lbF7.setObjectName("lbF7")
        self.lbRFIquierdo = QtWidgets.QLabel(Dialog)
        self.lbRFIquierdo.setGeometry(QtCore.QRect(280, 530, 51, 31))
        self.lbRFIquierdo.setStyleSheet("image: url(:/newPrefix/circuloLRRojo.png);")
        self.lbRFIquierdo.setText("")
        self.lbRFIquierdo.setObjectName("lbRFIquierdo")
        self.lbRFIquierdo_2 = QtWidgets.QLabel(Dialog)
        self.lbRFIquierdo_2.setGeometry(QtCore.QRect(90, 530, 61, 31))
        self.lbRFIquierdo_2.setStyleSheet("image: url(:/newPrefix/circuloLRRojo.png);")
        self.lbRFIquierdo_2.setText("")
        self.lbRFIquierdo_2.setObjectName("lbRFIquierdo_2")
        self.label_8.raise_()
        self.label_2.raise_()
        self.btnEvaluarConexion.raise_()
        self.label_4.raise_()
        self.cbAF3.raise_()
        self.cbF7.raise_()
        self.cbF3.raise_()
        self.cbFC5.raise_()
        self.cbT7.raise_()
        self.cbP7.raise_()
        self.cb01.raise_()
        self.cb02.raise_()
        self.cbP8.raise_()
        self.cbT8.raise_()
        self.cbFC6.raise_()
        self.cbF4.raise_()
        self.cbAF4.raise_()
        self.cbF8.raise_()
        self.textEdit.raise_()
        self.btSelElectrodos.raise_()
        self.label_5.raise_()
        self.frame.raise_()
        self.frame_2.raise_()
        self.lbAF3.raise_()
        self.lbAF4.raise_()
        self.lbF3.raise_()
        self.lbF4.raise_()
        self.lbFC6.raise_()
        self.lb02.raise_()
        self.lb01.raise_()
        self.lbP8.raise_()
        self.lbT8.raise_()
        self.lbF8.raise_()
        self.lbT7.raise_()
        self.lbP7.raise_()
        self.lbFC5.raise_()
        self.lbF7.raise_()
        self.lbRFIquierdo.raise_()
        self.lbRFIquierdo_2.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Conexion"))
        self.label_2.setText(_translate("Dialog", "Conexión con Emoti epoc +"))
        self.btnEvaluarConexion.setText(_translate("Dialog", "Evaluar Conexión"))
        self.cbAF3.setText(_translate("Dialog", "AF3"))
        self.cbF7.setText(_translate("Dialog", "F7"))
        self.cbF3.setText(_translate("Dialog", "F3"))
        self.cbFC5.setText(_translate("Dialog", "FC5"))
        self.cbT7.setText(_translate("Dialog", "T7"))
        self.cbP7.setText(_translate("Dialog", "P7"))
        self.cb01.setText(_translate("Dialog", "01"))
        self.cb02.setText(_translate("Dialog", "02"))
        self.cbP8.setText(_translate("Dialog", "P8"))
        self.cbT8.setText(_translate("Dialog", "T8"))
        self.cbFC6.setText(_translate("Dialog", "FC6"))
        self.cbF4.setText(_translate("Dialog", "F4"))
        self.cbAF4.setText(_translate("Dialog", "AF4"))
        self.cbF8.setText(_translate("Dialog", "F8"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hidrata corrrectamente los electrodos y asegurate que la posicion sea la correcta.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btSelElectrodos.setText(_translate("Dialog", "Aplicar Seleccion de electrodos"))
        self.label_6.setText(_translate("Dialog", "Configuración de la conexión (Emotiv Epoc +)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

