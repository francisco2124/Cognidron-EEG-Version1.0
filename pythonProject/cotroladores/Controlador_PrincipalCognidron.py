


from PyQt5 import QtWidgets
from vistas.principalCognitronp import Ui_MainWindow
from PyQt5.QtGui import QIntValidator



#Modelo
from modelos.ModeloTerapeuta import Modelo_Terapeuta

#----------------------------------Terapeutas----------------------------------------------
from cotroladores.ControladorAgregarTerapeuta import Controlador_AgrgarTerapeutas
from cotroladores.controlador_ConsultarTerapeuta import Controlador_ConsultarTerapeutas

#------------------------------------Tutores-----------------------------------------------
from cotroladores.ControladorAgregarTutor import Controlador_AgrgarTutor
from cotroladores.controlador_ConsultarTutores import Controlador_ConsultarTuotores

#----------------------------------Pacientes-----------------------------------------------
from cotroladores.ControladorAgregarPaciente import Controlador_AgrgarPaciente
from cotroladores.controlador_ConsultarPaciente import Controlador_ConsultarPaciente

#----------------------------------Reportes------------------------------------------------
from cotroladores.controladorReportesGenerales import Controlador_ConsultarReportesGenerales

#------------------------------------Terapias-----------------------------------------------
from cotroladores.controlador_Terapia import Controlador_Terapia
from cotroladores.controlador_TerapiaTipoNeurofeedback import Controlador_TerapiaNeurofeeldback

#----------------------------------Conexion------------------------------------------------
from cotroladores.controlador_ParametrosConexion import Controlador_parametros
from cotroladores.Controlador_conexion import Controlador_conexion

#----------------------------------Ejercicios----------------------------------------------
from cotroladores.controlador_EjerciciosNeurofeedback import Controlador_EjerciciosTerapeuticos
from cotroladores.controlador_EjerciciosControlMental import Controlador_EjerciciosTerapeuticosControlMental


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
        self.abrirTerapiaNeurofeedback()


    def InicializarGui(self):

        #----------------------------------Terapeutas----------------------------------------------
        self.ui.actionCrear_Terapeutta.triggered.connect(self.agregarTerapeuta)
        self.ui.actionConsultar_Terapeuta.triggered.connect(self.consultarTerapeuta)
        self.ui.actionIconoTerapeuta.triggered.connect(self.consultarTerapeuta)

        #-----------------------------------Tutores------------------------------------------------
        self.ui.actionCrear_Tutor_2.triggered.connect(self.agregarTutor)
        self.ui.actionConsultar_Tutor.triggered.connect(self.consultarTutor)
        self.ui.actionIconoTutor.triggered.connect(self.consultarTutor)

        #----------------------------------Paceintes------------------------------------------------
        self.ui.menuCrear_Paciente.triggered.connect(self.agregarPaciente)
        self.ui.actionIconPaciente.triggered.connect(self.consultarPaciente)

        #-----------------------------------Reportes-------------------------------------------------
        self.ui.actionIconConsulatrReporte.triggered.connect(self.consultarReportes)

        #-----------------------------------Terapias-------------------------------------------------
        self.ui.actionIconoTerapia.triggered.connect(self.abrirTerapia)
        self.ui.actionIconoTerapia_2.triggered.connect(self.abrirTerapiaNeurofeedback)

        #-----------------------------------Conexion-------------------------------------------------
        self.ui.actionConfigurar_parametros_de_conexi_n.triggered.connect(self.editarParametros)
        self.ui.actionConectar_Emotiv.triggered.connect(self.abrirConexionEmotiv)

        #-----------------------------------Ejercicios-------------------------------------------------
        self.ui.actionIconLibro.triggered.connect(self.ejerciciosNeuro)
        self.ui.actionEjerciciosControlMnetal.triggered.connect(self.ejerciciosControlMental)

        #---------------------------------Tipo de vistas-----------------------------------------------
        self.ui.actionVistaCascada.triggered.connect(self.vista_cascada)
        self.ui.actionVistaCuadricula.triggered.connect(self.vista_cuadri)
        self.ui.actionVistaVentana.triggered.connect(self.vista_tabs)

    #-----------------------------Funciones que mandan a llamar a los controladores-----------------------------------

    def agregarTerapeuta(self):

        self.abrir = QtWidgets.QMainWindow()
        self.abrir = Controlador_AgrgarTerapeutas()
        self.ui.mdiArea.addSubWindow(self.abrir)
        self.abrir.show()

    def consultarTerapeuta(self):

        self.abrir = QtWidgets.QMainWindow()
        self.abrir = Controlador_ConsultarTerapeutas()
        self.ui.mdiArea.addSubWindow(self.abrir)
        self.abrir.show()

    def agregarTutor(self):
        self.abrir = QtWidgets.QMainWindow()
        self.abrir = Controlador_AgrgarTutor()
        self.ui.mdiArea.addSubWindow(self.abrir)
        self.abrir.show()

    def consultarTutor(self):

        self.abrir = QtWidgets.QMainWindow()
        self.abrir = Controlador_ConsultarTuotores()
        self.ui.mdiArea.addSubWindow(self.abrir)
        self.abrir.show()

    def agregarPaciente(self):
        self.abrir = QtWidgets.QMainWindow()
        self.abrir = Controlador_AgrgarPaciente()
        self.ui.mdiArea.addSubWindow(self.abrir)
        self.abrir.show()

    def consultarPaciente(self):

        self.abrir = QtWidgets.QMainWindow()
        self.abrir = Controlador_ConsultarPaciente()
        self.ui.mdiArea.addSubWindow(self.abrir)
        self.abrir.show()

    def ejerciciosNeuro(self):

        self.abrir = QtWidgets.QMainWindow()
        self.abrir = Controlador_EjerciciosTerapeuticos()
        self.ui.mdiArea.addSubWindow(self.abrir)
        self.abrir.show()

    def ejerciciosControlMental(self):

        self.abrir = QtWidgets.QMainWindow()
        self.abrir = Controlador_EjerciciosTerapeuticosControlMental()
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

    def abrirTerapiaNeurofeedback(self):

        self.abrir = QtWidgets.QDialog()
        self.abrir = Controlador_TerapiaNeurofeeldback()
        self.ui.mdiArea.addSubWindow(self.abrir)
        self.abrir.show()

    def abrirConexionEmotiv(self):

        self.abrir = QtWidgets.QDialog()
        self.abrir = Controlador_conexion()
        self.ui.mdiArea.addSubWindow(self.abrir)
        self.abrir.show()

    def vista_tabs(self):
        self.ui.mdiArea.setViewMode(1)

    def vista_cascada(self):
        self.ui.mdiArea.cascadeSubWindows()

    def vista_cuadri(self):
        self.ui.mdiArea.tileSubWindows()