#Clase dedicada al dron tello
from plistlib import Data

import socket, time
import command as command

class DronTello():

    def __init__(self, dron_ip, dron_port, host_ip, host_port):
        super().__init__()
        print("Hola soy controlador tello")
        self.response = None
        self.dron_ip = dron_ip
        self.dron_port = dron_port
        self.host_ip = host_ip
        self.host_port = host_port
        self.tello_address = (self.dron_ip, self.dron_port)
        self.locaddr = (self.host_ip, self.host_port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(self.locaddr)
        self.sock.sendto('command'.encode(encoding="utf-8"), self.tello_address)
        time.sleep(5)

    def despegar(self):
        # Despegar dron
        self.sock.sendto('takeoff'.encode(encoding="utf-8"), self.tello_address)
        print("Despergar Dron")

    def aterrizar(self):
        # Aterrizar dron
        self.sock.sendto('land'.encode(encoding="utf-8"), self.tello_address)
        print("Aterrizar Dron")

    def adelante(self):
        # Mover dron hacia adelante
        self.sock.sendto('forward 20'.encode(encoding="utf-8"), self.tello_address)
        print("Adelante Dron")

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
        self.sock.sendto(f'cw 45'.encode(encoding="utf-8"), self.tello_address)
        print("Girar Derecha Dron")
        #time.sleep(5)

    def girarIzquierda(self):

        # Rotate counte clockwise 360
        self.sock.sendto(f'ccw 45'.encode(encoding="utf-8"), self.tello_address)
        print("Girar Izquierda Dron ")
        #time.sleep(5)

    def girarIzquierda90grados(self):

        # Rotate counte clockwise 360
        self.sock.sendto(f'ccw 90'.encode(encoding="utf-8"), self.tello_address)
        print("Girar Izquierda Dron 90 grados")
        #time.sleep(5)

    def send_command(self, command):

        self.sock.sendto(command.encode('utf-8'), self.tello_address)

        if self.response is None:
            response = 'none_response'
        else:
            response = self.response.decode('utf-8')

        self.response = None

        return response

    def getbateriaDron(self):

        try:
            batteryi = self.sock.sendto('battery?'.encode(encoding="utf-8"), self.tello_address)

            battery = self.sock.recvfrom(1024)


            print("La bateria desde la clase tello es*******************: "+str(battery[0].decode()))

            '''
            try:
                battery = int(battery)
            except:
                pass
            '''
            return battery[0].decode()
        except:
            return 0

    def __del__(self):
        self.sock.close()
        print("------Has destruido la instancia del dron tello....-----")

    #Instancia de una clase (Ejecta la clase XD)
#x = DronTello()