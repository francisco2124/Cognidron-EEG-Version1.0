from PyQt5.QtCore import Qt, QThread, pyqtSignal
import time
import websocket
import json
import ssl
import threading
from modelos.modeloParametros import Modelo_conexion

class conexionEmotiv(QThread):

    status = True
    signEmotiv = pyqtSignal(float)
    def __init__(self):
        super().__init__()

        self.modelo = Modelo_conexion()

        # Parametros necesarios
        #self.clientId = "L1eawU5ry1QItbMc8AokvIraebewehzRCyeIW4Ro"
        #self.clientSecret = "65jIP3680Y6qztv3uoKQyjihA4giZmsme0dzkyQUtdx5odLuO6jispNzIZO1I9PJpGad7tNbcDj8JuGUMWxOAlgzeqCLwpHNYkZw4Q0YgyeX3jXGEWUPGekcI28xcKzs"
        self.profile = "j"
        # - - - - - - - - - - - - - - - - -
        self.url = "wss://localhost:6868"

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


    def obtenerToken(self):

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

    def potenciaElectrodo(self):

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
            pass

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

        result = ws.recv()

        if 'appId' in result:
            dic = json.loads(result)
            sesion = dic['result']['id']
        else:
            print("Error en sesion")




        #print("-----------------------------Suscribirse a los comandos mentales...: ")
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
        print(str(bucle))

        #Prueba solo con theta en f3
        potencialElectrico = bucle["pow"][0]

        #Formula para sacar theta/beta = ( ((thetaf3+thetaf4)/2) / ((betaF3+betaf4)/2) )

        #                                   theta F4YF4 / Beta F3YF4
        #thetaf3 = bucle["pow"][0]
        #thetaf4 = bucle["pow"][55]
        #betaf3 = bucle["pow"][2]
        #betaf4 = bucle["pow"][57]
        #thetabetha = ( ((thetaf3+thetaf2)/2) / ((beta3+betaf4)/2) )
        #return thetabetha
        return potencialElectrico

    def run(self):
        self.cont = 0
        self.tiempoRegresivo = ""
        main_thread = next(filter(lambda t: t.name == "MainThread", threading.enumerate())) #Mientras el hilo esta vivo y recuperar los datos
        while main_thread.is_alive():
            potenciaElectrica = self.potenciaElectrodo()
            print("La potencia es: "+str(potenciaElectrica))
            time.sleep(0.5)
            self.signEmotiv.emit(potenciaElectrica)


