from builtins import set

from PyQt5.QtCore import Qt, QThread, pyqtSignal
import time
import threading

class HiloDuracionReloj(QThread):

    status = True
    signDSReloj = pyqtSignal(str)
    segundos = 0
    minutos = 0
    tiempoSesion = ""
    def __init__(self):
        super().__init__()

    def reanudar(self):
        self.status = True
        return self.status

    def detener(self):
        self.status = False
        return self.status

    def estadoHilo(self):
        return self.status

    def run(self):

        main_thread = next(filter(lambda t: t.name == "MainThread", threading.enumerate()))
        while main_thread.is_alive():
            while self.tiempoSesion != "59:59" and self.estadoHilo():

                self.segundos = self.segundos +1
                if self.minutos < 10:
                    if self.segundos < 10:
                            self.tiempoSesion = ("0"+str(self.minutos)+ ":" +"0"+str(self.segundos))
                            print("Entre al if 1")
                            print(self.tiempoSesion)
                            self.signDSReloj.emit(self.tiempoSesion)
                            time.sleep(1)

                    else:
                            print("Entre al if 2")
                            print(self.tiempoSesion)
                            #print(self.tiempoSesion)
                            if self.segundos == 60:
                                self.minutos = self.minutos + 1
                                self.segundos = 0
                                self.tiempoSesion = ("0"+str(self.minutos)+ ":0" +str(self.segundos))
                            else:
                                self.tiempoSesion = ("0"+str(self.minutos)+ ":" +str(self.segundos))

                            self.signDSReloj.emit(self.tiempoSesion)
                            time.sleep(1)

                else:
                    if self.segundos < 10:
                        self.tiempoSesion = (str(self.minutos)+ ":" +"0"+str(self.segundos))
                        #print(self.tiempoSesion)
                        self.signDSReloj.emit(self.tiempoSesion)
                        time.sleep(1)

                    else:
                        #print(self.tiempoSesion)
                        if self.segundos == 60:
                            self.minutos = self.minutos + 1
                            self.segundos = 0
                            self.tiempoSesion = (str(self.minutos)+ ":0" +str(self.segundos))
                        else:
                            self.tiempoSesion = (str(self.minutos)+ ":" +str(self.segundos))

                        self.signDSReloj.emit(self.tiempoSesion)
                        time.sleep(1)



