from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox

#Hilos necesarios

from cotroladores.timerDuracion import HiloDuracion
from cotroladores.timerDuracionReloj import HiloDuracionReloj
from cotroladores.classSingnsEmotiv import HiloSingsEotiv
from cotroladores.classEmotiv import conexionEmotiv

from vistas.terapiaNeurofeedback import Ui_TerapiaNeurofeedback


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
        self.posX = 380
        self.posY = 550
        self.ancho = 111
        self.alto = 71
        self.hilo = HiloDuracion;
        self.puntaje = 0
        self.Umbral = 0
        self.contadorumbral =1
        self.contadorumbralMaximo =0
        self.estadoDron = 0
        self.contadorPuntos = 0
        self.dirreccion = 0

        #modelos
        self.modeloPaciente = Modelo_Paciente_()
        self.modeloEjercicios = Modelo_Ejercicios()

        #Funciones
        self.cargarCbPacientes()
        self.cargarCbEjercicios()

        self.listapotencia = []
        self.hiloEmotiv = conexionEmotiv()






    def inicializarGUI(self):

        self.ui.btnIniciarTerapia.setEnabled(True)
        self.ui.labelEventoDrone.setText("")
        self.ui.label.setText("")
        self.ui.labelComandosMentales.setText("")


        #Controles de emergencia del dron
        self.ui.btnObtenerDrone.clicked.connect(self.obtenerControlDrone)

        self.ui.btnAterrizarDrone.clicked.connect(self.despegarAtirrizarDrone)
        self.ui.btnDecenderDrone.clicked.connect(self.decenderDrone)
        self.ui.btnDerechaDrone.clicked.connect(self.derechaDrone)
        self.ui.btnIsquierdaDrone.clicked.connect(self.izquierdaDrone)
        self.ui.btnAdelanteDrone.clicked.connect(self.adelanteDrone)
        self.ui.btnAtrasDrone.clicked.connect(self.atrasDrone)
        self.ui.btnElevarDrone.clicked.connect(self.elevarDrone)
        self.ui.rotarRelocj.clicked.connect(self.girarDroneDerecha)
        self.ui.rotarContraRelocj.clicked.connect(self.giraeDroneIzquierda)
        self.ui.btbCapturarObservaciones.clicked.connect(self.abrirCapturarObservaciones)


        #Botones basicos de la sesion
        self.ui.btnIniciarTerapia.clicked.connect(self.iniciarTerapia)
        self.ui.btnActivarEmotiv.clicked.connect(self.instruccion1)


        #Botones del umbral
        self.ui.spinBoxUmbral.setMinimum(1)
        self.ui.spinBoxUmbral.setMaximum(99)
        self.ui.spinBoxUmbral.valueChanged.connect(self.colocarumbral)
        self.ui.spinBoxUmbral.setSingleStep(1)
        self.ui.spinBoxUmbral.setValue(30)



    def iniciarTerapia(self):

            self.dron = Dron('192.168.10.1', 8889, "tello")

            pista = self.ui.cbPista.currentText()

            if pista != "Sin Pista":

                self.activarBarraNeurofeedback()
                self.crearArchivoCSV()
                self.reproducirPista(pista)
                self.ejecutardron()
            else:
                self.activarBarraNeurofeedback()
                self.crearArchivoCSV()
                self.ejecutardron()







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


    #Acciones del dron :) para el control manual ---------------------------------------

    def dronNoInstanciado(self):

        lerta = QMessageBox.information(self, 'Alerta', "Inicia sesion y selecciona un dron para usar sus comandos...", QMessageBox.Ok)

    def despegarAtirrizarDrone(self):

        if self.estadoDron == 0:
            try:
                print("llame la funcion despegar")
                self.dron.despegar()
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

    def instruccion1(self):

        print("Contador puntos es =: "+str(self.contadorPuntos))

        if self.contadorPuntos != 5:
            if self.contadorPuntos == 1:
                self.posY = self.posY - 33
                self.ui.label_11.setGeometry(QtCore.QRect(self.posX, self.posY, self.ancho, self.alto))
                self.contadorPuntos = self.contadorPuntos + 1
            else:
                self.posY = self.posY - 66
                self.ui.label_11.setGeometry(QtCore.QRect(self.posX, self.posY, self.ancho, self.alto))
                self.contadorPuntos = self.contadorPuntos + 1
        else:
            self.posY = 550
            self.ui.label_11.setGeometry(QtCore.QRect(self.posX, self.posY, self.ancho, self.alto))
            self.contadorPuntos = 1
            self.dirreccion = 1

        ejercicio = self.ui.cbEjercicio.currentText()
        print("El ejercicio es: "+str(ejercicio))

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

        if self.contadorPuntos != 5:
            if self.contadorPuntos == 1:
                self.posY = self.posY - 33
                self.ui.label_11.setGeometry(QtCore.QRect(self.posX, self.posY, self.ancho, self.alto))
                self.contadorPuntos = self.contadorPuntos + 1
            else:
                self.posY = self.posY - 66
                self.ui.label_11.setGeometry(QtCore.QRect(self.posX, self.posY, self.ancho, self.alto))
                self.contadorPuntos = self.contadorPuntos + 1
        else:
            self.posY = 550
            self.ui.label_11.setGeometry(QtCore.QRect(self.posX, self.posY, self.ancho, self.alto))
            self.contadorPuntos = 1
            self.dirreccion = 0

        ejercicio = self.ui.cbEjercicio.currentText()
        print("El ejercicio es: "+str(ejercicio))

        if ejercicio == "Elevar y descender dron":
            self.dron.decender()
        elif ejercicio == "Adelante y Atras Dron":
            self.dron.atras()
        elif ejercicio == "Derecha e Izquierda Dron":
            self.dron.izquierda()
        elif ejercicio == "Girar Dron":
            self.dron.girarizquierda()
        else:
            self.ui.labelEventoDrone.setText("------Selecciona un ejercicio---------")

    def adelanteDrone(self):
        try:
            print("llame la funcion Adelante")
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
        self.ui.label_11.setText(str(self.hilo.estadoHilo()))
    def reanudarTipoDuracion(self):

        self.hilo.reanudar()
        self.ui.label_11.setText(str(self.hilo.estadoHilo()))

    def finalizarTerapia(self):
        del(self.dron)

    def activarBarraNeurofeedback(self):
        #self.hilo2 = conexionEmotiv()
        #self.hilo2 = HiloSingsEotiv()
        self.hiloEmotiv.signEmotiv.connect(self.barraNeurofeedback)
        #self.hilo2.signDS.connect(self.barraNeurofeedback)
        self.hiloEmotiv.start()


    def barraNeurofeedback(self,val):

        #val = val*1000
        #print("la potencia de la barra es", str(val))
        self.ui.progressBar_4.setValue(val)






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
    #Movimiento del dron
    def ejecutardron(self):
        #self.hilodron = conexionEmotiv()
        #self.hilodron = HiloSingsEotiv()
        #self.hilodron.signEmotiv.connect(self.movimientoDron)
        self.hiloEmotiv.signEmotiv.connect(self.movimientoDron)
        self.hiloEmotiv.start()

    def movimientoDron(self, potencia):

        self.umbral = int(self.ui.spinBoxUmbral.value())


        #potencia = potencia * 1000
        if self.ui.rdbExitatorio.isChecked()== True:
            self.ui.labelEventoDrone.setText("Eleva tus ondas cerebrales")
            #operdor logico exitatorio
            operador = potencia >= self.umbral
        else:
            #operador logico inibitorio
            self.ui.labelEventoDrone.setText("Disminuye tus ondas cerebrales")
            operador = potencia <= self.umbral

        if self.dirreccion == 0:
            if self.contadorPuntos == 5:
                if self.puntaje !=0 and self.puntaje%2 != 0:
                    self.puntaje = self.puntaje +1
                    self.ui.label_18.setText(str(self.puntaje))
            #direccion
            self.val = True

        elif self.dirreccion == 1:
            self.val = False
            if self.contadorPuntos == 5:
                self.puntaje = self.puntaje +1
                self.ui.label_18.setText(str(self.puntaje))

        #Comparacion de umbral deacurdo al tipo ejercicio
        if self.val == True:

            #print("Elevar dron")
            if operador:

                self.instruccion1()
                self.ui.labelComandosMentales.setText("-SI- se alcanzo el umbral subir")

                self.contadorumbralMaximo = self.contadorumbralMaximo + 1
                self.contadorumbral = 0

            else:
                self.ui.labelComandosMentales.setText("-No- se alcazo el umbral")
                self.contadorumbral = self.contadorumbral + 1
                self.contadorumbralMaximo = 0


        else:
            #print("Bajar dron")
            if operador:
                self.instruccion2()
                self.ui.labelComandosMentales.setText("-SI- se alcanzo el umbral bajar")
                self.contadorumbralMaximo = self.contadorumbralMaximo + 1
                self.contadorumbral = 0
            else:
                self.ui.labelComandosMentales.setText("-No- se alcazo el umbral")
                self.contadorumbral = self.contadorumbral + 1
                self.contadorumbralMaximo = 0

        #Umbral Inteligente
        #print("El valor del contador bajar es: "+str(self.contadorumbral))
        #print("El valor del contador subir es: "+str(self.contadorumbralMaximo))
        if self.contadorumbral == 5:
            self.bajarumbral()
            self.contadorumbral = 0


        elif self.contadorumbralMaximo == 5:
            self.elevarumbral()
            self.contadorumbralMaximo = 0


    def cargarCbPacientes(self):

        pacientes =  self.modeloPaciente.recuperarPacientes()
        #print(str(pacientes))
        #print(terapeutas)

        combo = self.ui.cbPaciente
        combo.clear()
        combo.addItem("Todos")
        combo.addItems([str(x[1])+" "+str(x[2])+" "+str(x[0]) for x in pacientes])

    def cargarCbEjercicios(self):

        ejercicios =  self.modeloEjercicios.recuperarEjercicios()
        #print(str(ejercicios))
        #print(terapeutas)

        combo = self.ui.cbEjercicio
        combo.clear()
        combo.addItem("Todos")
        combo.addItems([str(x[1]) for x in ejercicios])

    def abrirCapturarObservaciones(self):

        self.abrir = Controlador_Observaciones()
        self.abrir.show()
