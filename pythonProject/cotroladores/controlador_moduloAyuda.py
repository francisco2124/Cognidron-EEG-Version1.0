from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from vistas.ayudaDelSistema import Ui_Dialog
from PyQt5.QtGui import QIntValidator


class Controlador_ModuloAyuda(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        print("soy la vista de consultar terapeutas")
        self.ui= Ui_Dialog()
        self.ui.setupUi(self)
        self.InicializarGui()


    def InicializarGui(self):

        pass