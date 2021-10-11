


from PyQt5 import QtWidgets
from vistas.principalCognitronp import Ui_MainWindow
from PyQt5.QtGui import QIntValidator



#Modelo
from modelos.ModeloTerapeuta import Modelo_Terapeuta

#Sub Ventanas
from cotroladores.ControladorAgregarTerapeuta import Controlador_AgrgarTerapeutas
from cotroladores.controlador_ConsultarTerapeuta import Controlador_ConsultarTerapeutas
from cotroladores.controladorReportesGenerales import Controlador_ConsultarReportesGenerales
from cotroladores.controlador_ConsultarTerapeutaSelccionado import Control_ConsultarTerapectuaSelec


#Tutor
from cotroladores.ControladorAgregarTutor import Controlador_AgrgarTutor
from cotroladores.controlador_ConsultarTutores import Controlador_ConsultarTuotores

#otros
from cotroladores.controlador_ParametrosConexion import Controlador_parametros
from cotroladores.controlador_Terapia import Controlador_Terapia
from cotroladores.Controlador_conexion import Controlador_conexion
#En esta clase se inserta codigo que permita a la vista realizar distintos comportamientos sin modificar el archivo principal de la vista


class Controlador_PrincipalCognidron(QtWidgets.QMainWindow):

    x = 0
    def __init__(self):
        super().__init__()
        print("soy princial de vista")
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)
        self.InicializarGui()
        self.modelo = Modelo_Terapeuta()
        #elf.generalTerapeuta = Controlador_ConsultarTerapeutas(self.modelo)
        #self.terapeutaSelect = Control_ConsultarTerapectuaSelec(self.modelo)
        self.abrirTerapia()


    def InicializarGui(self):

        self.ui.actionCrear_Terapeutta.triggered.connect(self.agregarTerapeuta)
        self.ui.actionConsultar_Terapeuta.triggered.connect(self.consultarTerapeuta)
        self.ui.actionIconConsulatrReporte.triggered.connect(self.consultarReportes)


        self.ui.actionCrear_Tutor_2.triggered.connect(self.agregarTutor)
        self.ui.actionConsultar_Tutor.triggered.connect(self.consultarTutor)


        self.ui.actionConfigurar_parametros_de_conexi_n.triggered.connect(self.editarParametros)
        self.ui.actionIconoTerapia.triggered.connect(self.abrirTerapia)
        self.ui.actionConectar_Emotiv.triggered.connect(self.abrirConexionEmotiv)

    def agregarTerapeuta(self):

        self.abrir = QtWidgets.QMainWindow()
        self.abrir = Controlador_AgrgarTerapeutas()
        self.ui.mdiArea.addSubWindow(self.abrir)
        self.abrir.show()

    def agregarTutor(self):
            self.abrir = QtWidgets.QMainWindow()
            self.abrir = Controlador_AgrgarTutor()
            self.ui.mdiArea.addSubWindow(self.abrir)
            self.abrir.show()

    def consultarTerapeuta(self):

        self.abrir = QtWidgets.QMainWindow()
        self.abrir = Controlador_ConsultarTerapeutas()
        self.ui.mdiArea.addSubWindow(self.abrir)
        self.abrir.show()

    def consultarTutor(self):

        self.abrir = QtWidgets.QMainWindow()
        self.abrir = Controlador_ConsultarTuotores()
        self.ui.mdiArea.addSubWindow(self.abrir)
        self.abrir.show()

    def consultarReportes(self):

        self.abrir = QtWidgets.QMainWindow()
        self.abrir = Controlador_ConsultarReportesGenerales()
        self.ui.mdiArea.addSubWindow(self.abrir)
        self.abrir.show()

    def editarParametros(self):

        self.abrir = QtWidgets.QDialog()
        self.abrir = Controlador_parametros()
        self.ui.mdiArea.addSubWindow(self.abrir)
        self.abrir.show()

    def abrirTerapia(self):

        self.abrir = QtWidgets.QDialog()
        self.abrir = Controlador_Terapia()
        self.ui.mdiArea.addSubWindow(self.abrir)
        self.abrir.show()

    def abrirConexionEmotiv(self):

        self.abrir = QtWidgets.QDialog()
        self.abrir = Controlador_conexion()
        self.ui.mdiArea.addSubWindow(self.abrir)
        self.abrir.show()