 #Clase dedicada para el dron....

from cotroladores.dron.tello.controladorDronTello import DronTello


class Dron():

    #Parametros de conexion del dron
    dron_ip = None
    dron_port = None
    #Parametros de conexion de la pc
    host_ip = None
    host_port = None
    drone = None
    tipo = {"tello":1, "bebop2":2}

    def __init__(self, dron_ip, dron_port, tipo, host_ip = '', host_port = 9000):

        self.dron_ip = dron_ip
        self.dron_port = dron_port
        self.host_ip = host_ip
        self.host_port = host_port

        if tipo.lower() in self.tipo.keys():

            if self.tipo[tipo.lower()] == 1:
                self.dron = DronTello(self.dron_ip, self.dron_port, self.host_ip, self.host_port)
            elif self.tipo[tipo.lower()] == 2:
                print("Falta implementar la clase de bebop 2.....")


    #-------------------------------------Metodos-------------------------------

    def despegar(self):
        if self.dron != None:
            print("")
            self.dron.despegar()
        else:
            print("----------------ERROR: No se ha creado una instancia del dron....-------------")

    def aterrizar(self):

        if self.dron != None:
            print("")
            self.dron.aterrizar()
        else:
            print("----------------ERROR: No se ha creado una instancia del dron....-------------")

    def adelante(self):

        if self.dron != None:
            print("")
            self.dron.adelante()
        else:
            print("----------------ERROR: No se ha creado una instancia del dron....-------------")

    def atras(self):

        if self.dron != None:
            print("")
            self.dron.atras()
        else:
            print("----------------ERROR: No se ha creado una instancia del dron....-------------")

    def elevar(self):

        if self.dron != None:
            print("")
            self.dron.elevar()
        else:
            print("----------------ERROR: No se ha creado una instancia del dron....-------------")

    def decender(self):

        if self.dron != None:
            print("")
            self.dron.decender()
        else:
            print("----------------ERROR: No se ha creado una instancia del dron....-------------")

    def derecha(self):

        if self.dron != None:
            print("")
            self.dron.derecha()
        else:
            print("----------------ERROR: No se ha creado una instancia del dron....-------------")

    def izquierda(self):

        if self.dron != None:
            print("")
            self.dron.izquierda()
        else:
            print("----------------ERROR: No se ha creado una instancia del dron....-------------")


    def girarderecha(self):

        if self.dron != None:
            print("")
            self.dron.girarDerecha()
        else:
            print("----------------ERROR: No se ha creado una instancia del dron....-------------")

    def girarizquierda(self):

        if self.dron != None:
            print("")
            self.dron.girarIzquierda()
        else:
            print("----------------ERROR: No se ha creado una instancia del dron....-------------")