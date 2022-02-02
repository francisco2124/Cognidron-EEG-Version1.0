from PyQt5.QtCore import Qt, QThread, pyqtSignal
import time
import websocket
import json
import ssl
import threading
from modelos.modeloParametros import Modelo_conexion

class pruebaconexionEmotiv(QThread):

    status = True
    signEmotiv = pyqtSignal(list)
    def __init__(self):
        super().__init__()

        self.modelo = Modelo_conexion()

        # Parametros necesarios
        #self.clientId = "L1eawU5ry1QItbMc8AokvIraebewehzRCyeIW4Ro"
        #self.clientSecret = "65jIP3680Y6qztv3uoKQyjihA4giZmsme0dzkyQUtdx5odLuO6jispNzIZO1I9PJpGad7tNbcDj8JuGUMWxOAlgzeqCLwpHNYkZw4Q0YgyeX3jXGEWUPGekcI28xcKzs"
        self.profile = "j"
        # - - - - - - - - - - - - - - - - -
        self.url = "wss://localhost:6868"
        self.contadorDePotencias = 0

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
        clientId = "0NONRi3ZtjAVSBKu9FSihOQcdsAPLwRPungPC5oq"
        clientSecret = "VKRg9KUJZwFuRkCESVkL9zIpmuoYbSyNAOiX6UwXuzU9CnHcDZzfmmKPcLs9534PElenBtKlcDrwUrL0kbEGwz0GGNP6Zggpi9eC74KtN4cZ8ERAkjyTnRvpc3SeC6BK"

        print("Los datos son los siguientes: ")
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


    def potenciaElectrodo(self):

        self.solicitarPermisos()

        ws = websocket.create_connection(self.url,sslopt={"cert_reqs": ssl.CERT_NONE})
        datos = self.modelo.cargarDatos()

        ListaDatos = datos[0]
        #self.clientId = str(ListaDatos[0]).strip()
        #self.clientSecret = str(ListaDatos[1]).strip()
        self.clientId = "0NONRi3ZtjAVSBKu9FSihOQcdsAPLwRPungPC5oq"
        self.clientSecret = "VKRg9KUJZwFuRkCESVkL9zIpmuoYbSyNAOiX6UwXuzU9CnHcDZzfmmKPcLs9534PElenBtKlcDrwUrL0kbEGwz0GGNP6Zggpi9eC74KtN4cZ8ERAkjyTnRvpc3SeC6BK"
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
        print("Respuesta de token es: "+str(result))
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

        result0 = ws.recv()

        if 'appId' in result0:
            dic = json.loads(result0)
            sesion = dic['result']['id']
            print("sesion es igual a "+str(sesion))
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
                                    "streams": ["eeg"]
                                }
                            }""" % (token, sesion)
        self.cont = 0
        star = time.perf_counter()
        star_treshold = time.perf_counter()
        while True:
            ws.send(msg)
            ws.recv()
            result = ws.recv()
            print(str(result))
            self.cont = self.cont + 1
            end = time.perf_counter()
            duracion = end - star
            update_treshold = end - star_treshold
            if update_treshold >= 1.0000000:
                print('Actualizar umbral....')
                star_treshold = time.perf_counter()
                print("--------------------------------------------------------------p")
            if duracion >= 10.0:
                break
        print("Las lecturas obtenidas son: "+str(self.cont)+" la duracion estimada fue "+str(duracion)+ " segundos")

if __name__ == "__main__":
    x = pruebaconexionEmotiv()
    x.potenciaElectrodo()