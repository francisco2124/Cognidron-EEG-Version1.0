 #Clase dedicada para el dron....

from cotroladores.controladorDronTello import DronTello


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

        self.dron.aterrizar()

    def adelanteDrone(self):

        pass

    def atrasDrone(self):

        pass

    def elevarDrone(self):

        pass

    def decenderDrone(self):

        pass

    def derechaDrone(self):

        pass

    def izquierdaDrone(self):

        pass