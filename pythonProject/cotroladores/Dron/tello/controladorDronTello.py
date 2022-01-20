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
        print("Despergar Dron")
        #time.sleep(5)

    def aterrizar(self):
        # Land
        self.sock.sendto('land'.encode(encoding="utf-8"), self.tello_address)
        print("Aterrizar Dron")
        #time.sleep(5)

    def adelante(self):

        self.sock.sendto('forward 20'.encode(encoding="utf-8"), self.tello_address)
        print("Adelante Dron")
        #time.sleep(5)

    def atras(self):

        self.sock.sendto('back 20'.encode(encoding="utf-8"), self.tello_address)
        print("Atras  Dron")
        #time.sleep(5)

    def elevar(self):

        self.sock.sendto('up 20'.encode(encoding="utf-8"), self.tello_address)
        print("Elevar Dron")
        #time.sleep(5)

    def decender(self):

        self.sock.sendto('down 20'.encode(encoding="utf-8"), self.tello_address)
        print("Desender Dron")
        #time.sleep(5)

    def derecha(self):

        self.sock.sendto('right 20'.encode(encoding="utf-8"), self.tello_address)
        print("Derecha Dron")
        #time.sleep(5)

    def izquierda(self):

        self.sock.sendto('left 20'.encode(encoding="utf-8"), self.tello_address)
        print("Izquierda Dron")
        #time.sleep(5)

    def girarDerecha(self):

        # Rotate clockwise 360
        self.sock.sendto('cw 45'.encode(encoding="utf-8"), self.tello_address)
        print("Girar Derecha Dron")
        #time.sleep(5)

    def girarIzquierda(self):

        # Rotate counte clockwise 360
        self.sock.sendto('ccw 45'.encode(encoding="utf-8"), self.tello_address)
        print("Girar Izquierda Dron")
        #time.sleep(5)

    def __del__(self):
        self.sock.close()
        print("------Has destruido la instancia del dron tello....-----")

    #Instancia de una clase (Ejecta la clase XD)
#x = DronTello()