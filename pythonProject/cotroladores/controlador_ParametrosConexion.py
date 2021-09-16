from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from vistas.editParametros import Ui_Dialog
from PyQt5.QtGui import QIntValidator



from modelos.modeloParametros import Modelo_conexion


#En esta clase se inserta codigo que permita a la vista realizar distintos comportamientos sin modificar el archivo principal de la vista



class Controlador_parametros(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui= Ui_Dialog()
        self.modelo = Modelo_conexion()
        self.ui.setupUi(self)
        self.InicializarGui()
        self.cargarParametris()


    def InicializarGui(self):
        self.ui.pushButton_4.clicked.connect(self.editarParametros)

    def cargarParametris(self):

        datos = self.modelo.cargarDatos()

        ListaDatos = datos[0]

        print("Los datos son los siguientes: ")
        print(str(datos))

        self.ui.lineEdit.setPlaceholderText(str(ListaDatos[0]).strip())
        self.ui.lineEdit_2.setPlaceholderText(str(ListaDatos[1]).strip())

    def editarParametros(self):

        if len(self.ui.lineEdit.text()) != 40:
            Alerta = QMessageBox.information(self, 'Alerta', "El Client Id debe tener 40 caracteres sin espacios", QMessageBox.Ok)

        elif len(self.ui.lineEdit_2.text()) != 128:

            Alerta = QMessageBox.information(self, 'Alerta', "El Secret Id debe tener 128 caracteres sin espacios", QMessageBox.Ok)
        else:
            clinteId = self.ui.lineEdit.text()
            SecretId = self.ui.lineEdit_2.text()

            self.modelo.editar(clinteId,SecretId)



