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

import matplotlib.pyplot as plt



from modelos.modeloParametros import Modelo_conexion
from cotroladores.classConexion import classConexion
import threading


#En esta clase se inserta codigo que permita a la vista realizar distintos comportamientos sin modificar el archivo principal de la vista



class Controlador_conexion(QtWidgets.QMainWindow):



    def __init__(self):
        super().__init__()

        self.ui= Ui_Dialog()
        self.conexionClass = classConexion()
        self.modelo = Modelo_conexion()

        # Parametros necesarios
        #self.clientId = "L1eawU5ry1QItbMc8AokvIraebewehzRCyeIW4Ro"
        #self.clientSecret = "65jIP3680Y6qztv3uoKQyjihA4giZmsme0dzkyQUtdx5odLuO6jispNzIZO1I9PJpGad7tNbcDj8JuGUMWxOAlgzeqCLwpHNYkZw4Q0YgyeX3jXGEWUPGekcI28xcKzs"
        self.profile = "Heiler"
        # - - - - - - - - - - - - - - - - -
        self.url = "wss://localhost:6868"

        self.ui.setupUi(self)
        self.InicializarGui()
        self.cargarParametris()



    def InicializarGui(self):

        #self.ui.btnEvaluarConexion.clicked.connect(self.evaluarConexion)
        self.ui.btnEvaluarConexion.clicked.connect(self.evaluarConexion)
        self.ui.btSelElectrodos.clicked.connect(self.aplicarSeleccion)
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
                Alerta = QMessageBox.information(self, 'Alerta', "Conexion Exitosa", QMessageBox.Ok)
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
        listaElectrodos = [lbAF3,lbAF4,lbF3,lbF4,lbFC5,lbFC6,lb01,lb02,lbT7,lbT8,lbP7,lbP8,lbF7,lbF8,lbF8]


        cbAF3  = self.ui.cbAF3
        cbAF4  = self.ui.cbAF4
        cbF3  = self.ui.cbF3
        cbF4  = self.ui.cbF4
        cbFC5  = self.ui.cbFC5
        cbFC6  = self.ui.cbFC6
        cb01  = self.ui.cb01
        cb02  = self.ui.cb02
        cbT7  = self.ui.cbT7
        cbT8  = self.ui.cbT8
        cbP7  = self.ui.cbP7
        cbP8  = self.ui.cbP8
        cbF7  = self.ui.cbF7
        cbF8  = self.ui.cbF8
        listaChecables = [cbAF3,cbAF4,cbF3,cbF4,cbFC5,cbFC6,cb01,cb02,cbT7,cbT8,cbP7,cbP8,cbF7,cbF8]
        a=0
        for i in listaChecables:
            print(i)
            print(a)
            if i.isChecked():
                listaElectrodos[a].setVisible(True)
            else:
                listaElectrodos[a].setVisible(False)
            a=a+1


        result = self.conexionClass.suscribirseDEV()
        calidadElectrodo = json.loads(result) #Utilizar Com
        print("Todos los datos: "+str(calidadElectrodo))
        calElectrodo = calidadElectrodo["dev"][2]
        print("la calidad es: "+str(calElectrodo))
        a=0
        for i in calElectrodo:
            #print(i)
            #print(a)
            if i == 0:
                listaElectrodos[a].setStyleSheet("image: url(:/newPrefix/circuloGris.png);")
            elif i == 1:
                listaElectrodos[a].setStyleSheet("image: url(:/newPrefix/circuloRojo.png);")
            elif i == 2:
                listaElectrodos[a].setStyleSheet("image: url(:/newPrefix/circuloAnaranjado.png);")
            elif i == 4:
                listaElectrodos[a].setStyleSheet("image: url(:/newPrefix/circuloVerde.png);")
            a=a+1


'''
    def actualizarProgresBar(self):

        a= self.generarConexion()
        b= a*100
        self.ui.progressBar_4.setProperty("value", b)
        self.ui.label_3.setText(str(b)+"%")
'''

