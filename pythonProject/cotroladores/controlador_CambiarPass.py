from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from vistas.cambiarPass import Ui_cambiarPass
from PyQt5.QtGui import QIntValidator

from modelos.ModeloTerapeuta import Modelo_Terapeuta


#En esta clase se inserta codigo que permita a la vista realizar distintos comportamientos sin modificar el archivo principal de la vista



class Controlador_CambiarPass(QtWidgets.QMainWindow):

    def __init__(self, idTerapeuta):
        super().__init__()
        print("soy la vista de consultar terapeutas")
        self.ui= Ui_cambiarPass()
        self.ui.setupUi(self)
        self.idTerapeuta = idTerapeuta
        self.modelo = Modelo_Terapeuta()
        self.InicializarGui()


    def InicializarGui(self):



        self.ui.btnRegistrar_2.clicked.connect(self.cambiarPass)
        self.ui.btnVerPas_3.pressed.connect(self.visualizarPass)
        self.ui.btnVerPas_3.released.connect(self.ocultarPass)
        self.ui.btnVerPas_4.pressed.connect(self.visualizarPass2)
        self.ui.btnVerPas_4.released.connect(self.ocultarPass2)



    def visualizarPass(self):

        self.ui.lePassword_2.setEchoMode(QtWidgets.QLineEdit.Normal)

    def ocultarPass(self):

        self.ui.lePassword_2.setEchoMode(QtWidgets.QLineEdit.Password)
    def visualizarPass2(self):

        self.ui.leCofirnarPassword_2.setEchoMode(QtWidgets.QLineEdit.Normal)

    def ocultarPass2(self):

        self.ui.leCofirnarPassword_2.setEchoMode(QtWidgets.QLineEdit.Password)

    def cambiarPass(self):
        def validrSiesNum(cadena):

            try:
                int(cadena)
                return False
            except ValueError:
                return True
        password = self.ui.lePassword_2.text()
        confirPaswword = self.ui.leCofirnarPassword_2.text()

        if password != confirPaswword:
            Alerta = QMessageBox.information(self, 'Alerta', "Las contraseñas no conciden", QMessageBox.Ok)
        elif len(password) <= 5 or len(password) >10:
            Alerta = QMessageBox.information(self, 'Alerta', "La contraseña debe ser mayor de 5 caracteres y maximo 10 caracteres", QMessageBox.Ok)
        elif validrSiesNum(password) == False:
            Alerta = QMessageBox.information(self, 'Alerta', "La contraseña debe tener almenos una letra", QMessageBox.Ok)
        elif password.isalpha() == True:
            Alerta = QMessageBox.information(self, 'Alerta', "La contraseña debe tener almenos un numero", QMessageBox.Ok)
        elif not any(char.isupper() for char in password):
            Alerta = QMessageBox.information(self, 'Alerta', "La contraseña debe tener almenos una mayuscula", QMessageBox.Ok)
        elif not any(char.islower() for char in password):
            Alerta = QMessageBox.information(self, 'Alerta', "La contraseña debe tener almenos una minuscula", QMessageBox.Ok)
        else:

            resuld = self.modelo.cambiarPass(password, str(self.idTerapeuta))
            print("El id es: "+str(self.idTerapeuta)+"-Y la pass-"+password.strip())

            Alerta = QMessageBox.information(self, 'Confirmacion', "Se ha cambiado la contraseña", QMessageBox.Ok)


