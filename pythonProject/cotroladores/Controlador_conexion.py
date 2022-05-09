from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import websocket
import asyncio
import webbrowser
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
import threading

import matplotlib.pyplot as plt


from cotroladores.controlador_TerapiaTipoNeurofeedback import Controlador_TerapiaNeurofeeldback
from modelos.modeloParametros import Modelo_conexion
from cotroladores.classConexion import classConexion

#Pruebas de conexion
from cotroladores.pruebaEmotivList import pruebaconexionEmotiv
import threading
from PyQt5.QtCore import QThread, pyqtSlot, pyqtSignal

#En esta clase se inserta codigo que permita a la vista realizar distintos comportamientos sin modificar el archivo principal de la vista



class Controlador_conexion(QtWidgets.QMainWindow):


    def __init__(self, electrodos, mdiArea, user):
        super().__init__()
        self.ui= Ui_Dialog()
        self.conexionClass = classConexion()
        self.modelo = Modelo_conexion()



        self.profile = "Heiler"
        # - - - - - - - - - - - - - - - - -
        self.url = "wss://localhost:6868"

        self.ui.setupUi(self)
        self.InicializarGui()
        #self.cargarParametris()
        self.dicionarioElectrodos = electrodos
        self.mdiArea =mdiArea
        self.user = user

        #Clase de pruebas
        self.emotiv = pruebaconexionEmotiv(self.dicionarioElectrodos, "Alfa")

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
        self.ui.commandLinkButton.clicked.connect(self.abrirPaginaDeErrores)
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
        if self.conectarServidor()== False:
            self.ui.label_4.setStyleSheet("background-color: rgb(255, 0, 0);")
            Alerta = QMessageBox.information(self, 'Alerta', "Fallo la conexion, revisa que la aplicacion de emotiv este instalada", QMessageBox.Ok)


        elif self.validadInicioSesion() != True:
             self.ui.label_4.setStyleSheet("background-color: rgb(255, 0, 0);")
             Alerta = QMessageBox.information(self, 'Alerta', "Es necesario que inicies sesion en emotiv para continuar", QMessageBox.Ok)
             self.ui.teErrores.setText("Probemas con el inicio de sesion, comprueva que tu inicio de sesion este activo o vuelve a iniciar sesion")

        elif self.solicitarPersmisos()!= True:
            self.ui.label_4.setStyleSheet("background-color: rgb(255, 0, 0);")
            Alerta = QMessageBox.information(self, 'Alerta', "Acepta los acuerdos en la aplicacion de emotiv app, para continuar", QMessageBox.Ok)
            self.ui.teErrores.setText("Verifica que hayas concedido permisos en la aplicacion emotiv app, en la parte final de la pestaña apps")

        elif self.obtenerToken() !=True:
            self.ui.label_4.setStyleSheet("background-color: rgb(255, 0, 0);")
            error = self.emotiv.obteunerToken()
            Alerta = QMessageBox.information(self, 'Alerta', "Error: "+str(error)+ ". Verifica tu conexion a internet y tus credenciales de emotiv", QMessageBox.Ok)
            self.ui.teErrores.setText("Error: "+str(error)+ ".Verifica que tu conenexion a internet sea estable, que tus credenciales de emotiId "
                                                            "y passwordId sean correctas, asi como que tu licencia de emotiv sea vigente")
        elif self.obtenerHeadset() != True:
            self.ui.label_4.setStyleSheet("background-color: rgb(255, 0, 0);")
            Alerta = QMessageBox.information(self, 'Alerta', "Se detecto un problema con la deadema... Verfica que la diadema este conectada correctamente", QMessageBox.Ok)
            self.ui.teErrores.setText("Revisa que la deadema este conectada. Algunos de lo posibles errores son: La deadema esta apagada, desconectada, fuera del"
                                      "rango de alcance, la memoria de bluetooth esta desconectada")

        elif self.crearSesion() != True:
            self.ui.label_4.setStyleSheet("background-color: rgb(255, 0, 0);")
            Alerta = QMessageBox.information(self, 'Alerta', "Ocurrio un problrma al iniciar sesión con el servidor...", QMessageBox.Ok)
            self.ui.teErrores.setText("Verifica que tu conexion a internet este estable y la deadema la deadema este conectada con bateria mayor a 20%. Para mayor información solicitar apoyo"
                                      "de un tecnico especializado de cognidron EEG")

        else:
            self.ui.label_4.setStyleSheet("background-color: rgb(41, 226, 69);")
            Alerta = QMessageBox.information(self, 'Conformación', "Conexion Exitosa", QMessageBox.Ok)
            self.ui.btnAplicarSelecion.setEnabled(True)
            self.ui.teErrores.setText("Se ha validado la conexió con el servidor y la deadema EEG")



    def conectarServidor(self):
        resConecServer = self.emotiv.conectar()
        print(str(resConecServer))
        return resConecServer

    def validadInicioSesion(self):
        valSesion = self.emotiv.validarInicioSesion()
        print(str(valSesion))
        return valSesion

    def solicitarPersmisos(self):
        solPermisos = self.emotiv.solicitarPermisos()
        print(str(solPermisos))
        return solPermisos

    def obtenerToken(self):
        token = self.emotiv.obteunerToken()
        print(str(token))
        return token

    def obtenerHeadset(self):
        Headset = self.emotiv.recuperarDeademaEEG()
        print(str(Headset))
        return Headset

    def crearSesion(self):
        sesion = self.emotiv.crearSesion()
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
            self.abrir = Controlador_TerapiaNeurofeeldback(self.dicionarioElectrodos, self.user)
            self.mdiArea.addSubWindow(self.abrir)
            self.abrir.show()

    def abrirPaginaDeErrores(self, event):
        try:
            webbrowser.open('https://emotiv.gitbook.io/cortex-api/error-codes')
        except:
            Alerta = QMessageBox.information(self, 'Alerta', "Lo siento el link caido... Busca la pagina de errores de la empresa emotiv :D", QMessageBox.Ok)


