from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from vistas.recuperarCredenciales import Ui_Dialog
from PyQt5.QtGui import QIntValidator
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from smtplib import SMTP
from email.mime.text import MIMEText

from modelos.ModeloTerapeuta import Modelo_Terapeuta


#En esta clase se inserta codigo que permita a la vista realizar distintos comportamientos sin modificar el archivo principal de la vista



class Controlador_RecuperarCredenciales(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        print("soy la vista de recuperarCredenciales")
        self.ui= Ui_Dialog()
        self.ui.setupUi(self)
        self.modelo = Modelo_Terapeuta()
        self.InicializarGui()


    def InicializarGui(self):

        self.ui.btnRecuperar.clicked.connect(self.recuperarCredenciales)


    def recuperarCredenciales(self):

        correo = self.ui.etCorreo.text()
        print("el correo es: "+str(correo))
        try:
            datos = self.modelo.recuperarCredenciales(correo)
            print("Los datos son: "+str(datos))

            if str(datos) == "()":
                print("No se recupero nada")
                self.ui.labelImagen.setStyleSheet("image: url(:/newPrefix/block.png);")
                self.ui.labelValidarCorreo.setText("El correo ingresado no esta vinculado a ningun terapeuta")
                self.ui.labelInstruccion.setText("Intenta ingresar un correo valido.....")
            else:
                print("Recuperacion exitosa")

                datosF =datos[0]
                mensaje = MIMEMultipart("plain")
                mensaje["From"]="cognidroneeg@gmail.com"
                mensaje["To"] = correo
                mensaje["Subject"] = "CogniDron-EEG. Recuperación de credenciales"
                body = "Hola soy el asistente del sistema CogniDron-EEG. Tu usuario es: -"+str(datosF[0])+"- y tu contraseña es: -"+\
                       str(datosF[1])+"- .Muchas gracias por preferir el sistema CogniDron-EEG :)"
                mensaje.attach(MIMEText(body, 'plain'))
                smtp = SMTP("smtp.gmail.com")
                smtp.starttls()
                smtp.login("cognidroneeg@gmail.com","eegcognidron")
                smtp.sendmail("cognidroneeg@gmail.com",correo,mensaje.as_string())
                print("Envie el correo ;)")

                self.ui.labelImagen.setStyleSheet("image: url(:/newPrefix/good.png);")
                self.ui.labelValidarCorreo.setText("El correo electrónico se ha validado satisfactoriamente")
                self.ui.labelInstruccion.setText("Recibiras un correo electrónico con tus credenciales")
        except:

            Alerta = QMessageBox.information(self, 'Confirmacion', "No se ha podido encontar un usuario vinculado al correo ingresado", QMessageBox.Ok)
            self.ui.labelImagen.setStyleSheet("image: url(:/newPrefix/block.png);")
            self.ui.labelValidarCorreo.setText("El correo ingresado no esta vinculado a ningun terapeuta")
            self.ui.labelInstruccion.setText("Intenta ingresar un correo valido.....")






