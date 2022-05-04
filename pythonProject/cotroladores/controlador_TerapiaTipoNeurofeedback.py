
import threading
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox
from datetime import *
import time
import pandas as pd
from PyQt5.Qt import Qt


#Hilos necesarios

from cotroladores.timerDuracion import HiloDuracion
from cotroladores.timerDuracionReloj import HiloDuracionReloj
from cotroladores.classSingnsEmotiv import HiloSingsEotiv
from cotroladores.classEmotiv import conexionEmotiv

from vistas.terapiaNeurofeedback import Ui_TerapiaNeurofeedback

#Pruebas ----------------------------

from cotroladores.pruebaEmotivList import pruebaconexionEmotiv


#modelos

from modelos.ModeloPacientes import Modelo_Paciente_
from modelos.modeloEjercicios import Modelo_Ejercicios

from cotroladores.controlador_Observaciones import Controlador_Observaciones

from PyQt5.QtGui import QIntValidator
import os
from playsound import playsound

from cotroladores.dron.controladorDron import Dron

#En esta clase se inserta codigo que permita a la vista realizar distintos comportamientos sin modificar el archivo principal de la vis
import sys


import random
from PyQt5.QtCore import QThread, pyqtSlot, pyqtSignal


class Controlador_TerapiaNeurofeeldback(QtWidgets.QMainWindow):


    def __init__(self, electrodos):
        super().__init__()
        self.ui = Ui_TerapiaNeurofeedback()
        self.ui.setupUi(self)

        #Lista de electrodos seleccionados en la ventana de conexion
        self.electrodosSelecionados = electrodos

        #Variables de imagenes de ejercicios
        self.posX = 380
        self.posY = 550
        self.ancho = 111
        self.alto = 71
        self.alterarposX = 0
        self.alterarposY = 0
        self.alterarancho = 0
        self.alteraralto = 0
        self.imagenDron1 = ""
        self.imagenDron2 = ""
        self.proximoMovimiento1 =  ""
        self.proximoMovimiento2 =  ""
        self.contadorPuntos = 1
        self.porcentajeBarraPuntaje = 0


        #Variables para ejercicios Complejor
        self.contadorIstrucciones = 20
        #Valida que se halla alcansado 3 veces el umbral
        self.contadorpassUmbral = 0

        #variable que almacena el tiempo en miutos que dura la sesion (Hilo)
        self.tiempoSesion = 0


        #Variable que almacena el hilo de emotiv
        self.hilo = HiloDuracion;
        self.puntaje = 0
        #self.Umbral = 0

        #Variable que contara el numero de veces que supero el umbral mas de 3 segundos
        self.contadorUmbralMas3Segundos = 0
        self.listaTiemposUmbral = []

        #Variables que verifican el estado del dron y la direccion
        self.estadoDron = 0
        self.dirreccion = 0

        #Contador motivacion que se activa cada 30 segundos que no se alcance el umbral
        self.motivacion = 0

        #Variable que establece la escala de umbral en la interfaz grafica
        self.escalaUmbral = 15
        #Variable que almacena 3 promedios de la deademas y coloca la linea de umbral en automatico
        self.listaUmbralAutomatico = []

        #Lista que alamacena el promedio de las potencias de las ondas cerebrales cada 5 segundos
        self.promedioPotencias5sg = []

        #variable que almacena el primer umbral
        self.tPrimerUmbral = "---"

        #Variable que almacena los segundos de concentracio sobre el umbral
        self.segundosSobreUmbral = 0

        #modelos
        self.modeloPaciente = Modelo_Paciente_()
        self.modeloEjercicios = Modelo_Ejercicios()

        #Funciones
        self.cargarCbPacientes()
        self.cargarCbEjercicios()

        #BanderaRegistroDatos
        self.banderaRegistro = False

        #Variable que determina si elctrol toal esta activado
        self.controlTotal = False

        self.ui.cbEjercicio.currentIndexChanged[str].connect(self.definirParametrosEjercicio)

        #Variables para crear archivo csv
        self.listapotencia = []

        self.inicializarGUI()

        #Detener Bateria Dron
        self.detenerHiloBateri = 0

        #Numero de electrodos seeccionados
        self.numeroElectrodosSeleccionados = 0

        #Lista del promedio de las potencias por segundos
        self.listapotenciaPorSegundo = []

        #Recuperar nombre de los esctrodos seleccionados
        self.listaElectrodosSeleccionados = [[]]

        #Variables de ejercicios complejos
        self.alturaMaximaDron = 0
        self.alturaMinimaDron = 0
        self.giroDron = 0


    def inicializarGUI(self):

        #Recuperar nombre y numero total de los electrodos seleccionados

        #Recuperar fecha actual
        fecha = str(datetime.now())
        self.fechaF = ""
        contadorFecha = 0
        for i in fecha:
            self.fechaF = self.fechaF + i
            contadorFecha = contadorFecha +1
            if contadorFecha == 10:
                break

        self.ui.lbFecha.setText("Fecha: "+ self.fechaF)

        #Inicializar valores de textos y botones
        self.ui.btnIniciarTerapia.setEnabled(True)
        self.ui.labelEventoDrone.setText("")
        self.ui.label.setText("")
        self.ui.labelComandosMentales.setText("")
        self.ui.pbBarraPuntos.setStyleSheet("QProgressBar::chunk "
                                                 "{"
                                                 "background-color: rgb(0, 200, 0);"
                                                 "}")
        self.ui.progressBar_4.setStyleSheet("QProgressBar::chunk "
                                            "{"
                                            "background-color: rgb(0, 170, 0);"
                                            "}")



        #Controles de emergencia del dron
        self.ui.btnObtenerDrone.clicked.connect(self.obtenerControl)

        self.ui.btnAterrizarDrone.clicked.connect(self.despegarAtirrizarDrone)
        self.ui.btnDecenderDrone.clicked.connect(self.decenderDrone)
        self.ui.btnDerechaDrone.clicked.connect(self.derechaDrone)
        self.ui.btnIsquierdaDrone.clicked.connect(self.izquierdaDrone)
        self.ui.btnAdelanteDrone.clicked.connect(self.adelanteDrone)
        self.ui.btnAtrasDrone.clicked.connect(self.atrasDrone)
        self.ui.btnElevarDrone.clicked.connect(self.elevarDrone)
        self.ui.rotarRelocj.clicked.connect(self.girarDroneDerecha)
        self.ui.rotarContraRelocj.clicked.connect(self.giraeDroneIzquierda)

        #Boton para capturar obseraciones
        self.ui.btbCapturarObservaciones.clicked.connect(self.abrirCapturarObservaciones)


        #Botones basicos de la sesion
        self.ui.btnIniciarTerapia.clicked.connect(self.iniciarTerapia)
        self.ui.btnGrabarSesion.clicked.connect(self.definirParametrosEjercicio)
        self.ui.btEditarUmbral.clicked.connect(self.modificarEscalaUmbral)


        #Botones del umbral
        self.ui.spinBoxUmbral.setMinimum(1)
        self.ui.spinBoxUmbral.setMaximum(99)
        self.ui.spinBoxUmbral.valueChanged.connect(self.colocarumbral)
        self.ui.spinBoxUmbral.setSingleStep(1)
        self.ui.spinBoxUmbral.setValue(30)

        self.hiloEmotiv = pruebaconexionEmotiv(self.electrodosSelecionados,self.ui.cbBanda.currentText())
        #self.hiloEmotiv = HiloSingsEotiv()

        self.activarBarraNeurofeedback()



    def iniciarTerapia(self):

        if self.ui.btnIniciarTerapia.text() == "Iniciar terapia":

                #Validaciones de seleccion de combo box
                if self.ui.cbPaciente.currentText() == "Selecciona un paciente":

                    lerta = QMessageBox.information(self, 'Alerta', "Selecciona un paciente para iniciar la terapia", QMessageBox.Ok)

                elif self.ui.cbEjercicio.currentText() == "Selecciona un ejercicio":

                    lerta = QMessageBox.information(self, 'Alerta', "Selecciona un ejercicio para iniciar la terapia", QMessageBox.Ok)

                #Condicioonal para la seleccion de la pista
                else:
                    if self.ui.cbPista.currentText() != "Sin Pista":
                        self.reproducirPista(self.ui.cbPista.currentText())
                    else:
                        pass

                    #Abrir audio de inicio de sesion
                    try:
                        os.startfile("C:\Cognidron-EEG-Software-Pruebas-Moni\pythonProject\multimedia\iniciosesion.mp3")
                    except:
                        print("Ocurrio un error con el sonido del punto")

                    try:
                        #-------IMPORTANTE----- Valores de conexion del dron
                        self.dron = Dron('192.168.10.1', 8889, "tello")
                        # Instancia del dron (Ip del dron, puerto del dron, valor del dicionario que se encuentra en la clase dron)
                    except:
                        pass
    #---------------
                    #self.hiloEmotiv = pruebaconexionEmotiv(self.electrodosSelecionados,self.ui.cbBanda.currentText())
                    #self.hiloEmotiv = HiloSingsEotiv()
                    try:
                        self.ejecutarHiloBateria()
                    except:
                        pass



                    #--------------------------------------------------------------------------------------------------
                    if self.ui.cbBanda.currentText() == "Theta/BetaBaja":
                        self.numeroElectrodosSeleccionados = 5


                    else:
                        for id,value in self.electrodosSelecionados.items():
                            print('{} = {}'.format(id,value))
                            if value == True:
                                self.listaElectrodosSeleccionados[0].append(id)

                        self.listaElectrodosSeleccionados[0].append("Promedio")
                        print("Los elestrodos seleccionados son: "+str(self.listaElectrodosSeleccionados[0]))
                        self.numeroElectrodosSeleccionados = len(self.listaElectrodosSeleccionados[0])
                        print("Num electrodos seleccionados "+str(self.numeroElectrodosSeleccionados))
                    #--------------------------------------------------------------------------------------------------
#---------------------
                    #self.activarBarraNeurofeedback()
                    self.llenarArchivoCSV()
                    self.ejecutardron()
                    #self.despegarDrone()
                    self.banderaRegistro = True
                    self.ui.btnIniciarTerapia.setText("Detener Terapia")
                    self.ui.btnIniciarTerapia.setStyleSheet("background-color: rgb(165, 164, 184);")
                    self.ui.btnGrabarSesion.setText("Grabando datos..")
                    self.ui.btnGrabarSesion.setStyleSheet("background-color: rgb(165, 164, 184);")
                    self.ui.lbGrabando.setText("Grabando...")
                    self.ui.cbEjercicio.setEnabled(False)
                    self.ui.cbBanda.setEnabled(False)
                    self.ui.cbPaciente.setEnabled(False)
                    self.ui.cbRobot.setEnabled(False)
                    self.iniciarTipempoSesion()
                    #icon = QtGui.QIcon()
                    #icon.addPixmap(QtGui.QPixmap(":/newPrefix/aterrizar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    #self.ui.btnAterrizarDrone.setIcon(icon)
                    #self.ejecutarHiloBateria()

        else:
            try:
                os.startfile("C:\Cognidron-EEG-Software-Pruebas-Moni\pythonProject\multimedia\sesionterminada.mp3")
            except:
               print("Ocurrio un error con el sonido del punto")
            self.banderaRegistro = False
            self.generarReportePotencias()
            self.hiloTiempo.detener()
            self.ui.btnIniciarTerapia.setText("Sesión Terminada")
            self.ui.btnGrabarSesion.setText("Datos Almacenados")
            self.ui.lbProximoMoviemntoDron.setText("Sesión Terminada")
            self.ui.lbGrabando.setText("No Grabando")
            self.ui.btnIniciarTerapia.setEnabled(False)
            self.ui.btnGrabarSesion.setEnabled(False)
            self.ui.btbCapturarObservaciones.setEnabled(True)
            self.hiloEmotiv.detener()
            self.controlTotal = True
            self.finalizarTerapia()
            self.listaElectrodosSeleccionados = [[]]





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




    def pruebaBateriaEmotiv(self):

        self.hiloEmotiv = pruebaconexionEmotiv(self.electrodosSelecionados,self.ui.cbBanda.currentText())
        main_thread = next(filter(lambda t: t.name == "MainThread", threading.enumerate()))
        while main_thread.is_alive():
            porcentajeBateriaEmotiv = self.hiloEmotiv.recuperarBatera()
            time.sleep(4)
            try:
                bateria = int(porcentajeBateriaEmotiv)
                if bateria == 0:
                    bateria = 20
                elif bateria ==1:
                    bateria = 40
                elif bateria ==2:
                    bateria = 60
                elif bateria ==3:
                    bateria = 80
                elif bateria ==4:
                    bateria = 100

                self.ui.lbPorcentajeBateriaEEG.setText(str(bateria)+"%")

            except:
                pass


    def ejecutarHiloBateriaEmotiv(self):

        self.hiloBateriaEmotiv= threading.Thread(target=self.pruebaBateriaEmotiv)
        self.hiloBateriaEmotiv.start()






    #Funcion para dejar de esuchar las instrucciones de la diadema
    def obtenerControl(self):
        try:
            #-------IMPORTANTE----- Valores de conexion del dron
            self.dron = Dron('192.168.10.1', 8889, "tello")
            # Instancia del dron (Ip del dron, puerto del dron, valor del dicionario que se encuentra en la clase dron)
        except:
            pass
        self.ejecutarHiloBateria()
        if self.ui.btnObtenerDrone.text() == "Obtener Control Total":
            self.controlTotal = True
            self.ui.btnObtenerDrone.setStyleSheet("background-color: rgb(0, 170 ,170);")
            self.ui.btnObtenerDrone.setText("Devolver Control")

        else:
            self.controlTotal = False
            self.ui.btnObtenerDrone.setStyleSheet("background-color: rgb();")
            self.ui.btnObtenerDrone.setText("Obtener Control Total")




#Funcion para finalizar una terapia
    def finalizarTerapia(self):
        self.aterrizarDrone()
        del(self.dron)

    #Funcion para capturar obsrvaciones y recuperar datos sbresalientes de la sesion
    def abrirCapturarObservaciones(self):

        if len(self.listaTiemposUmbral) != 0:
            max_tiempo = max(self.listaTiemposUmbral, key=int)
            min_tiempo = min(self.listaTiemposUmbral, key=int)
            promedioTiempo = sum(self.listaTiemposUmbral) / len(self.listaTiemposUmbral)
        else:
            max_tiempo = 0
            min_tiempo = 0
            promedioTiempo = 0

        porcentajeTiempo = (100 / len(self.listapotenciaPorSegundo)) * (sum(self.listaTiemposUmbral))
        porcentajeTiempoF = round(porcentajeTiempo, 2)

        #Obtener tipo ejercicio
        tipoEjercio = ""
        if self.ui.rbInivitorio.isChecked():
            tipoEjercio = "Inivitorio"
        else:
            tipoEjercio = "Exitatorio"

        #Recuperar frecuencia
        frecuencia  =  self.ui.cbBanda.currentText()

        #Recuperar Frecuencia
        ejericicio = self.ui.cbEjercicio.currentText()
        #Recuperar robot
        robot = self.ui.cbRobot.currentText()

        #Recuperar electrodos
        electrodos = ""
        for id,value in self.electrodosSelecionados.items():
            print('{} = {}'.format(id,value))
            if value == True:
                electrodos = electrodos +str(id)+ ", "
        try:
            promedioPotencias =  str(sum(self.listapotenciaPorSegundo) / len(self.listapotenciaPorSegundo))
        except:
            Alerta = QMessageBox.information(self, 'Alerta', "No se registraron las potencias por electrodo", QMessageBox.Ok)


        #Id Paciente
        indexPaciente = self.ui.cbPaciente.currentIndex()
        print("Index paciente es: "+str(indexPaciente))
        idPaciente = self.listaIdPaciente[indexPaciente-1]

        numVecesUmbrales = int(int(self.segundosSobreUmbral) / 3)
        print("Veces que supero el umbral por 3 segundos ="+str(numVecesUmbrales))

        self.abrir = Controlador_Observaciones(self.tiempoSesion,self.puntaje,promedioPotencias, electrodos, max_tiempo, min_tiempo,
                                               promedioTiempo, porcentajeTiempoF, self.fechaF, tipoEjercio, frecuencia,
                                               ejericicio, robot, idPaciente,self.tPrimerUmbral, numVecesUmbrales)
        self.abrir.show()

        self.ui.btnIniciarTerapia.setText("Iniciar terapia")
        self.ui.btnGrabarSesion.setText("Grabar Sesión")
        self.ui.lbProximoMoviemntoDron.setText("")
        self.ui.btbCapturarObservaciones.setEnabled(False)
        self.ui.btnIniciarTerapia.setEnabled(True)
        self.ui.btnGrabarSesion.setEnabled(True)
        self.ui.cbEjercicio.setEnabled(True)
        self.ui.cbEjercicio.setCurrentIndex(0)
        self.ui.cbPaciente.setEnabled(True)
        self.ui.cbPaciente.setCurrentIndex(0)
        self.ui.cbBanda.setEnabled(True)






    def definirParametrosEjercicio(self):

        ejercicio = self.ui.cbEjercicio.currentText()
        if ejercicio == "Elevar y descender dron":
            self.ui.imgDron.setStyleSheet("image: url(:/newPrefix/EjerElevar.png);")
            self.posY = 550
            self.posX = 414
            self.ancho = 111
            self.alto = 71

            self.alterarposY = 55
            self.alterarposX = 0
            self.alterarancho = 0
            self.alteraralto = 0

            self.ui.imgDron.setGeometry(QtCore.QRect(self.posX, self.posY, self.ancho, self.alto))
            self.imagenDron1 = "image: url(:/newPrefix/EjerElevar.png);"
            self.imagenDron2= "image: url(:/newPrefix/EjerDecender.png);"
            self.proximoMovimiento1 = "- Elevar Dron -"
            self.proximoMovimiento2 = "- Decender Dron -"
            self.ui.lbProximoMoviemntoDron.setText(self.proximoMovimiento1)

        elif ejercicio == "Adelante y Atras Dron":
            self.ui.imgDron.setStyleSheet("image: url(:/newPrefix/EjerAdelante.png);")
            self.posY = 410
            self.posX = 360
            self.ancho = 171
            self.alto = 131

            self.alterarposY = 0
            self.alterarposX = 10
            self.alterarancho = 10
            self.alteraralto = 10
            self.imagenDron1 = "image: url(:/newPrefix/EjerAdelante.png);"
            self.imagenDron2= "image: url(:/newPrefix/EjerAtras.png);"
            self.proximoMovimiento1 = "- Edelante Dron -"
            self.proximoMovimiento2 = "- Atras Dron -"
            self.ui.imgDron.setGeometry(QtCore.QRect(self.posX, self.posY, self.ancho, self.alto))

        elif ejercicio == "Derecha e Izquierda Dron":
            self.ui.imgDron.setStyleSheet("image: url(:/newPrefix/EjerDerecha.png);")
            self.ancho = 111
            self.alto = 71
            self.posY = 400
            self.posX = 250

            self.alterarposY = 0
            self.alterarposX = 60
            self.alterarancho = 0
            self.alteraralto = 0

            self.ui.imgDron.setGeometry(QtCore.QRect(self.posX, self.posY, self.ancho, self.alto))
            self.imagenDron1 = "image: url(:/newPrefix/EjerDerecha.png);"
            self.imagenDron2= "image: url(:/newPrefix/EjerIzquierda.png);"
            self.proximoMovimiento1 = "- Derecha Dron -"
            self.proximoMovimiento2 = "- Izquierda Dron -"
            self.ui.lbProximoMoviemntoDron.setText(self.proximoMovimiento1)


        elif ejercicio == "Girar Dron":
            self.ui.imgDron.setStyleSheet("image: url(:/newPrefix/EjerCirculo.png);")

            self.posY = 360
            self.posX = 340
            self.ancho = 251
            self.alto = 191

            self.ui.imgDron.setGeometry(QtCore.QRect(self.posX, self.posY, self.ancho, self.alto))

            #Valores para ejercicio girar a la derecha
            self.listaEjercicioGirar = ["EjerCirculo1.png", "EjerCirculo2.png","EjerCirculo3.png","EjerCirculo4.png","EjerCirculo5.png",
                                    "EjerCirculo6.png",  "EjerCirculo7.png", "EjerCirculo8.png"]
            self.contadorListaEjercicioGirar = 0
            self.proximoMovimiento1 = "Girar 45° grados a la derecha"
        elif ejercicio == "Ejercicio Complejo 1":
            print("Entre en Ejercicio Complejo 1")
            self.ui.lbProximoMoviemntoDron.setText("El dron despegara")
            self.posY = 360
            self.posX = 340
            self.ancho = 251
            self.alto = 191
            self.ui.imgDron.setGeometry(QtCore.QRect(self.posX, self.posY, self.ancho, self.alto))

            self.ui.imgDron.setStyleSheet("image: url(:/newPrefix/despegar.png);")
        else:
            self.ui.labelEventoDrone.setText("------Selecciona un ejercicio---------")






    #Ventana emergente para instancia del dron
    def dronNoInstanciado(self):

        lerta = QMessageBox.information(self, 'Alerta', "Inicia sesion y selecciona un dron para usar sus comandos...", QMessageBox.Ok)

    #**************************************************************************
    #-----IMPORTANTE--------------FUNCIONES DEL DRON---------------------------
    #**************************************************************************

    #-----Istrucciones--------------ISTRUCCIONES DE DRON-----------------------
    """______________________________________________________________________
        La funciob istruccion1 es la encargada de establecer los movimientos de dron con base a la seleccion de un
        ejercicio. Dicha seleccion se hace desde el combo box para ejercicios ubicado en la ventana de terapia de tipo
        neurofeedback.
        
        Se asigana un comando del dron (Adelante, Atras, Elevar etc..) para una la istrucion numero uno que se reitira 
        5 veces y despues de acurdo a la seleccion del ejercicio la istruccion hara la istruccion contrarea para que 
        regrese a la posicion original. (Manera ciclica) Ejemplo:
        
        Seleccion de ejercicio: Eelvar y desender dron:
        
            La istruccion 1 elevara el dron 5 veces 
            La istruccion 2 hara que el dron desienda 5 veces el dron
        
        El ejercicio se mantendra de esa forma hasta terminar la sesion terapeutica.
        
        Lod ejercicios que no necesiten ser ciclicos como los es el ejercicios de rotar el dron hacia la derecha 
        simplemente se repitira el comando del dron tanto en istruccion uno cpmo en istruccion 2 (Girar dron hacia la derecha)
       ______________________________________________________________________"""

    def valoresPredeterminadosdePuntaje(self):
        if self.banderaRegistro == True:
            self.contadorPuntos = self.contadorPuntos + 1
            self.porcentajeBarraPuntaje = self.porcentajeBarraPuntaje + 20
            self.ui.pbBarraPuntos.setValue(self.porcentajeBarraPuntaje)
            self.segundosSobreUmbral = self.segundosSobreUmbral + 3
            self.ui.lbSegundosObtenidos.setText(str(self.segundosSobreUmbral)+" Segundos")
        else:
            pass

    def valoresPredeterminadosPuntaje2(self):
        if self.banderaRegistro == True:
            self.contadorPuntos = self.contadorPuntos + 1
            self.porcentajeBarraPuntaje = self.porcentajeBarraPuntaje + 20
            self.ui.pbBarraPuntos.setValue(self.porcentajeBarraPuntaje)
            self.puntaje = self.puntaje +1
            self.ui.label_18.setText(str(self.puntaje))
            self.contadorPuntos = 1
            self.porcentajeBarraPuntaje = 0
            self.ui.pbBarraPuntos.setValue(self.porcentajeBarraPuntaje)
            self.segundosSobreUmbral = self.segundosSobreUmbral + 3
            self.ui.lbSegundosObtenidos.setText(str(self.segundosSobreUmbral)+" Segundos")
        else:
            pass

    def instruccion1(self):

        #print("Contador puntos es =: "+str(self.contadorPuntos))
        ejercicio = self.ui.cbEjercicio.currentText()
        #print("El ejercicio es: "+str(ejercicio))

        if self.contadorPuntos !=5:

            if ejercicio == "Girar Dron":

                 self.ui.imgDron.setStyleSheet("image: url(:/newPrefix/"+self.listaEjercicioGirar[self.contadorListaEjercicioGirar]+");")
                 self.contadorListaEjercicioGirar =  self.contadorListaEjercicioGirar +  1
                 self.valoresPredeterminadosdePuntaje()
                 self.ui.lbProximoMoviemntoDron.setText(self.proximoMovimiento1)
                 if self.contadorListaEjercicioGirar == 8:
                     self.contadorListaEjercicioGirar = 0


            else:
                self.valoresPredeterminadosdePuntaje()
                self.ui.lbProximoMoviemntoDron.setText(self.proximoMovimiento1)
                self.posY = self.posY - self.alterarposY
                self.posX = self.posX + self.alterarposX
                self.ancho = self.ancho - self.alterarancho
                self.alto = self.alto - self.alteraralto
                self.ui.imgDron.setGeometry(QtCore.QRect(self.posX, self.posY, self.ancho, self.alto))



        elif self.contadorPuntos ==5:
            if ejercicio == "Girar Dron":

                self.ui.imgDron.setStyleSheet("image: url(:/newPrefix/"+self.listaEjercicioGirar[self.contadorListaEjercicioGirar]+");")
                self.contadorListaEjercicioGirar =  self.contadorListaEjercicioGirar +  1
                self.valoresPredeterminadosPuntaje2()
                self.ui.lbProximoMoviemntoDron.setText(self.proximoMovimiento1)
                if self.contadorListaEjercicioGirar == 8:
                    self.contadorListaEjercicioGirar = 0

            else:
                self.posY = self.posY - self.alterarposY
                self.posX = self.posX + self.alterarposX
                self.ancho = self.ancho - self.alterarancho
                self.alto = self.alto - self.alteraralto
                self.ui.imgDron.setGeometry(QtCore.QRect(self.posX, self.posY, self.ancho, self.alto))
                self.valoresPredeterminadosPuntaje2()
                self.ui.imgDron.setStyleSheet(self.imagenDron2)
                self.ui.lbProximoMoviemntoDron.setText(self.proximoMovimiento2)
                self.dirreccion = 1


        if ejercicio == "Elevar y descender dron":
            try:
                self.dron.elevar()
            except:
                pass
        elif ejercicio == "Adelante y Atras Dron":
            try:
                self.dron.adelante()
            except:
                pass
        elif ejercicio == "Derecha e Izquierda Dron":
            try:
                self.dron.derecha()
            except:
                pass
        elif ejercicio == "Girar Dron":
            try:
                self.dron.girarderecha()
            except:
                pass
        else:
            self.ui.labelEventoDrone.setText("------Selecciona un ejercicio---------")




    def instruccion2(self):

        ejercicio = self.ui.cbEjercicio.currentText()

        if self.contadorPuntos != 5:
            if ejercicio == "Girar Dron":

                self.ui.imgDron.setStyleSheet("image: url(:/newPrefix/"+self.listaEjercicioGirar[self.contadorListaEjercicioGirar]+");")
                self.contadorListaEjercicioGirar =  self.contadorListaEjercicioGirar +  1
                self.valoresPredeterminadosdePuntaje()
                self.ui.lbProximoMoviemntoDron.setText(self.proximoMovimiento1)
                if self.contadorListaEjercicioGirar == 8:
                    self.contadorListaEjercicioGirar = 0


            else:
                self.ui.lbProximoMoviemntoDron.setText(self.proximoMovimiento2)
                self.posY = self.posY + self.alterarposY
                self.posX = self.posX - self.alterarposX
                self.ancho = self.ancho + self.alterarancho
                self.alto = self.alto + self.alteraralto
                self.ui.imgDron.setGeometry(QtCore.QRect(self.posX, self.posY, self.ancho, self.alto))
                self.valoresPredeterminadosdePuntaje()

        elif self.contadorPuntos==5:
            if ejercicio == "Girar Dron":

                self.ui.imgDron.setStyleSheet("image: url(:/newPrefix/"+self.listaEjercicioGirar[self.contadorListaEjercicioGirar]+");")
                self.contadorListaEjercicioGirar =  self.contadorListaEjercicioGirar +  1
                self.valoresPredeterminadosPuntaje2()
                self.ui.lbProximoMoviemntoDron.setText(self.proximoMovimiento1)
                if self.contadorListaEjercicioGirar == 8:
                    self.contadorListaEjercicioGirar = 0


            else:
                self.posY = self.posY + self.alterarposY
                self.posX = self.posX - self.alterarposX
                self.ancho = self.ancho + self.alterarancho
                self.alto = self.alto + self.alteraralto
                self.ui.imgDron.setGeometry(QtCore.QRect(self.posX, self.posY, self.ancho, self.alto))
                self.valoresPredeterminadosPuntaje2()
                self.ui.imgDron.setStyleSheet(self.imagenDron1)
                self.ui.lbProximoMoviemntoDron.setText(self.proximoMovimiento1)
                self.dirreccion = 0


        if ejercicio == "Elevar y descender dron":
            self.dron.decender()
        elif ejercicio == "Adelante y Atras Dron":
            self.dron.atras()
        elif ejercicio == "Derecha e Izquierda Dron":
            self.dron.izquierda()
        elif ejercicio == "Girar Dron":
            self.dron.girarderecha()
        else:
            self.ui.labelEventoDrone.setText("------Selecciona un ejercicio---------")


    #****************************************************************************************************************************
    #-Comandos del dron-(Despegar, Aterrizar, Elevar, Desender, Adelante, Atras, Derecha, Izquierda, Roatar Izquierda y Derecha)
    #****************************************************************************************************************************

    def despegarAtirrizarDrone(self):

        if self.estadoDron == 0:
            try:
                self.despegarDrone()
            except:
                self.dronNoInstanciado()

        else:
            self.aterrizarDrone()

    def despegarDrone(self):
        print("llame la funcion despegar")
        self.dron.despegar()
        #--------Cambiar imagen del boton de Despege y Aterrizaje del dron
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/aterrizar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.btnAterrizarDrone.setIcon(icon)
        self.estadoDron = 1
        #print("El estado del dron es: "+str(self.estadoDron))
    def aterrizarDrone(self):

        print("llame la funcion aterrizar")
        self.dron.aterrizar()
        self.estadoDron = 0
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/despegar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.btnAterrizarDrone.setIcon(icon)
        self.detenerHiloBateri = 2

    def adelanteDrone(self):
        try:
            print("llame la funcion Adelante")
            #La funcion se ubica en la clase controlador dron ubicada en la carpeta dron dentro de controladores
            self.dron.adelante()
        except:
            self.dronNoInstanciado()

    def atrasDrone(self):

        try:
            print("llame la funcion Atras")
            self.dron.atras()
        except:
            self.dronNoInstanciado()

    def elevarDrone(self):

        try:
            print("llame la funcion elevar Dron")
            self.dron.elevar()
        except:
            self.dronNoInstanciado()

    def decenderDrone(self):

        try:
            print("llame la funcion decender")
            self.dron.decender()

        except:
            self.dronNoInstanciado()

    def derechaDrone(self):

        try:
            print("llame la funcion derecha")
            self.dron.derecha()

        except:
            self.dronNoInstanciado()

    def izquierdaDrone(self):

        try:
            print("llame la funcion izquierda")
            self.dron.izquierda()
        except:
            self.dronNoInstanciado()

    def girarDroneDerecha(self):

        try:
            print("llame la funcion girar derecha")
            self.dron.girarderecha()
        except:
            self.dronNoInstanciado()

    def giraeDroneIzquierda(self):

        try:
            print("llame la funcion girar izquierda")
            self.dron.girarizquierda()
        except:
            self.dronNoInstanciado()

    #Controles de umbral ------------------------------------------------------------------------
    def colocarumbral(self):

        #print(str(self.ui.spinBoxUmbral.value()))

        self.umbral = 570 - (int(self.ui.spinBoxUmbral.value()) * 4)
        self.ui.lbUmbral.setGeometry(QtCore.QRect(673, self.umbral, 161, 91))

    def bajarumbral(self):

        if self.ui.spinBoxUmbral.value() != 1:
            #print(str(self.ui.spinBoxUmbral.value()))
            valor = self.ui.spinBoxUmbral.value() - 1
            self.ui.spinBoxUmbral.setValue(valor)

            self.umbral = 573 - (int(self.ui.spinBoxUmbral.value()) * 4)
            self.ui.lbUmbral.setGeometry(QtCore.QRect(673, self.umbral, 161, 91))
        else:
            #print("Umbral Minimo")
            pass
    def elevarumbral(self):

        if self.ui.spinBoxUmbral.value() != 99:
            #print(str(self.ui.spinBoxUmbral.value()))
            valor = self.ui.spinBoxUmbral.value() + 1
            self.ui.spinBoxUmbral.setValue(valor)

            self.umbral = 573 - (int(self.ui.spinBoxUmbral.value()) * 4)
            self.ui.lbUmbral.setGeometry(QtCore.QRect(673, self.umbral, 161, 91))
        else:
            #print("Umbral Maximo")
            pass

    #Metodos con hilos

    def deternerTipoDuracion(self):

        self.hilo.detener()
    def reanudarTipoDuracion(self):

        self.hilo.reanudar()

    #----------------Bateria del Dron---------------------------------

    def obtenerBateriaEmotiv(self):
        hiloBateria = pruebaconexionEmotiv(self.electrodosSelecionados,self.ui.cbBanda.currentText(), "bateria")
        hiloBateria.signEmotiv.connect(self.asignarHiloBateria)
        #self.hilo2.signDS.connect(self.barraNeurofeedback)
        hiloBateria.start()

    def asignarHiloBateria(self, bateria):

        try:
            bateria = int(bateria)
            if bateria == 0:
                bateria = 20
            elif bateria ==1:
                bateria = 40
            elif bateria ==2:
                bateria = 60
            elif bateria ==3:
                bateria = 80
            elif bateria ==4:
                bateria = 100

            self.ui.lbPorcentajeBateriaEEG.setText(str(bateria)+"%")

        except:
            pass


    #-IPORTANTE---------Funciones de la barra de progreso-------------
    def activarBarraNeurofeedback(self):

        self.hiloEmotiv.signEmotiv.connect(self.barraNeurofeedback)
        #self.hilo2.signDS.connect(self.barraNeurofeedback)
        self.hiloEmotiv.start()

    def barraNeurofeedback(self,val):


        promedioPotencia = val[self.numeroElectrodosSeleccionados - 1]
        #promedioPotencia = val

        val = (promedioPotencia * 100) / self.escalaUmbral


        self.ui.progressBar_4.setValue(val)
        self.promedioPotencias5sg.append(promedioPotencia)

        if len(self.promedioPotencias5sg) == 5:
            promedio5sg = round((sum(self.promedioPotencias5sg) / 5), 3)
            self.ui.lbPromedioPotencias5sg.setText(str(promedio5sg))
            self.promedioPotencias5sg = []


        if self.ui.rbUmbralAutomatico.isChecked()== True:

            #print("===================Automatico===========")
            self.listaUmbralAutomatico.append(val)
            #print("La lista tiene: "+str(self.listaUmbralAutomatico))

            if len(self.listaUmbralAutomatico) == 3:

                actualizarUmbral = sum(self.listaUmbralAutomatico) / 3
                #print("El promedio cada 3 segundos es: "+str(actualizarUmbral))
                self.ui.spinBoxUmbral.setValue(actualizarUmbral)
                self.listaUmbralAutomatico = []


        else:
            #print("===================Manual===========")
        #print("==============================================")
            pass
    #Funciones para el timer de la seson

    def iniciarTipempoSesion(self):
        self.hiloTiempo = HiloDuracionReloj()
        self.hiloTiempo.signDSReloj.connect(self.actualizarTiempoSesion)
        self.hiloTiempo.start()

    def actualizarTiempoSesion(self,tiempo):

        self.ui.lbMinutos.setText(tiempo)
        self.tiempoSesion = tiempo


    #Funcion para establecer escala de umbral
    def modificarEscalaUmbral(self):

        try:
            nuevoUmbral = int(self.ui.edUmbral.text())
            self.escalaUmbral = nuevoUmbral
        except:
            pass


    #Funciones para crear y llenar el archico csv correspondiente al reporte de potencias
    def llenarArchivoCSV(self):
        self.hiloEmotiv.signEmotiv.connect(self.registrarPotenciasReporte)
        self.hiloEmotiv.start()



    def cargarArchivoCSV(self, potencia): #222222222222222222222222222222222222222222222222222222222222222222222222222222222222-------

            if self.banderaRegistro == True:
                archivo = open("archivo.csv","w")
                #Titulo
                archivo.write("Reporte de potencias 2")
                archivo.write("\n")

                #Metadatos
                archivo.write("*Fecha")
                archivo.write(",")
                archivo.write("14-02-2022")
                archivo.write(",")
                archivo.write(",")
                archivo.write("*Duracion de sesion")
                archivo.write(",")
                archivo.write("1:05 minutos")
                archivo.write("\n")
                archivo.write("*Tipo de ejercicio")
                archivo.write(",")
                archivo.write("Inivitorio")
                archivo.write(",")
                archivo.write(",")
                archivo.write("Promedio F")
                archivo.write(",")
                archivo.write("3.146")

                archivo.write("\n")

                #Encabezado
                archivo.write("AF3")
                archivo.write(",")
                archivo.write("F7")
                archivo.write(",")
                archivo.write("F3")
                archivo.write(",")
                archivo.write("Promedio")


                self.listapotencia.append(potencia)
                #self.listapotencia.append(potencia)

                for i in self.listapotencia:
                    archivo.write("\n")
                    archivo.write(str(i[0]))
                    archivo.write(",")
                    archivo.write(str(i[1]))
                    archivo.write(",")
                    archivo.write(str(i[2]))
                    archivo.write(",")
                    archivo.write(str(i[3]))

            else:
                print("No estoy almacenando datos....")


    #***********************************************************
    #--IMPORTANTE -----------Movimiento del dron----------------
    #***********************************************************

    def ejecutardron(self):
        #self.hilodron = conexionEmotiv()
        #self.hilodron = HiloSingsEotiv()
        #self.hilodron.signEmotiv.connect(self.movimientoDron)
        self.hiloEmotiv.signEmotiv.connect(self.movimientoDron)
        self.hiloEmotiv.start()

    def movimientoDron(self, potencia):

        if self.ui.cbEjercicio.currentText() == "Ejercicio Complejo 1":
            self.umbral = int(self.ui.spinBoxUmbral.value())

            potencia = (potencia[self.numeroElectrodosSeleccionados - 1] * 100) / self.escalaUmbral

            #potencia = potencia * 1000
            if self.ui.rdbExitatorio.isChecked()== True:
                self.ui.labelEventoDrone.setText("Eleva tus ondas cerebrales")
                #operdor logico exitatorio
                operador = potencia >= self.umbral
            else:
                #operador logico inibitorio
                self.ui.labelEventoDrone.setText("Disminuye tus ondas cerebrales")
                operador = potencia <= self.umbral

            if operador:

                self.ui.labelComandosMentales.setText("-SI- se alcanzo el umbral subir")
                self.motivacion = 0
                self.contadorpassUmbral = self.contadorpassUmbral + 1

                if self.contadorpassUmbral == 3:

                    if self.contadorPuntos !=5:
                        self.valoresPredeterminadosdePuntaje()

                    elif self.contadorPuntos ==5:
                        self.valoresPredeterminadosPuntaje2()


                    if self.contadorIstrucciones == 14:
                        self.contadorIstrucciones = 0

                    else:
                        pass

                    if self.contadorIstrucciones <13:

                        list = ["Girar Izquierda","Girar Izquierda", "Girar Izquierda","Girar Izquierda","Elevar",
                                "Elevar","Elevar","Girar Izquierda","Girar Izquierda","Girar Izquierda","Girar Izquierda",
                                "Desecnder","Desecnder","Desecnder"]

                        listImages = ["EjerGiro90Izq.png","EjerGiro90Izq.png","EjerGiro90Izq.png","EjerGiro90Izq.png","EjerElevarC1.png",
                                      "EjerElevarC1.png","EjerElevarC1.png","EjerGiro90Izq.png","EjerGiro90Izq.png","EjerGiro90Izq.png",
                                      "EjerGiro90Izq.png","EjerDecenderC1.png","EjerDecenderC1.png","EjerDecenderC1.png"]
                        imagenDron = listImages[self.contadorIstrucciones]
                        self.ui.lbProximoMoviemntoDron.setText(list[self.contadorIstrucciones])
                        self.ui.imgDron.setStyleSheet("image: url(:/newPrefix/"+imagenDron+");")

                    else:
                        pass


                    if self.controlTotal == False:
                        if self.estadoDron == 0:
                            print("Despegar-----------------")
                            self.dron.despegar()
                            icon = QtGui.QIcon()
                            icon.addPixmap(QtGui.QPixmap(":/newPrefix/aterrizar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                            self.ui.btnAterrizarDrone.setIcon(icon)
                            self.ui.imgDron.setStyleSheet("image: url(:/newPrefix/EjerGiro90Izq.png);")
                            self.ui.lbProximoMoviemntoDron.setText("Girar Izquierda")
                            self.contadorIstrucciones = 1
                            self.estadoDron = 1
                            self.tPrimerUmbral = self.ui.lbMinutos.text()
                            print("El  primer umbral se logro en el minuto: "+self.tPrimerUmbral)
                        elif self.giroDron <4:
                            self.dron.girarizquierda90()
                            self.contadorIstrucciones = self.contadorIstrucciones + 1
                            self.giroDron = self.giroDron +1
                        elif self.alturaMaximaDron <3:
                            self.dron.elevar()
                            self.contadorIstrucciones = self.contadorIstrucciones + 1
                            self.alturaMaximaDron = self.alturaMaximaDron + 1
                            if self.alturaMaximaDron == 3:
                                self.giroDron = 0
                                self.alturaMinimaDron = 0
                            else:
                                pass
                        elif self.alturaMinimaDron <3:
                            self.dron.decender()
                            self.contadorIstrucciones = self.contadorIstrucciones + 1
                            self.alturaMinimaDron= self.alturaMinimaDron + 1
                            if self.alturaMinimaDron == 3:
                                self.giroDron = 0
                                self.alturaMaximaDron = 0
                            else:
                                pass
                        else:
                            print("Erro con el ejercicio complejo_1")


                        try:
                            os.startfile("C:\Cognidron-EEG-Software-Pruebas-Moni\pythonProject\multimedia\punto.mp3")
                        except:
                            print("Ocurrio un error con el sonido de umbral")

                    self.contadorpassUmbral = 0
                    self.contadorUmbralMas3Segundos = self.contadorUmbralMas3Segundos+1
                    print("=================================: "+str(self.contadorUmbralMas3Segundos))

            else:
                if self.contadorUmbralMas3Segundos > 0:
                    self.listaTiemposUmbral.append(self.contadorUmbralMas3Segundos * 3)
                    print("La lista de tiempos tiene ===== "+str(self.listaTiemposUmbral))
                self.ui.labelComandosMentales.setText("-No- se alcazo el umbral")
                self.motivacion = self.motivacion + 1
                residuomotivacion = self.motivacion / 30
                residuo = residuomotivacion.is_integer()
                print("Reciduo : "+str(residuomotivacion))
                print("Motivacion : "+str(self.motivacion))
                if self.motivacion !=0 and residuo == True:
                    try:
                        os.startfile("C:\Cognidron-EEG-Software-Pruebas-Moni\pythonProject\multimedia\motivacion.mp3")
                    except:
                        print("Ocurrio un error con el sonido de motivacion")

                self.contadorUmbralMas3Segundos = 0
                self.contadorpassUmbral = 0

        elif self.ui.cbEjercicio.currentText() == "Ejercicio Complejo 2":
            self.umbral = int(self.ui.spinBoxUmbral.value())

            potencia = (potencia[self.numeroElectrodosSeleccionados - 1] * 100) / self.escalaUmbral

            #potencia = potencia * 1000
            if self.ui.rdbExitatorio.isChecked()== True:
                self.ui.labelEventoDrone.setText("Eleva tus ondas cerebrales")
                #operdor logico exitatorio
                operador = potencia >= self.umbral
            else:
                #operador logico inibitorio
                self.ui.labelEventoDrone.setText("Disminuye tus ondas cerebrales")
                operador = potencia <= self.umbral

            if operador:

                self.ui.labelComandosMentales.setText("-SI- se alcanzo el umbral subir")
                self.contadorpassUmbral = self.contadorpassUmbral + 1

                if self.contadorpassUmbral == 3:
                    if self.contadorPuntos !=5:
                        self.valoresPredeterminadosdePuntaje()

                    elif self.contadorPuntos ==5:
                        self.valoresPredeterminadosPuntaje2()


                    if self.controlTotal == False:
                        if self.estadoDron == 0:
                            self.dron.despegar()
                            self.estadoDron = 1
                        elif self.giroDron <4:
                            self.dron.girarizquierda90()
                            self.giroDron = self.giroDron +1
                        elif self.alturaMaximaDron <3:
                            self.dron.adelante()
                            self.alturaMaximaDron = self.alturaMaximaDron + 1
                            if self.alturaMaximaDron == 3:
                                self.giroDron = 0
                                self.alturaMinimaDron = 0
                            else:
                                pass
                        elif self.alturaMinimaDron <3:
                            self.dron.atras()
                            self.alturaMinimaDron= self.alturaMinimaDron + 1
                            if self.alturaMinimaDron == 3:
                                self.giroDron = 0
                                self.alturaMaximaDron = 0
                            else:
                                pass
                        else:
                            print("Erro con el ejercicio complejo_1")

                    self.contadorpassUmbral = 0
                    self.contadorUmbralMas3Segundos = self.contadorUmbralMas3Segundos+1
                    print("=================================: "+str(self.contadorUmbralMas3Segundos))

            else:
                if self.contadorUmbralMas3Segundos > 0:
                    self.listaTiemposUmbral.append(self.contadorUmbralMas3Segundos * 3)
                    print("La lista de tiempos tiene ===== "+str(self.listaTiemposUmbral))
                self.ui.labelComandosMentales.setText("-No- se alcazo el umbral")
                self.contadorUmbralMas3Segundos = 0
                self.contadorpassUmbral = 0

        else:
            self.umbral = int(self.ui.spinBoxUmbral.value())

            potencia = (potencia[self.numeroElectrodosSeleccionados - 1] * 100) / self.escalaUmbral

            #potencia = potencia * 1000
            if self.ui.rdbExitatorio.isChecked()== True:
                self.ui.labelEventoDrone.setText("Eleva tus ondas cerebrales")
                #operdor logico exitatorio
                operador = potencia >= self.umbral
            else:
                #operador logico inibitorio
                self.ui.labelEventoDrone.setText("Disminuye tus ondas cerebrales")
                operador = potencia <= self.umbral


            #Comparacion de umbral deacurdo al tipo ejercicio
            if self.dirreccion == 0:

                #print("Elevar dron")
                if operador:

                    self.ui.labelComandosMentales.setText("-SI- se alcanzo el umbral subir")
                    self.contadorpassUmbral = self.contadorpassUmbral + 1

                    if self.contadorpassUmbral == 3:

                        if self.controlTotal == False:
                            self.instruccion1()

                        self.contadorpassUmbral = 0
                        self.contadorUmbralMas3Segundos = self.contadorUmbralMas3Segundos+1
                        print("=================================: "+str(self.contadorUmbralMas3Segundos))

                else:
                    if self.contadorUmbralMas3Segundos > 0:
                        self.listaTiemposUmbral.append(self.contadorUmbralMas3Segundos * 3)
                        print("La lista de tiempos tiene ===== "+str(self.listaTiemposUmbral))
                    self.ui.labelComandosMentales.setText("-No- se alcazo el umbral")
                    self.contadorUmbralMas3Segundos = 0
                    self.contadorpassUmbral = 0


            else:
                #print("Bajar dron")
                if operador:

                    self.ui.labelComandosMentales.setText("-SI- se alcanzo el umbral")
                    self.contadorpassUmbral = self.contadorpassUmbral + 1

                    if self.contadorpassUmbral == 3:
                        if self.controlTotal == False:
                            self.instruccion2()
                        self.contadorpassUmbral = 0
                        self.contadorUmbralMas3Segundos = self.contadorUmbralMas3Segundos + 1
                        print("=================================: "+str(self.contadorUmbralMas3Segundos))


                else:
                    if self.contadorUmbralMas3Segundos > 0:
                        self.listaTiemposUmbral.append(self.contadorUmbralMas3Segundos * 3)
                        print("La lista de tiempos tiene ===== "+str(self.listaTiemposUmbral))
                    self.ui.labelComandosMentales.setText("-No- se alcazo el umbral")
                    self.contadorpassUmbral = 0
                    self.contadorUmbralMas3Segundos = 0

    #Funcion Umbral Intelinte (Automatico)

    #------Funciones para llenar los combo box de pacientes y de ejercicios recueperando datos de la base de datos

    def cargarCbPacientes(self):
        #lista idPaciente
        self.listaIdPaciente = []
        pacientes =  self.modeloPaciente.recuperarPacientes()
        #print(str(pacientes))
        #print(terapeutas)
        for i in pacientes:
            self.listaIdPaciente.append(i[0])

        combo = self.ui.cbPaciente
        combo.clear()
        combo.addItem("Selecciona un paciente")
        combo.addItems([str(x[1])+" "+str(x[2])+"_id:"+str(x[0] ) for x in pacientes])

    def cargarCbEjercicios(self):

        ejercicios =  self.modeloEjercicios.cargarTablaEjercicios()
        #print(str(ejercicios))
        #print(terapeutas)

        combo = self.ui.cbEjercicio
        combo.clear()
        combo.addItem("Selecciona un ejercicio")
        combo.addItems([str(x[1]) for x in ejercicios])

    #Funcion para reproducir la pista
    def reproducirPista(self, pista):


        if pista == "Pista 1":
            try:
                os.startfile("C:\Cognidron-EEG-Software-Pruebas-Moni\pythonProject\multimedia\pista_1.mp3")
            except:
                Alerta = QMessageBox.information(self, 'Alerta', "Ocurrio un error con el reproductor de musica", QMessageBox.Ok)

        elif pista == "Pista 2":
            try:
                os.startfile("C:\Cognidron-EEG-Software-Pruebas-Moni\pythonProject\multimedia\pista_2.mp3")
            except:
                Alerta = QMessageBox.information(self, 'Alerta', "Ocurrio un error con el reproductor de musica", QMessageBox.Ok)

        elif pista == "Pista 3":
            try:
                os.startfile("C:\Cognidron-EEG-Software-Pruebas-Moni\pythonProject\multimedia\pista_3.mp3")
            except:
                Alerta = QMessageBox.information(self, 'Alerta', "Ocurrio un error con el reproductor de musica", QMessageBox.Ok)

    def registrarPotenciasReporte(self, potencia):


        if self.banderaRegistro == True:

            if self.ui.cbBanda.currentText() == "Theta/BetaBaja":
                self.listapotencia.append(potencia)
                self.listapotenciaPorSegundo.append(potencia[4])
            else:
                self.listapotencia.append(potencia)
                self.listapotenciaPorSegundo.append(potencia[self.numeroElectrodosSeleccionados - 1])

        else:

            print("No estoy almacenando potencias.....")



    def generarReportePotencias(self):
        indexPaciente = self.ui.cbPaciente.currentIndex()
        idPaciente = self.listaIdPaciente[indexPaciente-1]
        if self.ui.cbBanda.currentText() == "Theta/BetaBaja":

            listaEncabezadosThetaBetaBaja = [["ThetaF3","ThetaF4","BetaBajaF3","BetaBajaF4","Theta/BetaBajaF3,F4"]]
            data = pd.DataFrame(self.listapotencia[0:],columns=listaEncabezadosThetaBetaBaja[0])

            data.head()


            directorio = "C:\CogniDron-EEG\Reportes_De_Potencias\paciente"+str(idPaciente)+""
            directorio2 = "C:\CogniDron-EEG\Reportes_De_Potencias\paciente"+str(idPaciente)+"\d"+str(self.fechaF)
            try:
                os.mkdir(directorio)
            except:
                pass

            try:
                os.mkdir(directorio2)
            except:
                pass

            data.to_csv("C:\CogniDron-EEG\Reportes_De_Potencias\paciente"+str(idPaciente)+"\d"+str(self.fechaF)+"\Reporte1.csv", index=False)
            self.listapotencia = []
        else:

            data = pd.DataFrame(self.listapotencia[0:],columns=self.listaElectrodosSeleccionados[0])

            data.head()

            #data.to_csv("C:\CogniDron-EEG\Reportes_De_Potencias\Reporte1.csv", index=False)
            data.to_csv("C:\CogniDron-EEG\Reportes_De_Potencias\paciente"+str(idPaciente)+"\d"+str(self.fechaF)+"\Reporte1.csv", index=False)
            self.listapotencia = []


    def cerrarVentana(self):
        try:
            self.hiloEmotiv.detener()

        except:
            print("No hay hilo de emotiv")

    def closeEvent(self, a0: QtGui.QCloseEvent):
        resultado = QMessageBox.question(self,"Salir...","¿Seguro que quieres salir de la ventana de terapia?",
                                         QMessageBox.Yes|QMessageBox.No)
        if resultado == QMessageBox.Yes: a0.accept(), self.cerrarVentana()

        else: a0.ignore()

