

import websocket
import json
import ssl
from modelos.modeloParametros import Modelo_conexion

class classConexion():

    def __init__(self):
        super().__init__()

        self.modelo = Modelo_conexion()

        # Parametros necesarios
        #self.clientId = "L1eawU5ry1QItbMc8AokvIraebewehzRCyeIW4Ro"
        #self.clientSecret = "65jIP3680Y6qztv3uoKQyjihA4giZmsme0dzkyQUtdx5odLuO6jispNzIZO1I9PJpGad7tNbcDj8JuGUMWxOAlgzeqCLwpHNYkZw4Q0YgyeX3jXGEWUPGekcI28xcKzs"
        self.profile = "j"
        # - - - - - - - - - - - - - - - - -
        self.url = "wss://localhost:6868"

        self.cargarParametris()
        self.conectar()
        print("Hola Mundo")
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

    def suscribirseDEV(self):

        ws = websocket.create_connection(self.url,sslopt={"cert_reqs": ssl.CERT_NONE})
        datos = self.modelo.cargarDatos()

        ListaDatos = datos[0]
        clientId = str(ListaDatos[0]).strip()
        clientSecret = str(ListaDatos[1]).strip()
        profile = "j"


        token = self.obtenerToken()
        headset = self.recuperarDeadema()
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
        print("Suscribirse a los comandos mentales...: ")
        msg = """{
                            "id": 1,
                            "jsonrpc": "2.0",
                            "method": "subscribe",
                            "params": {
                                "cortexToken": "%s",
                                "session": "%s",
                                "streams": ["dev"]
                            }
                        }""" % (token, sesion)
        ws.send(msg)

        print("--------------------------------------------------------")
        result = ws.recv()
        print("Se recupera lo siguiente: " + result)
        result = ws.recv()

        return result


if __name__ == '__main__':
    print('PyCharm')
