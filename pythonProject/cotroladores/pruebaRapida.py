from PyQt5.QtCore import Qt, QThread, pyqtSignal
import time
import websocket
import json
import ssl
import threading
from modelos.modeloParametros import Modelo_conexion

class pruebaconexionEmotiv():

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
                                    "streams": ["pow"]
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
            if update_treshold >= 1.999999:
                print('Actualizar umbral....')
                star_treshold = time.perf_counter()
            if duracion >= 10.0:
                break
        print("Las lecturas obtenidas son: "+str(self.cont)+" la duracion estimada fue "+str(duracion)+ " segundos")

if __name__ == "__main__":
    x = pruebaconexionEmotiv()
    x.potenciaElectrodo()