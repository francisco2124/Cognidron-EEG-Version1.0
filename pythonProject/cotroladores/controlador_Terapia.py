from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from vistas.terapia import Ui_Dialog
from PyQt5.QtGui import QIntValidator



#En esta clase se inserta codigo que permita a la vista realizar distintos comportamientos sin modificar el archivo principal de la vis
import sys


import random
from PyQt5.QtCore import QThread, pyqtSlot, pyqtSignal

class Controlador_Terapia(QtWidgets.QMainWindow):


    color = {1:"red", 2:"blue", 3:"green", 4:"brown"}
    isEmotivWorking = False

    signalCommand = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.gui = Ui_Dialog()
        self.gui.setupUi(self)
        self.isDroneConnected = False
        self.emotiv = Emotiv()

        # 1) Crear el objeto que se moverá a otro hilo
        self.mental_command = MentalCommands(self.emotiv)
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


        # 1) Crear el objeto que se moverá a otro hilo
        self.dron = Drone()
        # 2) Crear el hilo
        self.dron_thread = QThread()
        # 3) Mover el objeto al hilo
        self.dron.moveToThread(self.dron_thread)
        # 4) Conectar la señal del objeto con el slot de la interfaz gráfica
        self.signalCommand.connect(self.dron.command)
        # 5) Conectar la señal de inicio del método run del objeto dentro de otro hilo
        #self.dron_thread.started.connect(self.dron.run)
        # 6) Iniciar el hilo
        self.dron_thread.start()



        self.inicializarGUI()

    def inicializarGUI(self):
        self.gui.labelEventoDrone.setText("")
        self.gui.label.setText("")
        self.gui.labelComandosMentales.setText("")
        self.gui.progressBar.setStyleSheet("QProgressBar::chunk "
                                            "{"
                                            "background-color: rgb(170, 170, 255);"
                                            "}")

        self.gui.progressBar_4.setStyleSheet("QProgressBar::chunk "
                                           "{"
                                           "background-color: rgb(255, 85, 0);"
                                           "}")

        self.gui.btnEnviarIstruccion.clicked.connect(self.mensaje1)
        self.gui.btnActivarEmotiv.clicked.connect(self.mensaje4)
        self.gui.btnActivarDrone.clicked.connect(self.activarDron)
        #self.gui.btnElevarDrone.clicked.connect(self.actualizarProgressBar)

    def mensaje1(self):
        if len(self.gui.lbl_terapeutas.text())==0:
            self.gui.lbl_terapeutas.setText("Abriendo ventana...")
        else:
            self.gui.lbl_terapeutas.setText("")






    @pyqtSlot(str)

    def actualizarProgressBar(self, command):

        a = float(command)
        print(command)
        b = a*100
        self.gui.progressBar_4.setProperty("value", b)

        if b > 6.0:

            self.gui.label_11.setStyleSheet("image: url(:/newPrefix/EjerDecender.png);")
        else:
            self.gui.label_11.setStyleSheet("image: url(:/newPrefix/EjerElevar.png);")

    def mensaje2(self, command):
        self.gui.labelComandosMentales.setStyleSheet("color:{}".format(self.color[random.randint(1,4)]))
        self.gui.labelComandosMentales.setText(command)
        print(command)
        self.mensaje3()

    def activarDron(self):
        if self.isEmotivWorking:
            if self.gui.btnActivarDrone.text() == "Activar Dron":
                self.gui.btnActivarDrone.setText("Desactivar Dron")
            else:
                self.gui.btnActivarDrone.setText("Activar Dron")
                self.gui.labelEventoDrone.setText("")

        else:
            self.gui.labelEventoDrone.setText("Primero activa Emotiv...")


    def mensaje3(self):
        if self.isEmotivWorking==True and self.gui.btnActivarDrone.text() == "Desactivar Dron":
            command = self.gui.labelComandosMentales.text()
            if len(command)>0:
                self.gui.labelEventoDrone.setStyleSheet("color:{}".format(self.color[random.randint(1,4)]))
                if command=="push":
                    self.gui.labelEventoDrone.setText("Elevar Drone")
                    self.signalCommand.emit("Dron avanza")
                    self.gui.label_11.setStyleSheet("image: url(:/newPrefix/EjerElevar.png);")
                elif command=="left":
                    self.gui.labelEventoDrone.setText("Dron izquierda")
                    self.signalCommand.emit("Dron izquierda")
                    self.gui.label_11.setStyleSheet("image: url(:/newPrefix/EjerIzquierda.png);")
                elif command=="right":
                    self.gui.labelEventoDrone.setText("Dron derecha")
                    self.signalCommand.emit("Dron derecha")
                    self.gui.label_11.setStyleSheet("image: url(:/newPrefix/EjerDerecha.png);")
                elif command=="pull":
                    self.gui.labelEventoDrone.setText("Descender Drone")
                    self.signalCommand.emit("Dron retrocede")
                    self.gui.label_11.setStyleSheet("image: url(:/newPrefix/EjerDecender.png);")

    def mensaje4(self):
        if self.isEmotivWorking:
            self.isEmotivWorking = self.mental_command.stop()
            self.gui.labelComandosMentales.setText("")
            self.gui.btnActivarEmotiv.setText("Activar Emotiv")
        else:
            self.isEmotivWorking = self.mental_command.start()
            self.gui.btnActivarEmotiv.setText("Desactivar Emotiv")


#Esta clase deberá implementar rodos los método de Emotiv con excepción de el sensado de comandos mentales y en sensado de la bandas.
#Esas dos actividades deberán ser realizadas por otras cases que estarán trabajando en hilos secundarios de forma respectiva.
class Emotiv():

    def connect(self):
        return True


    def disconnect(self):
        return True

    def activateSensors(self,sensors):
        pass

    def getProfiles(self):
        pass




from PyQt5.QtCore import pyqtSignal, QObject
from time import sleep
import threading
import websocket
import json
import ssl

class MentalCommands(QObject):

    commands = {1:"push",2:"left",3:"right",4:"pull"}

    signalCommand = pyqtSignal(str)
    status = False

    def __init__(self,headset):
        super().__init__()
        """


        Parameters
        ----------
        headset : Emotiv
            DESCRIPTION. Esta clase permite sensar la actividad cerebral del pasiente y enviar el comando mental que corresponda según la actividad cerebral.

        Returns
        -------
        None.

        """
        # Parametros necesarios
        self.clientId = "L1eawU5ry1QItbMc8AokvIraebewehzRCyeIW4Ro"
        self.clientSecret = "65jIP3680Y6qztv3uoKQyjihA4giZmsme0dzkyQUtdx5odLuO6jispNzIZO1I9PJpGad7tNbcDj8JuGUMWxOAlgzeqCLwpHNYkZw4Q0YgyeX3jXGEWUPGekcI28xcKzs"
        self.profile = "heiler"
        # - - - - - - - - - - - - - - - - -
        self.url = "wss://localhost:6868"

        #self.ui.setupUi(self)
        #self.InicializarGui()
        self.evaluarConexion()


    def evaluarConexion(self):
        self.conectar()
        self.validarInicioSesion()
        self.solicitarPermisos()
        #self.generarConexion()



    def conectar(self):

        ws = websocket.create_connection(self.url,sslopt={"cert_reqs": ssl.CERT_NONE})

        print("-------------------------------------------------------")
        print("Conectando con cortex...: ")
        msg = """{
            "id": 1,
            "jsonrpc": "2.0",
            "method": "getCortexInfo"
        }"""
        ws.send(msg)

        print("--------------------------------------------------------")
        result = ws.recv()
        print("Se recupera lo siguiente: " + str(result))
        print("--------------------------------------------------------")


        resuladoFallido = '''{"id":1,"jsonrpc":"2.0","result":{"buildDate":"2020-09-08T12:06:34","buildNumber":"v2.2.3-659-gfa6e645","version":"2.6.0.105"}}'''
        print(resuladoFallido)
        if result != resuladoFallido:
            print("Fallo la conexion istala la aplicacion de emotiv")
        # self.ui.label_4.setStyleSheet("background-color: rgb(255, 0, 0);")
        else:
            print("Conctado con cortex")

    def validarInicioSesion(self):

        ws = websocket.create_connection(self.url,sslopt={"cert_reqs": ssl.CERT_NONE})

        print("-------------------------------------------------------")
        print("Validar inicio de sesion del usuario...: ")
        msg = """{
            "id": 1,
            "jsonrpc": "2.0",
            "method": "getUserLogin"
    }"""
        ws.send(msg)

        print("--------------------------------------------------------")
        result = ws.recv()
        print("Se recupera lo siguiente: " + str(result))
        print("--------------------------------------------------------")


        resuladoFallido = '''{"id":1,"jsonrpc":"2.0","result":[]}'''
        print(resuladoFallido)
        if result == resuladoFallido:
            print("Fallo la conexion istala la aplicacion de emotiv")
            Alerta = QMessageBox.information(self, 'Alerta', "Es necesario que inicies sesion en emotiv para continuar", QMessageBox.Ok)
        # self.ui.label_4.setStyleSheet("background-color: rgb(255, 0, 0);")
        else:
            print("Inicio de sesion correcto")
        # self.ui.label_4.setStyleSheet("background-color: rgb(41, 226, 69);")


    def solicitarPermisos(self):

        ws = websocket.create_connection(self.url,sslopt={"cert_reqs": ssl.CERT_NONE})



        print("-------------------------------------------------------")
        print("Pedir permisios al usuario usuario...: ")
        msg = """{
                            "id": 1,
                            "jsonrpc": "2.0",
                            "method": "requestAccess",
                            "params": {
                                "clientId": "%s",
                                "clientSecret": "%s"
                            }
                        }""" % (self.clientId, self.clientSecret)
        ws.send(msg)

        print("--------------------------------------------------------")
        result = ws.recv()
        print("Se recupera lo siguiente: " + str(result))
        print("--------------------------------------------------------")


        resuladoFallido = '''{
            "id": 1,
            "jsonrpc": "2.0",
            "result": {
                "accessGranted":false,
                "message":"The User has not granted access right to this application. Please use Emotiv App to proceed."
            }
        }'''
        print(resuladoFallido)
        if result == resuladoFallido:
            print("No has aceptado el mensaje de emoyiv")
            Alerta = QMessageBox.information(self, 'Alerta', "Acepta los aurdos en la aplicacion de emotiv app, para continuar", QMessageBox.Ok)
            #self.ui.label_4.setStyleSheet("background-color: rgb(255, 0, 0);")
        else:
            print("Inicio de sesion correcto")
            #self.ui.label_4.setStyleSheet("background-color: rgb(41, 226, 69);")



    def generarConexion(self):

        #Pasos relacionado con la conexion del emotiv

        ws = websocket.create_connection(self.url,sslopt={"cert_reqs": ssl.CERT_NONE})

        profile = "Francisco"
        print("-------------------------------------------------------")
        print("Obtener Token...: ")
        msg = """{
                            "id": 1,
                            "jsonrpc": "2.0",
                            "method": "authorize",
                            "params": {
                                "clientId": "%s",
                                "clientSecret": "%s"
                            }
                        }""" % (self.clientId, self.clientSecret)
        ws.send(msg)

        print("--------------------------------------------------------")
        result = ws.recv()
        print("Se recupera lo siguiente: " + str(result))
        print("--------------------------------------------------------")


        resuladoFallido = '''{"error":{"code":-32102,"message":"You have no access rights to the Application."},"id":1,"jsonrpc":"2.0"}'''
        print(resuladoFallido)
        if result == resuladoFallido:
            print("Fallo la conexion... Revisa tu conexion a internet")
            Alerta = QMessageBox.information(self, 'Alerta', "Error en las credenciales verifica su autenticidad", QMessageBox.Ok)
            self.ui.label_4.setStyleSheet("background-color: rgb(255, 0, 0);")
        else:
            print("Inicio de sesion correcto")
            #self.ui.label_4.setStyleSheet("background-color: rgb(41, 226, 69);")

        dic = json.loads(result)
        print("El diccionario es: "+str(dic))
        print("--------------------------------------------------------")
        token = dic["result"]["cortexToken"]
        print("token es: ", token)
        #**************************************************************************
        print("-------------------------------------------------------")
        print("Ver diademas conectadas...: ")
        msg = """{"jsonrpc": "2.0", 
                            "method": "queryHeadsets",
                            "params": {},
                            "id": 1
                        }"""
        ws.send(msg)

        print("--------------------------------------------------------")
        result = ws.recv()
        print("Se recupera lo siguiente: " + result)
        print("--------------------------------------------------------")
        if 'dongle' in result:
            dic = json.loads(result)
            headset = dic["result"][0]["id"]  # Obtener el ID de la diadema
            print("id de la deadema es: ", headset)
            #self.ui.label_4.setStyleSheet("background-color: rgb(41, 226, 69);")
        else:
            print("Error: No hay ningun diadema conectada")
            Alerta = QMessageBox.information(self, 'Alerta', "Se detecto un problema con la deadema... Verfica que la diadema este conectada", QMessageBox.Ok)
            #self.ui.label_4.setStyleSheet("background-color: rgb(255, 0, 0);")



        #**************************************************************************
        print("-------------------------------------------------------")
        print("Crear Sesion...: ")
        msg = """{
                            "id": 1,
                            "jsonrpc": "2.0",
                            "method": "createSession",
                            "params": {
                                "cortexToken": "%s",
                                "headset": "%s",
                                "status": "open"
                            }
                        }""" % (token, headset)
        ws.send(msg)

        print("--------------------------------------------------------")
        result = ws.recv()
        print("Se recupera lo siguiente: " + result)


        if 'appId' in result:
            dic = json.loads(result)
            sesion = dic['result']['id']
            print("El ide de la sesion es: "+str(sesion))
        else:
            print("Error: Problemas al iniciar sesión con el dispositivo en Cortex")


        #**************************************************************************
        print("-------------------------------------------------------")
        print("Cargar un perfil...: ")
        msg = """{
                            "id": 1,
                            "jsonrpc": "2.0",
                            "method": "setupProfile",
                            "params": {
                                "cortexToken": "%s",
                                "headset": "%s",
                                "profile": "%s",
                                "status": "load"
                            }
                        }""" % (token, headset, profile)
        ws.send(msg)

        print("--------------------------------------------------------")
        result = ws.recv()
        print("Se recupera lo siguiente: " + result)

        #**************************************************************************
        print("-------------------------------------------------------")
        print("Suscribirse a los comandos mentales...: ")
        msg = """{
                            "id": 1,
                            "jsonrpc": "2.0",
                            "method": "subscribe",
                            "params": {
                                "cortexToken": "%s",
                                "session": "%s",
                                "streams": ["com"]
                            }
                        }""" % (token, sesion)
        ws.send(msg)

        print("--------------------------------------------------------")
        result = ws.recv()
        print("Se recupera lo siguiente: " + result)



        print("------------==============================-------------------------")
        result =ws.recv()
        print(result)




        """"
        while True:
            bucle = json.loads(ws.recv()) #Utilizar Com
            comandoMental = bucle["pow"]

            for i in listaElectrodos:
                a=a+1
                if i.isChecked():
                    electrodox = bucle["pow"][a-1]
                    print("Esta activada la potencia numero: "+str(a))
                    listapotencias.append(electrodox)
                else:
                    print("No esta activada la potencia numero: "+str(a))

            comandoMentalXElectrodo = listapotencias
            print(comandoMental)
            print(comandoMentalXElectrodo)
            listapotencias.clear()
            a=0"""


        super().__init__()
        self.headset = headset #Este atributo recibe la instancia que permite acceder a Emotiv
        print("Se ha creado una instancia de la clase MentalCommands.")


    def potenciaElectrodo(self):

        ws = websocket.create_connection(self.url,sslopt={"cert_reqs": ssl.CERT_NONE})

        profile = "Francisco"
        #print("Obtener Token...: ")
        msg = """{
                            "id": 1,
                            "jsonrpc": "2.0",
                            "method": "authorize",
                            "params": {
                                "clientId": "%s",
                                "clientSecret": "%s"
                            }
                        }""" % (self.clientId, self.clientSecret)
        ws.send(msg)

        result = ws.recv()
        dic = json.loads(result)
        token = dic["result"]["cortexToken"]


        #print("Ver diademas conectadas...: ")
        msg = """{"jsonrpc": "2.0", 
                            "method": "queryHeadsets",
                            "params": {},
                            "id": 1
                        }"""
        ws.send(msg)

        result = ws.recv()
        if 'dongle' in result:
            dic = json.loads(result)
            headset = dic["result"][0]["id"]  # Obtener el ID de la diadema
        else:
            pass

        #print("Crear Sesion...: ")
        msg = """{
                            "id": 1,
                            "jsonrpc": "2.0",
                            "method": "createSession",
                            "params": {
                                "cortexToken": "%s",
                                "headset": "%s",
                                "status": "open"
                            }
                        }""" % (token, headset)
        ws.send(msg)

        result = ws.recv()

        if 'appId' in result:
            dic = json.loads(result)
            sesion = dic['result']['id']
        else:
            print("Error en sesion")




        #print("Suscribirse a los comandos mentales...: ")
        msg = """{
                            "id": 1,
                            "jsonrpc": "2.0",
                            "method": "subscribe",
                            "params": {
                                "cortexToken": "%s",
                                "session": "%s",
                                "streams": ["pow"]
                            }
                        }""" % (token, sesion)
        ws.send(msg)
        ws.recv()
        result = ws.recv()

        bucle = json.loads(result) #Utilizar Com
        potencialElectrico = bucle["pow"][0]
        return potencialElectrico


    def start(self):
        self.status = True
        return self.status

    def stop(self):
        self.status = False
        return self.status

    def isWorking(self):
        return self.status

    def run(self):
        main_thread = next(filter(lambda t: t.name == "MainThread", threading.enumerate()))
        while main_thread.is_alive(): #Mientras que el hilo principal esta vivo se ejecutará este hilo secundario o de trabajo
            if self.status:
                self.signalCommand.emit(str(self.potenciaElectrodo()))
            sleep(0.1)



class Drone(QObject):
    def __init__(self):
        super().__init__()
        print("Se ha creado una instancia de la clase Drone.")

    @pyqtSlot(str)
    def command(self,command):
        print(command)

    def connect(self):
        self.status = True
        return self.status

    def disconnect(self):
        self.status = False
        return self.status

    def isConnected(self):
        return self.status












