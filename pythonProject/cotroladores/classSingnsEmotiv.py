from PyQt5.QtCore import Qt, QThread, pyqtSignal
import time

class HiloSingsEotiv(QThread):
    signDS = pyqtSignal(int)

    def run(self):
       potencias = [20.2,30.2,10.12,12,40,24,80,28,22,40.56,50,78,20.2,30.2,10.12,40.56,50,78,20.2,30.2,10.12,40.56,50,78,70,40,50,89,50,60,32,60,40,21,78]

       for i in potencias:
        potenciaElectrodo = i
        print("La potencia del hilo es: "+str(potenciaElectrodo))
        time.sleep(2)
        self.signDS.emit(potenciaElectrodo)