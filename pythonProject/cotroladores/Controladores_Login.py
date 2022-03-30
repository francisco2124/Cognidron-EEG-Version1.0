from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox


from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from smtplib import SMTP
from email.mime.text import MIMEText

from vistas.login import Ui_Dialog
from PyQt5.QtGui import QIntValidator
from cotroladores.Controlador_PrincipalCognidron import Controlador_PrincipalCognidron

from modelos.ModeloTerapeuta import Modelo_Terapeuta


#En esta clase se inserta codigo que permita a la vista realizar distintos comportamientos sin modificar el archivo principal de la vista



class Controlador_Login(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui= Ui_Dialog()
        self.modelo = Modelo_Terapeuta()
        #self.controladorCognidron = controlaorCognidron
        self.ui.setupUi(self)
        self.InicializarGui()
        self.user = "Hola"


    def InicializarGui(self):

        self.ui.btnIngresar.clicked.connect(self.abrir)
        self.ui.btnVerPas.pressed.connect(self.visualizarPass)
        self.ui.btnVerPas.released.connect(self.ocultarPass)


    def abrir(self):
        usuario = "Francisco"
        self.controladorCognidron = Controlador_PrincipalCognidron(usuario)
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
                user = password
                self.controladorCognidron = Controlador_PrincipalCognidron(user)
                self.controladorCognidron.show()
                self.close()
            else:
                Alerta = QMessageBox.information(self, 'Alerta', "Usuario o contraseña incorectos", QMessageBox.Ok)

    def recuperarPasword(self):
        try:
            mensaje = MIMEMultipart("plain")
            mensaje["From"]="cognidroneeg@gmail.com"
            mensaje["To"] = "ingcervantes@hotmail.com"
            mensaje["Subject"] = "Correo de prueba >:)"
            body = "Hola Mundo"
            mensaje.attach(MIMEText(body, 'plain'))
            smtp = SMTP("smtp.gmail.com")
            smtp.starttls()
            smtp.login("cognidroneeg@gmail.com","eegcognidron")
            smtp.sendmail("vasito352@gmail.com","ingcervantes@hotmail.com",mensaje.as_string())
            print("Envie el correo :O")
        except:
            pass