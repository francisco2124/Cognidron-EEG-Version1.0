from PyQt5 import QtWidgets, QtCore
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

from PyQt5.QtGui import QIntValidator
import os
from playsound import playsound

from cotroladores.controladorDron import Dron

#En esta clase se inserta codigo que permita a la vista realizar distintos comportamientos sin modificar el archivo principal de la vis
import sys


import random
from PyQt5.QtCore import QThread, pyqtSlot, pyqtSignal

class Controlador_TerapiaNeurofeedback(QtWidgets.QMainWindow):


    def __init__(self):
        super().__init__()
        self.ui = Ui_TerapiaNeurofeedback()
        self.ui.setupUi(self)
        self.inicializarGUI()
        self.posX = 310
        self.posY = 500
        self.ancho = 141
        self.alto = 101
        self.hilo = HiloDuracion;
        self.puntaje = 0
        self.Umbral = 0
        self.contadorumbral =0
        self.contadorumbralMaximo =0

        #modelos
        self.modeloPaciente = Modelo_Paciente_()
        self.modeloEjercicios = Modelo_Ejercicios()

        #Funciones
        self.cargarCbPacientes()
        self.cargarCbEjercicios()




    def inicializarGUI(self):

        self.ui.btnIniciarTerapia.setEnabled(True)
        self.ui.labelEventoDrone.setText("")
        self.ui.label.setText("")
        self.ui.labelComandosMentales.setText("")
        self.ui.proBarTiempoSesion.setStyleSheet("QProgressBar::chunk "
                                            "{"
                                            "background-color: rgb(170, 170, 255);"
                                            "}")

        #Controles de emergencia del dron
        self.ui.btnObtenerDrone.clicked.connect(self.obtenerControlDrone)

        self.ui.btnDecenderDrone.clicked.connect(self.decenderDrone)
        self.ui.btnDerechaDrone.clicked.connect(self.derechaDrone)
        self.ui.btnIsquierdaDrone.clicked.connect(self.izquierdaDrone)
        self.ui.btnAdelanteDrone.clicked.connect(self.adelanteDrone)
        self.ui.btnAtrasDrone.clicked.connect(self.atrasDrone)

        self.ui.btnElevarDrone.clicked.connect(self.despegarDrone)
        self.ui.btnAterrizarDrone.clicked.connect(self.aterrizarDrone)
        self.ui.btnPausar.clicked.connect(self.finalizarTerapia)


        #Botones basicos de la sesion
        self.ui.btnIniciarTerapia.clicked.connect(self.iniciarTerapia)
        self.ui.btnDetener.clicked.connect(self.deternerTipoDuracion)
        self.ui.btnResumen.clicked.connect(self.reanudarTipoDuracion)
        #.ui.btnResumen.clicked.connect(self.iniciarBarraProgreso)


        #Botones del umbral
        self.ui.spinBoxUmbral.setMinimum(5)
        self.ui.spinBoxUmbral.setMaximum(95)
        self.ui.spinBoxUmbral.valueChanged.connect(self.colocarumbral)
        self.ui.spinBoxUmbral.setSingleStep(5)
        self.ui.spinBoxUmbral.setValue(30)



    def iniciarTerapia(self):

            self.dron = Dron('192.168.10.1', 8889, "tello")

            pista = self.ui.cbPista.currentText()

            tiempo = tiempo = self.ui.cbTiempoSesion.currentText()

            if tiempo == "Sin Seleccion":
                Alerta = QMessageBox.information(self, 'Alerta', "Selecciona un una duracion de la sesion para iniciar la terapia", QMessageBox.Ok)

            elif pista != "Sin Pista":
                self.iniciarBarraProgreso(tiempo)

                self.activarBarraNeurofeedback()
                self.crearArchivoCSV()
                self.reproducirPista(pista)
                self.ejecutardron()
            else:
                self.iniciarBarraProgreso(tiempo)
                self.activarcuntaRegresiva(tiempo)
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

    def despegarDrone(self):
        print("llame la funcion elevar")
        self.dron.despegar()

    def aterrizarDrone(self):
        print("llame la funcion decender")
        self.dron.aterrizar()

    def adelanteDrone(self):

        self.ui.labelComandosMentales.setText("Dron hacia adelante")
        self.alto = self.alto - 5
        self.ancho = self.ancho - 5
        self.ui.label_11.setGeometry(QtCore.QRect(self.posX, self.posY, self.ancho, self.ancho))

    def atrasDrone(self):

        self.ui.labelComandosMentales.setText("Dron hacia atras")
        self.alto = self.alto  + 5
        self.ancho = self.ancho + 5
        self.ui.label_11.setGeometry(QtCore.QRect(self.posX, self.posY, self.ancho, self.ancho))

    def elevarDrone(self):
        self.posY = self.posY - 23
        self.ui.label_11.setGeometry(QtCore.QRect(self.posX, self.posY, self.ancho, self.alto))

    def decenderDrone(self):
        self.posY = self.posY + 23
        self.ui.label_11.setGeometry(QtCore.QRect(self.posX, self.posY, self.ancho, self.alto))

    def derechaDrone(self):
        self.posX = self.posX + 5
        self.ui.label_11.setGeometry(QtCore.QRect(self.posX, self.posY, 251, 281))

    def izquierdaDrone(self):
        self.posX = self.posX - 5
        self.ui.label_11.setGeometry(QtCore.QRect(self.posX, self.posY, 251, 281))

    #Controles de umbral ------------------------------------------------------------------------


    def colocarumbral(self):

        print(str(self.ui.spinBoxUmbral.value()))

        self.umbral = 570 - (int(self.ui.spinBoxUmbral.value()) * 4)
        self.ui.lbUmbral.setGeometry(QtCore.QRect(673, self.umbral, 161, 91))

    def bajarumbral(self):

        if self.ui.spinBoxUmbral.value() != 5:
            print(str(self.ui.spinBoxUmbral.value()))
            valor = self.ui.spinBoxUmbral.value() - 5
            self.ui.spinBoxUmbral.setValue(valor)

            self.umbral = 573 - (int(self.ui.spinBoxUmbral.value()) * 4)
            self.ui.lbUmbral.setGeometry(QtCore.QRect(673, self.umbral, 161, 91))
        else:
            print("Umbral Minimo")

    def elevarumbral(self):

        if self.ui.spinBoxUmbral.value() != 95:
            print(str(self.ui.spinBoxUmbral.value()))
            valor = self.ui.spinBoxUmbral.value() + 5
            self.ui.spinBoxUmbral.setValue(valor)

            self.umbral = 573 - (int(self.ui.spinBoxUmbral.value()) * 4)
            self.ui.lbUmbral.setGeometry(QtCore.QRect(673, self.umbral, 161, 91))
        else:
            print("Umbral Maximo")


    #Metodos con hilos

    def iniciarBarraProgreso(self,tiempo):

        self.valTiempo = 0

        print(tiempo)
        if tiempo == "1 Minuto":
            print("Duarara 1 minuto")
            self.valTiempo = 0.6
        elif tiempo == "5 Minutos":
            print("Duarara 5 minutos")
            self.valTiempo = 3
        elif tiempo == "10 Minutos":
            print("Duarara 10 minutos")
            self.valTiempo = 6
        elif tiempo == "15 Minutos":
            print("Duarara 15 minutos")
            self.valTiempo = 9
        elif tiempo == "20 Minutos":
            print("Duarara 20 minutos")
            self.valTiempo = 12
        elif tiempo == "25 Minutos":
            print("Duarara 25 minutos")
            self.valTiempo = 15
        else:
            print("Seleceiona un opcion")

        if self.valTiempo != 0:
            self.hilo = HiloDuracion(self.valTiempo)
            self.hilo.signDS.connect(self.actualizarDuracion)
            self.hilo.start()



        else:
            Alerta = QMessageBox.information(self, 'Alerta', "Selecciona el tiempo de duracion de la sesion", QMessageBox.Ok)

    def deternerTipoDuracion(self):

        self.hilo.detener()
        self.ui.label_11.setText(str(self.hilo.estadoHilo()))
    def reanudarTipoDuracion(self):

        self.hilo.reanudar()
        self.ui.label_11.setText(str(self.hilo.estadoHilo()))

    def finalizarTerapia(self):
        del(self.dron)

    def actualizarDuracion(self,val):
        #print("b", str(val))
        self.ui.proBarTiempoSesion.setValue(val)



    def activarBarraNeurofeedback(self):
        #self.hilo2 = conexionEmotiv()
        self.hilo2 = HiloSingsEotiv()
        #self.hilo2.signEmotiv.connect(self.barraNeurofeedback)
        self.hilo2.signDS.connect(self.barraNeurofeedback)
        self.hilo2.start()

    def barraNeurofeedback(self,val):

        #val = val*1000
        #print("la potencia de la barra es", str(val))
        self.ui.progressBar_4.setValue(val)



    def activarcuntaRegresiva(self, tiempo):
        valTiempo = 0

        print(tiempo)
        if tiempo == "1 Minuto":
            print("Duarara 1 minuto")
            valTiempo = 1
        elif tiempo == "5 Minutos":
            print("Duarara 5 minutos")
            valTiempo = 5
        elif tiempo == "10 Minutos":
            print("Duarara 10 minutos")
            valTiempo = 10
        elif tiempo == "15 Minutos":
            print("Duarara 15 minutos")
            valTiempo = 15
        elif tiempo == "20 Minutos":
            print("Duarara 20 minutos")
            valTiempo = 20
        elif tiempo == "25 Minutos":
            print("Duarara 25 minutos")
            valTiempo = 25
        else:
            print("Seleceiona un opcion")

        if self.valTiempo != 0:
            self.hiloreloj = HiloDuracionReloj(valTiempo)
            self.hiloreloj.signDSReloj.connect(self.cuentaRegresiva)
            self.hiloreloj.start()

        else:
            Alerta = QMessageBox.information(self, 'Alerta', "Selecciona el tiempo de duracion de la sesion", QMessageBox.Ok)

    def cuentaRegresiva(self,tiempo):
        #print("Desde  la clase: "+repr(tiempo))
        self.ui.lbMinutos.setText(tiempo)

    def crearArchivoCSV(self):
        archivo = open("archivo.csv","w")
        #Titulo
        archivo.write("Reporte de potencias")
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

        potencias = [20.2,30.2,10.12,40.56,50,78,20.2,30.2,10.12,40.56,50,78,20.2,30.2,10.12,40.56,50,78]

        for i in potencias:

            archivo.write("\n")
            archivo.write("F3")
            archivo.write(",")
            archivo.write("Theta")
            archivo.write(",")
            archivo.write(str(i))
            archivo.write(",")
            archivo.write("001")
            archivo.write(",")
            archivo.write("Inivitorio")


    #Movimiento del dron
    def ejecutardron(self):
        #self.hilodron = conexionEmotiv()
        self.hilodron = HiloSingsEotiv()
        #self.hilodron.signEmotiv.connect(self.movimientoDron)
        self.hilodron.signDS.connect(self.movimientoDron)
        self.hilodron.start()

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

        if self.posY == 500:

            if self.puntaje !=0 and self.puntaje%2 != 0:
                self.puntaje = self.puntaje +1
                self.ui.label_18.setText(str(self.puntaje))
            #direccion
            self.val = True

        elif self.posY == 270:
            if self.puntaje%2 == 0  or self.puntaje == 0:
                self.puntaje = self.puntaje +1
                self.ui.label_18.setText(str(self.puntaje))
            self.val = False

        #Comparacion de umbral deacurdo al tipo ejercicio
        if self.val == True:

            #print("Elevar dron")
            if operador:
                self.elevarDrone()
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
                self.decenderDrone()
                self.ui.labelComandosMentales.setText("-SI- se alcanzo el umbral bajar")
                self.contadorumbralMaximo = self.contadorumbralMaximo + 1
                self.contadorumbral = 0
            else:
                self.ui.labelComandosMentales.setText("-No- se alcazo el umbral")
                self.contadorumbral = self.contadorumbral + 1
                self.contadorumbralMaximo = 0

        #Umbral Inteligente
        print("El valor del contador bajar es: "+str(self.contadorumbral))
        print("El valor del contador subir es: "+str(self.contadorumbralMaximo))
        if self.contadorumbral == 5:
            self.bajarumbral()
            self.contadorumbral = 0


        elif self.contadorumbralMaximo == 5:
            self.elevarumbral()
            self.contadorumbralMaximo = 0


    def cargarCbPacientes(self):

        pacientes =  self.modeloPaciente.recuperarPacientes()
        print(str(pacientes))
        #print(terapeutas)

        combo = self.ui.cbPaciente
        combo.clear()
        combo.addItem("Todos")
        combo.addItems([str(x[1])+" "+str(x[2])+" "+str(x[0]) for x in pacientes])

    def cargarCbEjercicios(self):

        ejercicios =  self.modeloEjercicios.recuperarEjercicios()
        print(str(ejercicios))
        #print(terapeutas)

        combo = self.ui.cbEjercicio
        combo.clear()
        combo.addItem("Todos")
        combo.addItems([str(x[1]) for x in ejercicios])

