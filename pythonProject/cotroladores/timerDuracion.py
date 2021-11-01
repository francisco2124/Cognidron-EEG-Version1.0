from PyQt5.QtCore import Qt, QThread, pyqtSignal
import time
import threading

class HiloDuracion(QThread):

    status = True
    signDS = pyqtSignal(int)
    def __init__(self, tiempo):
        super().__init__()
        self.tiempo = tiempo

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
        main_thread = next(filter(lambda t: t.name == "MainThread", threading.enumerate()))
        while main_thread.is_alive():
            while self.cont < 100 and self.estadoHilo():
                self.cont+=1
                time.sleep(self.tiempo)
                #print("a", str(self.cont))
                self.signDS.emit(self.cont)




