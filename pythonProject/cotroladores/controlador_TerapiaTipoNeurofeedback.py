from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox

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


    def __init__(self):
        super().__init__()
        self.ui = Ui_TerapiaNeurofeedback()
        self.ui.setupUi(self)
        self.inicializarGUI()

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



        self.hilo = HiloDuracion;
        self.puntaje = 0
        self.Umbral = 0
        self.contadorumbral =1
        self.contadorumbralMaximo =0
        self.estadoDron = 0
        self.dirreccion = 0

        self.escalaUmbral = 15
        self.listaUmbralAutomatico = []

        #modelos
        self.modeloPaciente = Modelo_Paciente_()
        self.modeloEjercicios = Modelo_Ejercicios()

        #Funciones
        self.cargarCbPacientes()
        self.cargarCbEjercicios()

        self.listapotencia = []
        self.hiloEmotiv = pruebaconexionEmotiv()

        self.ui.cbEjercicio.currentIndexChanged[str].connect(self.definirParametrosEjercicio)







    def inicializarGUI(self):

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
        #self.ui.btnObtenerDrone.clicked.connect(self.obtenerControlDrone)

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



    def iniciarTerapia(self):

    #-------IMPORTANTE----- Valores de conexion del dron
            self.dron = Dron('192.168.10.1', 8889, "tello")
            # Instancia del dron (Ip del dron, puerto del dron, valor del dicionario que se encuentra en la clase dron)

            #Obtener nombre de la pista del combo box de la entana de terapia
            pista = self.ui.cbPista.currentText()

            #Condicioonal para la seleccion de la pista
            if pista != "Sin Pista":
                self.activarBarraNeurofeedback()
                self.crearArchivoCSV()
                self.reproducirPista(pista)
                self.ejecutardron()
                self.iniciarTipempoSesion()

            else:
                self.activarBarraNeurofeedback()
                self.crearArchivoCSV()
                self.ejecutardron()
                self.iniciarTipempoSesion()


    #Funcion para finalizar una terapia

    def finalizarTerapia(self):
        del(self.dron)

    #Funcion para capturar obsrvaciones y recuperar datos sbresalientes de la sesion
    def abrirCapturarObservaciones(self):

        self.abrir = Controlador_Observaciones()
        self.abrir.show()

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

        self.contadorPuntos = self.contadorPuntos + 1
        self.porcentajeBarraPuntaje = self.porcentajeBarraPuntaje + 20
        self.ui.pbBarraPuntos.setValue(self.porcentajeBarraPuntaje)

    def valoresPredeterminadosPuntaje2(self):

        self.contadorPuntos = self.contadorPuntos + 1
        self.porcentajeBarraPuntaje = self.porcentajeBarraPuntaje + 20
        self.ui.pbBarraPuntos.setValue(self.porcentajeBarraPuntaje)
        self.puntaje = self.puntaje +1
        self.ui.label_18.setText(str(self.puntaje))
        self.contadorPuntos = 1
        self.porcentajeBarraPuntaje = 0
        self.ui.pbBarraPuntos.setValue(self.porcentajeBarraPuntaje)

    def instruccion1(self):

        print("Contador puntos es =: "+str(self.contadorPuntos))
        ejercicio = self.ui.cbEjercicio.currentText()
        print("El ejercicio es: "+str(ejercicio))

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
            self.dron.elevar()
        elif ejercicio == "Adelante y Atras Dron":
            self.dron.adelante()
        elif ejercicio == "Derecha e Izquierda Dron":
            self.dron.derecha()
        elif ejercicio == "Girar Dron":
            self.dron.girarderecha()
        else:
            self.ui.labelEventoDrone.setText("------Selecciona un ejercicio---------")




    def instruccion2(self):

        print("Contador puntos es =: "+str(self.contadorPuntos))
        ejercicio = self.ui.cbEjercicio.currentText()
        print("El ejercicio es: "+str(ejercicio))

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

    '''
    #Funcion para obtener un control total de dron. (Dejara de recibir istruciones del EEG)
    def obtenerControlDrone(self):

        if self.ui.btnObtenerDrone.text() == "Obtener Control Total":

            self.ui.labelComandosMentales.setText("Control del dron activado")
            self.ui.btnObtenerDrone.setText("Devolver Control")
            self.ui.btnObtenerDrone.setStyleSheet("background-color: rgb(85, 85, 255);")
            self.ui.btnActivarEmotiv.setStyleSheet("background-color: rgb(182, 181, 203);")
            self.ui.btnActivarEmotiv.setEnabled(False)


        else:
            self.ui.labelComandosMentales.setText("Control del dron desactivado")
            self.ui.btnObtenerDrone.setText("Obtener Control Total")
            self.ui.btnObtenerDrone.setStyleSheet("background-color: rgb(116, 147 ,198);")
            self.ui.btnActivarEmotiv.setStyleSheet("background-color: rgb(0, 226, 0);")
            self.ui.btnActivarEmotiv.setEnabled(True)
        '''
    #****************************************************************************************************************************
    #-Comandos del dron-(Despegar, Aterrizar, Elevar, Desender, Adelante, Atras, Derecha, Izquierda, Roatar Izquierda y Derecha)
    #****************************************************************************************************************************

    def despegarAtirrizarDrone(self):

        if self.estadoDron == 0:
            try:
                print("llame la funcion despegar")
                self.dron.despegar()
                #--------Cambiar imagen del boton de Despege y Aterrizaje del dron
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(":/newPrefix/aterrizar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.ui.btnAterrizarDrone.setIcon(icon)
                self.estadoDron = 1
            except:
                self.dronNoInstanciado()

        else:
            print("llame la funcion aterrizar")
            self.dron.aterrizar()
            self.estadoDron = 0
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/newPrefix/despegar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.btnAterrizarDrone.setIcon(icon)

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

    #-IPORTANTE---------Funciones de la barra de progreso-------------
    def activarBarraNeurofeedback(self):

        self.hiloEmotiv.signEmotiv.connect(self.barraNeurofeedback)
        #self.hilo2.signDS.connect(self.barraNeurofeedback)
        self.hiloEmotiv.start()

    def barraNeurofeedback(self,val):

        #self.ui.progressBar_4.setValue(val[4])
        print("Recibi el valor -------- "+str(val))
        #val = (val * 100) / self.escalaUmbral
        val = (val[8] * 100) / self.escalaUmbral
        print("El valor aplicando la escala -" +str(self.escalaUmbral)+"- es: "+str(val))
        self.ui.progressBar_4.setValue(val)

        if self.ui.rbUmbralAutomatico.isChecked()== True:

            print("===================Automatico===========")
            self.listaUmbralAutomatico.append(val)
            print("La lista tiene: "+str(self.listaUmbralAutomatico))

            if len(self.listaUmbralAutomatico) == 3:

                actualizarUmbral = sum(self.listaUmbralAutomatico) / 3
                print("El promedio cada 3 segundos es: "+str(actualizarUmbral))
                self.ui.spinBoxUmbral.setValue(actualizarUmbral)
                self.listaUmbralAutomatico = []


        else:
            print("===================Manual===========")
        print("==============================================")
    #Funciones para el timer de la seson

    def iniciarTipempoSesion(self):
        self.hiloTiempo = HiloDuracionReloj()
        self.hiloTiempo.signDSReloj.connect(self.actualizarTiempoSesion)
        self.hiloTiempo.start()

    def actualizarTiempoSesion(self,tiempo):

        self.ui.lbMinutos.setText(tiempo)

    #Funcion para establecer escala de umbral
    def modificarEscalaUmbral(self):
        nuevoUmbral = int(self.ui.edUmbral.text())
        self.escalaUmbral = nuevoUmbral


    #Funciones para crear y llenar el archico csv correspondiente al reporte de potencias
    def crearArchivoCSV(self):
        #self.hilo3 = HiloSingsEotiv()
        self.hiloEmotiv.signEmotiv.connect(self.llenarArchivoCSV)
        #self.hilo3.signDS.connect(self.almacenarPotencias)
        self.hiloEmotiv.start()



    def llenarArchivoCSV(self, potencia): #222222222222222222222222222222222222222222222222222222222222222222222222222222222222-------
        archivo = open("archivo.csv","w")
        #Titulo
        archivo.write("Reporte de potencias 2")
        archivo.write("\n")

        #Encabezado
        archivo.write("Electrodo")
        archivo.write(",")
        archivo.write("Banda")
        archivo.write(",")
        archivo.write("Promedio Potencia")
        archivo.write(",")
        archivo.write("Id de la sesio")
        archivo.write(",")
        archivo.write("Tipo de ejercicio")
        archivo.write(",")
        archivo.write("Id del paciente")

        #potencias = [20.2,30.2,10.12,40.56,50,78,20.2,30.2,10.12,40.56,50,78,20.2,30.2,10.12,40.56,50,78,1,1,1]

        self.listapotencia.append(str(potencia))
        for i in self.listapotencia:

            archivo.write("\n")
            archivo.write("F3 F4")
            archivo.write(",")
            archivo.write("Theta/BetaL")
            archivo.write(",")
            archivo.write(str(i))
            archivo.write(",")
            archivo.write("001")
            archivo.write(",")
            archivo.write("Inivitorio")
            archivo.write(",")
            archivo.write("001")


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

        self.umbral = int(self.ui.spinBoxUmbral.value())

        #potencia = (potencia * 100) / self.escalaUmbral
        potencia = (potencia[8] * 100) / self.escalaUmbral

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
                self.instruccion1()
                #self.contadorumbralMaximo = self.contadorumbralMaximo + 1
                #self.contadorumbral = 0

            else:
                self.ui.labelComandosMentales.setText("-No- se alcazo el umbral")
                #self.contadorumbral = self.contadorumbral + 1
                #self.contadorumbralMaximo = 0


        else:
            #print("Bajar dron")
            if operador:

                self.ui.labelComandosMentales.setText("-SI- se alcanzo el umbral bajar")
                self.instruccion2()
                #self.contadorumbralMaximo = self.contadorumbralMaximo + 1
                #self.contadorumbral = 0
            else:
                self.ui.labelComandosMentales.setText("-No- se alcazo el umbral")
                #self.contadorumbral = self.contadorumbral + 1
                #self.contadorumbralMaximo = 0

    #Funcion Umbral Intelinte (Automatico)

    #------Funciones para llenar los combo box de pacientes y de ejercicios recueperando datos de la base de datos

    def cargarCbPacientes(self):

        pacientes =  self.modeloPaciente.recuperarPacientes()
        #print(str(pacientes))
        #print(terapeutas)

        combo = self.ui.cbPaciente
        combo.clear()
        combo.addItem("Selecciona un paciente")
        combo.addItems([str(x[1])+" "+str(x[2])+" "+str(x[0]) for x in pacientes])

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
