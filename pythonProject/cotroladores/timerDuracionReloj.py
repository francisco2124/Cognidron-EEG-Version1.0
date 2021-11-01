from builtins import set

from PyQt5.QtCore import Qt, QThread, pyqtSignal
import time
import threading

class HiloDuracionReloj(QThread):

    status = True
    signDSReloj = pyqtSignal(str)
    def __init__(self, minutos):
        super().__init__()
        self.minutos = minutos

    def reanudar(self):
        self.status = True
        return self.status

    def detener(self):
        self.status = False
        return self.status

    def estadoHilo(self):
        return self.status

    def run(self):
        self.cont = 0
        self.tiempoRegresivo = ""
        main_thread = next(filter(lambda t: t.name == "MainThread", threading.enumerate()))
        while main_thread.is_alive():
            while self.tiempoRegresivo != "00:00" and self.estadoHilo():
                segundos = 60
                for i in range(1,self.minutos+1):
                    for j in range(1,segundos+1):

                        if self.minutos <10:
                            if segundos-j < 10:
                                self.tiempoRegresivo = ("0"+str(self.minutos-i)+ ":" +"0"+str(segundos-j))
                                #print(self.tiempoRegresivo)
                                self.signDSReloj.emit(self.tiempoRegresivo)
                                time.sleep(1)
                                #print("Hasta la vista, Baby."+str(self.tiempoRegresivo))

                            else:
                                self.tiempoRegresivo = ("0"+str(self.minutos-i)+ ":" +str(segundos-j))
                                #print(self.tiempoRegresivo)
                                self.signDSReloj.emit(self.tiempoRegresivo)
                                time.sleep(1)
                                #print("Hasta la vista, Baby."+str(self.tiempoRegresivo))
                        else:
                            if segundos-j < 10:
                                self.tiempoRegresivo = (str(self.minutos-i)+ ":" +"0"+str(segundos-j))
                                #print(self.tiempoRegresivo)
                                self.signDSReloj.emit(self.tiempoRegresivo)
                                time.sleep(1)
                                #print("Hasta la vista, Baby."+str(self.tiempoRegresivo))

                            else:
                                self.tiempoRegresivo = (str(self.minutos-i)+ ":" +str(segundos-j))
                                #print(self.tiempoRegresivo)
                                self.signDSReloj.emit(self.tiempoRegresivo)
                                time.sleep(1)
                                #print("Hasta la vista, Baby."+str(self.tiempoRegresivo))



