


from PyQt5 import QtWidgets, QtGui
from vistas.principalCognitronp import Ui_MainWindow
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QMessageBox
from PyQt5.Qt import Qt



#Modelo
from modelos.ModeloTerapeuta import Modelo_Terapeuta

#----------------------------------Terapeutas----------------------------------------------
from cotroladores.ControladorAgregarTerapeuta import Controlador_AgrgarTerapeutas
from cotroladores.controlador_ConsultarTerapeuta import Controlador_ConsultarTerapeutas
from cotroladores.controlador_RecuperarTerapeutas import Controlador_RecuperarTerapeutasEliminados

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
from cotroladores.controlador_ConexionDron import Controlador_ConexionDron

#----------------------------------Ejercicios----------------------------------------------
from cotroladores.controlador_EjerciciosNeurofeedback import Controlador_EjerciciosTerapeuticos
from cotroladores.controlador_EjerciciosControlMental import Controlador_EjerciciosTerapeuticosControlMental


#----------------------------------Modulo de ayuda----------------------------------------------
from cotroladores.controlador_moduloAyuda import Controlador_ModuloAyuda

#En esta clase se inserta codigo que permita a la vista realizar distintos comportamientos sin modificar el archivo principal de la vista


class Controlador_PrincipalCognidron(QtWidgets.QMainWindow):

    x = 0
    def __init__(self,user):
        super().__init__()
        print("soy princial de vista")
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)
        #Electrodos bajo el estandar 10-10
        self.electrodos = {'Estandar':'10-10',"AF3":False, "F7":False,"F3":False,'FC5':False,'T7':False,'P7':False,'01':False,'02':False, 'P8':False, 'T8':False, 'FC6':False, 'F4':False,'F8':False,'AF4':False}
        self.user = user
        self.modelo = Modelo_Terapeuta()
        self.InicializarGui()
        self.abrirConexionEmotiv()
        print("El usuario es: "+self.user)



    def InicializarGui(self):

        #----------------------------------Terapeutas----------------------------------------------
        self.ui.actionCrear_Terapeutta.triggered.connect(self.agregarTerapeuta)
        self.ui.actionConsultar_Terapeuta.triggered.connect(self.consultarTerapeuta)
        self.ui.actionIconoTerapeuta.triggered.connect(self.consultarTerapeuta)
        self.ui.actionRecuperar_Teraputas_Eliminados.triggered.connect(self.recuperarTerapeutasEliminados)

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
        self.ui.menuConectar_Robot_Fisico.triggered.connect(self.abrirConexionDron)

        #-----------------------------------Ejercicios-------------------------------------------------
        self.ui.actionIconLibro.triggered.connect(self.ejerciciosNeuro)
        self.ui.actionEjerciciosControlMnetal.triggered.connect(self.ejerciciosControlMental)

        #---------------------------------Tipo de vistas-----------------------------------------------
        self.ui.actionVistaCascada.triggered.connect(self.vista_cascada)
        self.ui.actionVistaCuadricula.triggered.connect(self.vista_cuadri)
        self.ui.actionVistaVentana.triggered.connect(self.vista_tabs)

        datos = self.modelo.cargarPlaceHolder(self.user)
        print("Las datos de terapeuta son:" +str(datos))
        datosF = datos[0]
        if datosF[14] == '0':
            print("Eres un simple mortal  XD")
            self.ui.actionIconoTerapeuta.setEnabled(False)
            self.ui.menuTerapeuta.setEnabled(False)
        else:
            print("Eres administrador")

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

    def recuperarTerapeutasEliminados(self):

        self.abrir = QtWidgets.QMainWindow()
        self.abrir = Controlador_RecuperarTerapeutasEliminados()
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

        a =0
        print("La lista de electrodos es---------------------")
        for id,value in self.electrodos.items():
            print('{} = {}'.format(id,value))
            if value == False:
                a = a+1
        #Regresar a 14 para que la validacion sea correcta
        if a == 14:
            lerta = QMessageBox.information(self, 'Alerta', "No se han identificado ningun electrodo..... Por favor realiza la seleccion de los electros", QMessageBox.Ok)
            self.abrirConexionEmotiv()
        else:
            self.abrir = QtWidgets.QDialog()
            self.abrir = Controlador_TerapiaNeurofeeldback(self.electrodos, self.user)
            self.ui.mdiArea.addSubWindow(self.abrir)
            self.abrir.show()



    def abrirConexionEmotiv(self):

        self.abrir = QtWidgets.QDialog()
        self.abrir = Controlador_conexion(self.electrodos,self.ui.mdiArea, self.user)
        self.ui.mdiArea.addSubWindow(self.abrir)
        self.abrir.show()

    def abrirConexionDron(self):

        self.abrir = QtWidgets.QDialog()
        self.abrir = Controlador_ConexionDron()
        self.ui.mdiArea.addSubWindow(self.abrir)
        self.abrir.show()

    def abrirModuloAyuda(self):

        self.abrir = QtWidgets.QDialog()
        self.abrir = Controlador_ModuloAyuda()
        self.ui.mdiArea.addSubWindow(self.abrir)
        self.abrir.show()

    def vista_tabs(self):
        self.ui.mdiArea.setViewMode(2)

    def vista_cascada(self):
        self.ui.mdiArea.cascadeSubWindows()

    def vista_cuadri(self):
        self.ui.mdiArea.tileSubWindows()

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:

        if a0.key() == Qt.Key_M:
            print("Hola desde M")