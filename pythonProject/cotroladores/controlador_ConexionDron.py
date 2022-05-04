from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIntValidator
from vistas.conexiondron import Ui_ConexionDron
import threading
import time



#En esta clase se inserta codigo que permita a la vista realizar distintos comportamientos sin modificar el archivo principal de la vista



class Controlador_ConexionDron(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui= Ui_ConexionDron()
        self.ui.setupUi(self)
        self.InicializarGui()


    def InicializarGui(self):

        pass

    def pruebaBateriaDron(self):

        #-------IMPORTANTE----- Valores de conexion del dron

        # Instancia del dron (Ip del dron, puerto del dron, valor del dicionario que se encuentra en la clase dron)
        main_thread = next(filter(lambda t: t.name == "MainThread", threading.enumerate()))
        while main_thread.is_alive():
            porcentajeBateria = self.dron.getBateria()
            time.sleep(4)
            try:
                bateria = int(porcentajeBateria)
                self.ui.lbPorcentajeBateriaDron.setText(str(bateria)+"%")

            except:
                pass


    def ejecutarHiloBateria(self):

        self.hiloBateriaDron = threading.Thread(target=self.pruebaBateriaDron)
        self.hiloBateriaDron.start()