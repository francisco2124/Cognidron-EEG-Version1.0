#Clase dedicada al dron tello
from plistlib import Data

import socket, time

import command as command

class DronTello():

    def __init__(self, dron_ip, dron_port, host_ip, host_port):
        super().__init__()
        print("Hola soy controlador tello")
        self.dron_ip = dron_ip
        self.dron_port = dron_port
        self.host_ip = host_ip
        self.host_port = host_port

        self.locaddr = (self.host_ip, self.host_port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.tello_address = (self.dron_ip, self.dron_port)
        self.sock.bind(self.locaddr)
        self.sock.sendto('command'.encode(encoding="utf-8"), self.tello_address)
        time.sleep(5)


    def despegar(self):
        # Takeoff
        self.sock.sendto('takeoff'.encode(encoding="utf-8"), self.tello_address)
        time.sleep(5)

    def aterrizar(self):
        # Land
        self.sock.sendto('land'.encode(encoding="utf-8"), self.tello_address)
        time.sleep(5)

    def adelante(self):

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

    def girarDerecha(self):

        pass

    def girarIzquierda(self):

        pass

    def __del__(self):
        self.sock.close()
        print("------Has destruido la instancia del dron tello....-----")

    #Instancia de una clase (Ejecta la clase XD)
#x = DronTello()