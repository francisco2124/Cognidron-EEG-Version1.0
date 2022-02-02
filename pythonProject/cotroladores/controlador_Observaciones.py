from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from vistas.capturarObservaciones import Ui_capturarObservaciones
from PyQt5.QtGui import QIntValidator



#En esta clase se inserta codigo que permita a la vista realizar distintos comportamientos sin modificar el archivo principal de la vista



class Controlador_Observaciones(QtWidgets.QMainWindow):

    def __init__(self, tiempoSesion, puntos, promedioPotencias, mayorTiempo, menorTiempo, promedioTiempo, porcentajeTiempo):
        super().__init__()
        print("soy la vista de capturar observaciones")
        self.ui= Ui_capturarObservaciones()
        self.ui.setupUi(self)
        #self.idTerapeuta = idTerapeuta


        #Resultados de Sesio
        self.tiempoSesion = tiempoSesion
        self.promedioPotencias = promedioPotencias
        self.puntosSesion = puntos
        self.mayorTiempo = mayorTiempo
        self.menorTiempo = menorTiempo
        self.promedioTiepo = promedioTiempo
        self.porcentajeTiempo = porcentajeTiempo

        self.InicializarGui()

    def InicializarGui(self):
        print("Hola mundo :)")
        self.ui.lbDuracioSesion.setText(str(self.tiempoSesion)+" Minutos")
        self.ui.lbPromedioPotencias.setText(str(self.promedioPotencias))
        self.ui.lbPuntos.setText(str(self.puntosSesion))
        self.ui.lbMayorTiempo.setText(str(self.mayorTiempo))
        self.ui.lbMenorTiempo.setText(str(self.menorTiempo))
        self.ui.lbPromedioTiempo.setText(str(self.promedioTiepo))
        self.ui.lbTiempoUmbralObtenido.setText(str(self.porcentajeTiempo)+" %")

