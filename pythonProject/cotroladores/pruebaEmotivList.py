from PyQt5.QtCore import Qt, QThread, pyqtSignal
import time
import websocket
import json
import ssl
import threading
from modelos.modeloParametros import Modelo_conexion
from PyQt5.QtWidgets import QMessageBox


class pruebaconexionEmotiv(QThread):

    status = True
    signEmotiv = pyqtSignal(list)
    def __init__(self, electrodos, banda):
        super().__init__()

        self.modelo = Modelo_conexion()

        # Parametros necesarios
        #self.clientId = "L1eawU5ry1QItbMc8AokvIraebewehzRCyeIW4Ro"
        #self.clientSecret = "65jIP3680Y6qztv3uoKQyjihA4giZmsme0dzkyQUtdx5odLuO6jispNzIZO1I9PJpGad7tNbcDj8JuGUMWxOAlgzeqCLwpHNYkZw4Q0YgyeX3jXGEWUPGekcI28xcKzs"
        self.profile = "j"
        # - - - - - - - - - - - - - - - - -
        self.url = "wss://localhost:6868"
        self.contadorDePotencias = 0
        self.electrodosSeleccionados = electrodos
        self.bandaSeleccionada = banda
        self.potenciasXElectrodo = {'Estandar':'10-10','AF3':[0,1,2,3,4], 'F7':[5,6,7,8,9],'F3':[10,11,12,13,14],'FC5':[15,16,17,18,19],'T7':[20,21,22,23,24],
                                    'P7':[25,26,27,28,29],'E01':[30,31,32,33,34],'E02':[35,36,37,38,39],'P8':[40,41,42,43,44],'T8':[45,46,47,48,49],
                                    'FC6':[50,51,52,53,54], 'F4':[55,56,57,58,59],'F8':[60,61,62,63,64],'AF4':[65,66,67,68,69]}


    def cargarParametris(self):

        datos = self.modelo.cargarDatos()

        ListaDatos = datos[0]

        print("Los datos son los siguientes: ")
        print(str(datos))

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

        mensaje = ""
        resuladoFallido = '''{"id":1,"jsonrpc":"2.0","result":{"buildDate":"2020-09-08T12:06:34","buildNumber":"v2.2.3-659-gfa6e645","version":"2.6.0.105"}}'''
        print(resuladoFallido)
        if result != resuladoFallido:
            mensaje = False

        else:
            mensaje = True

        return mensaje


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
            print("Verifica que tu inicio sesion este activo")
            mensaje = False

        else:
            mensaje = True

        return mensaje


    def solicitarPermisos(self):

        ws = websocket.create_connection(self.url,sslopt={"cert_reqs": ssl.CERT_NONE})
        datos = self.modelo.cargarDatos()


        print("Las credenciales son........")
        ListaDatos = datos[0]
        clientId = str(ListaDatos[0]).strip()
        clientSecret = str(ListaDatos[1]).strip()

        print("Los datos son los siguientes: ")
        print(str(datos))
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
                        }""" % (clientId, clientSecret)
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
            Mensaje = False
        else:
            Mensaje = True

        return Mensaje

    def crearConexion(self):

        ws = websocket.create_connection(self.url,sslopt={"cert_reqs": ssl.CERT_NONE})

    def obteunerToken(self):

        #Pasos relacionado con la conexion del emotiv

        try:
            ws = websocket.create_connection(self.url,sslopt={"cert_reqs": ssl.CERT_NONE})
            datos = self.modelo.cargarDatos()

            ListaDatos = datos[0]
            clientId = str(ListaDatos[0]).strip()
            clientSecret = str(ListaDatos[1]).strip()
            profile = "j"
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
                            }""" % (clientId, clientSecret)
            ws.send(msg)

            print("--------------------------------------------------------")
            result = ws.recv()
            print("Se recupera lo siguiente: " + str(result))
            print("--------------------------------------------------------")

            dic = json.loads(result)
            print("El diccionario es: "+str(dic))
            print("--------------------------------------------------------")
            token = dic["result"]["cortexToken"]
            print("token es: ", token)

            mensaje = token

        except:

            mensaje = False

        return mensaje

    def recuperarDeadema(self):

        try:
            ws = websocket.create_connection(self.url,sslopt={"cert_reqs": ssl.CERT_NONE})
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
            dic = json.loads(result)
            headset = dic["result"][0]["id"]  # Obtener el ID de la diadema
            diadema =  headset
            #self.ui.label_4.setStyleSheet("background-color: rgb(41, 226, 69);")
        except:
            print("Error: No hay ningun diadema conectada")
            diadema = False
            #"Se detecto un problema con la deadema... Verfica que la diadema este conectada"

        return diadema

    def crearSesion(self):
        try:
            token = self.obtenerToken()
            headset = self.recuperarDeadema()

            ws = websocket.create_connection(self.url,sslopt={"cert_reqs": ssl.CERT_NONE})
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

            dic = json.loads(result)
            sesion = dic['result']['id']
            print("El ide de la sesion es: "+str(sesion))
            mensaje = sesion
        except:
            mensaje = False

        return mensaje


    def reanudar(self):
        self.status = True
        return self.status

    def detener(self):
        self.status = False
        return self.status

    def estadoHilo(self):
        return self.status

    def run(self):
        self.tiempoRegresivo = ""
        main_thread = next(filter(lambda t: t.name == "MainThread", threading.enumerate())) #Mientras el hilo esta vivo y recuperar los datos
        ws = websocket.create_connection(self.url,sslopt={"cert_reqs": ssl.CERT_NONE})
        datos = self.modelo.cargarDatos()

        ListaDatos = datos[0]
        self.clientId = str(ListaDatos[0]).strip()
        self.clientSecret = str(ListaDatos[1]).strip()
        profile = "Francisco"
        #print("--------------------------Obtener Token...: ")
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


        #print("======================Ver diademas conectadas...: ")
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
            lerta = QMessageBox.information(self, 'Alerta', "Verifica la conecion con la diadema EEG...", QMessageBox.Ok)


        #print("----------------------------------Crear Sesion...: ")
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

        result0 = ws.recv()

        if 'appId' in result0:
            dic = json.loads(result0)
            sesion = dic['result']['id']
            print("sesion es igual a "+str(sesion))
        else:
            sesion = "Sin Sesion"
        listaPotencias = []

        sumas =0
        self.cont = 0
        while self.status == True:

            try: #print("-----------------------------Suscribirse a neurofeedback...: ")
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

            except:
                print("Fallo la conexion")



            ws.send(msg)
            ws.recv()
            result = ws.recv()
            #print(str(result))

            try:
                #return potencialElectrico
                bucle = json.loads(result)
                #print(str(result))
                #print("La banda desde pruebaEmotiv es: "+str(self.bandaSeleccionada))
                if self.bandaSeleccionada == "Theta/BetaBaja":
                    thetaf3 = bucle["pow"][10]
                    thetaf4 = bucle["pow"][55]
                    betaBajaF3 = bucle["pow"][12]
                    betaBajaF4 = bucle["pow"][57]
                    thetabetaBaja = ( ((thetaf3+thetaf4)/2) / ((betaBajaF3+betaBajaF4)/2) )
                    listaPotencias.append(thetabetaBaja)
                    sumas = sumas + thetabetaBaja
                    self.cont = self.cont+1
                elif self.bandaSeleccionada == "Theta/BetaAlta":
                    thetaf3 = bucle["pow"][10]
                    thetaf4 = bucle["pow"][55]
                    betaAltaF3 = bucle["pow"][13]
                    betaAltaF4 = bucle["pow"][58]
                    thetabetaAlta = ( ((thetaf3+thetaf4)/2) / ((betaAltaF3+betaAltaF4)/2) )
                    sumas = sumas + thetabetaAlta
                    listaPotencias.append(thetabetaAlta)
                    self.cont = self.cont+1
                    #print(str(thetabetha))
                elif self.bandaSeleccionada == "Theta/BetaCompleta":
                    thetaf3 = bucle["pow"][10]
                    thetaf4 = bucle["pow"][55]
                    betaBajaF3 = bucle["pow"][12]
                    betaBajaF4 = bucle["pow"][57]
                    betaAltaF3 = bucle["pow"][13]
                    betaAltaF4 = bucle["pow"][58]
                    thetabetaCompleta = ( ((thetaf3+thetaf4)/2) / ((betaAltaF3+betaAltaF4+betaBajaF3+betaBajaF4)/4))
                    sumas = sumas + thetabetaCompleta
                    listaPotencias.append(thetabetaCompleta)
                    self.cont = self.cont+1
                elif str(self.bandaSeleccionada) == "Theta":
                    promedioTheta =0
                    #print("Entre a theta")
                    for id,value in self.electrodosSeleccionados.items():
                        if value == True:
                            potenciaDelElectrodoSeleccionado = bucle["pow"][self.potenciasXElectrodo[id][0]]
                            promedioTheta = promedioTheta+potenciaDelElectrodoSeleccionado
                            listaPotencias.append(promedioTheta)
                            sumas = sumas + potenciaDelElectrodoSeleccionado
                    self.cont = self.cont+1

                elif str(self.bandaSeleccionada) == "Alfa":

                    print("Entre a Alfa")
                    for id,value in self.electrodosSeleccionados.items():
                        if value == True:
                            #print("El electrodo es: "+str(id))
                            potenciaDelElectrodoSeleccionado = bucle["pow"][self.potenciasXElectrodo[id][1]]
                            #print("la potencia obtenida es "+str(potenciaDelElectrodoSeleccionado))
                            sumas = sumas + potenciaDelElectrodoSeleccionado
                            #print("la suma de alfas es "+str(sumaAlfas))
                            listaPotencias.append(potenciaDelElectrodoSeleccionado)
                            #print("la lista de potencias es "+str(listaPotencias))
                    self.cont = self.cont+1

            except:

                print("No se obtuvo lectura...")

            #Se obtiene el promedio cuando se hace 8 lecturas. Las 8 lecturas son por aegundo
            if self.cont == 8:
                listaPotenciasFinal = []
                print("lista "+str(listaPotencias))
                numElectrodos = len(listaPotencias) / 8
                print(str("Numero de electrodos es igual a: "+str(numElectrodos)))
                promedio = sumas/8
                listaPotenciasFinal.append(promedio)
                print("===========Promedio 1s======: "+str(promedio))
                print("----------------------------------------------------------------------------------------------------")
                self.signEmotiv.emit(listaPotenciasFinal)
                sumas = 0
                listaPotencias = []
                self.cont = 0




