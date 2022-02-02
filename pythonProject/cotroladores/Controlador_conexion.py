from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import websocket
import asyncio

from datetime import datetime
import json
import ssl
import time
import sys
from PyQt5.QtWidgets import QMessageBox
from vistas.conexion import Ui_Dialog
from PyQt5.QtGui import QIntValidator
import os
from time import sleep
#import threading

import matplotlib.pyplot as plt


from cotroladores.controlador_TerapiaTipoNeurofeedback import Controlador_TerapiaNeurofeeldback
from modelos.modeloParametros import Modelo_conexion
from cotroladores.classConexion import classConexion
import threading
from PyQt5.QtCore import QThread, pyqtSlot, pyqtSignal

#En esta clase se inserta codigo que permita a la vista realizar distintos comportamientos sin modificar el archivo principal de la vista



class Controlador_conexion(QtWidgets.QMainWindow):


    def __init__(self, electrodos, mdiArea):
        super().__init__()
        self.ui= Ui_Dialog()
        self.conexionClass = classConexion()
        self.modelo = Modelo_conexion()
        #electrodos['P7'] = True
        # Parametros necesarios
        #self.clientId = "L1eawU5ry1QItbMc8AokvIraebewehzRCyeIW4Ro"
        #self.clientSecret = "65jIP3680Y6qztv3uoKQyjihA4giZmsme0dzkyQUtdx5odLuO6jispNzIZO1I9PJpGad7tNbcDj8JuGUMWxOAlgzeqCLwpHNYkZw4Q0YgyeX3jXGEWUPGekcI28xcKzs"
        self.profile = "Heiler"
        # - - - - - - - - - - - - - - - - -
        self.url = "wss://localhost:6868"

        self.ui.setupUi(self)
        self.InicializarGui()
        #self.cargarParametris()
        self.dicionarioElectrodos = electrodos
        self.mdiArea =mdiArea


        '''
        # 1) Crear el objeto que se moverá a otro hiloa=
        self.mental_command = self.aplicarSeleccion(self.calidadElectrodo())
        # 2) Crear el hilo
        self.emotiv_thread = QThread()
        # 3) Mover el objeto al hilo
        self.mental_command.moveToThread(self.emotiv_thread)
        # 4) Conectar la señal del objeto con el slot de la interfaz gráfica
        self.mental_command.signalCommand.connect(self.actualizarProgressBar)
        # 5) Conectar la señal de inicio del método run del objeto dentro de otro hilo
        self.emotiv_thread.started.connect(self.mental_command.run)
        # 6) Iniciar el hilo
        self.emotiv_thread.start()
        '''

        #self.calidadElectrodo()




    def InicializarGui(self):

        self.ui.btnTerapiaNeurofeedback.clicked.connect(self.abrirTerapiaNeurofeedback)
        self.ui.btnEvaluarConexion.clicked.connect(self.evaluarConexion)
        self.ui.btnAplicarSelecion.clicked.connect(self.aplicarSeleccion)
        self.ui.lbAF3.setVisible(False)
        self.ui.lbAF4.setVisible(False)
        self.ui.lbF3.setVisible(False)
        self.ui.lbF4.setVisible(False)
        self.ui.lbFC5.setVisible(False)
        self.ui.lbFC6.setVisible(False)
        self.ui.lb01.setVisible(False)
        self.ui.lb02.setVisible(False)
        self.ui.lbT7.setVisible(False)
        self.ui.lbT8.setVisible(False)
        self.ui.lbP7.setVisible(False)
        self.ui.lbP8.setVisible(False)
        self.ui.lbF7.setVisible(False)
        self.ui.lbF8.setVisible(False)





    def evaluarConexion(self):
        a = True
        while a == True:
            if self.conectarServidor()== False:
                self.ui.label_4.setStyleSheet("background-color: rgb(255, 0, 0);")
                Alerta = QMessageBox.information(self, 'Alerta', "Fallo la conexion, revisa que la aplicacion de emotiv este instalada", QMessageBox.Ok)
                break
            elif self.validadInicioSesion()== False:
                self.ui.label_4.setStyleSheet("background-color: rgb(255, 0, 0);")
                Alerta = QMessageBox.information(self, 'Alerta', "Es necesario que inicies sesion en emotiv para continuar", QMessageBox.Ok)
                break
            elif self.solicitarPersmisos()== False:
                self.ui.label_4.setStyleSheet("background-color: rgb(255, 0, 0);")
                Alerta = QMessageBox.information(self, 'Alerta', "Acepta los acuerdos en la aplicacion de emotiv app, para continuar", QMessageBox.Ok)
                break
            elif self.obtenerToken() == False:
                self.ui.label_4.setStyleSheet("background-color: rgb(255, 0, 0);")
                Alerta = QMessageBox.information(self, 'Alerta', "Revisa tu conexion a internet y que las credenciales de tu cuenta de emotiv sean correctas", QMessageBox.Ok)
                break
            elif self.obtenerHeadset() == False:
                self.ui.label_4.setStyleSheet("background-color: rgb(255, 0, 0);")
                Alerta = QMessageBox.information(self, 'Alerta', "Se detecto un problema con la deadema... Verfica que la diadema este conectada correctamente", QMessageBox.Ok)
                break
            elif self.crearSesion() == False:
                self.ui.label_4.setStyleSheet("background-color: rgb(255, 0, 0);")
                Alerta = QMessageBox.information(self, 'Alerta', "Problemas al iniciar sesión con el dispositivo en Cortex", QMessageBox.Ok)
                break
            else:
                self.ui.label_4.setStyleSheet("background-color: rgb(41, 226, 69);")
                Alerta = QMessageBox.information(self, 'Alerta', "Conexion Exitosa", QMessageBox.Ok)
                self.ui.btnAplicarSelecion.setEnabled(True)
                break


    def conectarServidor(self):
        resConecServer = self.conexionClass.conectar()
        print(str(resConecServer))
        return resConecServer

    def validadInicioSesion(self):
        valSesion = self.conexionClass.validarInicioSesion()
        print(str(valSesion))
        return valSesion

    def solicitarPersmisos(self):
        solPermisos = self.conexionClass.solicitarPermisos()
        print(str(solPermisos))
        return solPermisos

    def obtenerToken(self):
        token = self.conexionClass.obtenerToken()
        print(str(token))
        return token

    def obtenerHeadset(self):
        Headset = self.conexionClass.recuperarDeadema()
        print(str(Headset))
        return Headset

    def crearSesion(self):
        sesion = self.conexionClass.crearSesion()
        print(str(sesion))
        return sesion

    def cargarParametris(self):

        datos = self.modelo.cargarDatos()

        ListaDatos = datos[0]

        print("Los datos son los siguientes: ")
        print(str(datos))

    def calidadElectrodo(self):
        result = self.conexionClass.suscribirseDEV()
        calidadElectrodo = json.loads(result) #Utilizar Com
        print("Todos los datos: "+str(calidadElectrodo))
        calElectrodo = calidadElectrodo["dev"][2]
        print("la calidad es: "+str(calElectrodo))
        a=0

        return calElectrodo



    def aplicarSeleccion(self):
        lbAF3  = self.ui.lbAF3
        lbAF4  = self.ui.lbAF4
        lbF3  = self.ui.lbF3
        lbF4  = self.ui.lbF4
        lbFC5  = self.ui.lbFC5
        lbFC6  = self.ui.lbFC6
        lb01  = self.ui.lb01
        lb02  = self.ui.lb02
        lbT7  = self.ui.lbT7
        lbT8  = self.ui.lbT8
        lbP7  = self.ui.lbP7
        lbP8  = self.ui.lbP8
        lbF7  = self.ui.lbF7
        lbF8  = self.ui.lbF8
        listaElectrodos = [lbAF3,lbF7,lbF3,lbFC5,lbT7,lbP7,lb01,lb02,lbP8,lbT8,lbFC6,lbF4,lbF8,lbAF4,lbF8]


        AF3  = self.ui.cbAF3
        AF4  = self.ui.cbAF4
        F3  = self.ui.cbF3
        F4  = self.ui.cbF4
        FC5  = self.ui.cbFC5
        FC6  = self.ui.cbFC6
        E01  = self.ui.cb01
        E02  = self.ui.cb02
        T7  = self.ui.cbT7
        T8  = self.ui.cbT8
        P7  = self.ui.cbP7
        P8  = self.ui.cbP8
        F7  = self.ui.cbF7
        F8  = self.ui.cbF8
        listaChecables = [AF3,F7,F3,FC5,T7,P7,E01,E02,P8,T8,FC6,F4,F8,AF4]
        listaNombreElectrodo = ["AF3","F7","F3","FC5","T7","P7","E01","E02","P8","T8","FC6","F4","F8","AF4"]
        a=0
        contadorParaDesabilitarTerapiaNeuro = 0
        for i in listaChecables:
            print("I es igual a :"+str())
            #print(a)
            if i.isChecked():
                listaElectrodos[a].setVisible(True)
                self.dicionarioElectrodos[listaNombreElectrodo[a]] = True
                self.ui.btnTerapiaNeurofeedback.setEnabled(True)

            else:
                listaElectrodos[a].setVisible(False)
                contadorParaDesabilitarTerapiaNeuro = contadorParaDesabilitarTerapiaNeuro +1
            a=a+1

            if contadorParaDesabilitarTerapiaNeuro == 14:
                self.ui.btnTerapiaNeurofeedback.setEnabled(False)

        b = 0
        calElectrodo = self.calidadElectrodo()
        #print("El resultado calE ---> "+str(calElectrodo))
        for i in calElectrodo:
            #print("Soy i: "+str(i))
            #print("Soy a:"+str(b))
            if i == 0:
                listaElectrodos[b].setStyleSheet("image: url(:/newPrefix/circuloGris.png);")
            elif i == 1:
                listaElectrodos[b].setStyleSheet("image: url(:/newPrefix/circuloRojo.png);")
            elif i == 2:
                listaElectrodos[b].setStyleSheet("image: url(:/newPrefix/circuloAnaranjado.png);")
            elif i == 4:
                listaElectrodos[b].setStyleSheet("image: url(:/newPrefix/circuloVerde.png);")

            else:
                print("Hola XD")
            b=b+1

    def abrirTerapiaNeurofeedback(self):
            self.abrir = QtWidgets.QDialog()
            self.abrir = Controlador_TerapiaNeurofeeldback(self.dicionarioElectrodos)
            self.mdiArea.addSubWindow(self.abrir)
            self.abrir.show()

