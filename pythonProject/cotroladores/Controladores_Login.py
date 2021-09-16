from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from vistas.login import Ui_Dialog
from PyQt5.QtGui import QIntValidator

from modelos.ModeloTerapeuta import Modelo_Terapeuta


#En esta clase se inserta codigo que permita a la vista realizar distintos comportamientos sin modificar el archivo principal de la vista



class Controlador_Login(QtWidgets.QMainWindow):

    def __init__(self, controlaorCognidron):
        super().__init__()

        self.ui= Ui_Dialog()
        self.modelo = Modelo_Terapeuta()
        self.controladorCognidron = controlaorCognidron
        self.ui.setupUi(self)
        self.InicializarGui()


    def InicializarGui(self):

        self.ui.btnIngresar.clicked.connect(self.abrir)
        self.ui.btnVerPas.pressed.connect(self.visualizarPass)
        self.ui.btnVerPas.released.connect(self.ocultarPass)


    def abrir(self):
        self.controladorCognidron.show()
        self.close()

    def visualizarPass(self):

        self.ui.etPass.setEchoMode(QtWidgets.QLineEdit.Normal)

    def ocultarPass(self):

        self.ui.etPass.setEchoMode(QtWidgets.QLineEdit.Password)

    def validar(self):


        if len(self.ui.etUser.text()) == 0:

            Alerta = QMessageBox.information(self, 'Alerta', "No has ingresado el nombre del usuario", QMessageBox.Ok)

        elif len(self.ui.etUser.text()) >= 1 and self.ui.etUser.text().isalnum() == False:
            Alerta = QMessageBox.information(self, 'Alerta', "El campo usuario solo admite entradas alphanumericas", QMessageBox.Ok)

        elif len(self.ui.etPass.text()) == 0:
            Alerta = QMessageBox.information(self, 'Alerta', "No has ingresado la contraseña", QMessageBox.Ok)

        elif len(self.ui.etPass.text()) >= 1 and self.ui.etPass.text().isalnum() == False:

            Alerta = QMessageBox.information(self, 'Alerta', "El campo contraseña solo admite entradas alphanumericas", QMessageBox.Ok)
        else:
            usuario = self.ui.etPass.text()
            password = self.ui.etUser.text()
            resuld = self.modelo.validarLogin(usuario,password)

            if resuld == True:
                self.controladorCognidron.show()
                self.close()
            else:
                Alerta = QMessageBox.information(self, 'Alerta', "Usuario o contraseña incorectos", QMessageBox.Ok)



