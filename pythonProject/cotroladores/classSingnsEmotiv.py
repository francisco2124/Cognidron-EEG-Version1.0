from PyQt5.QtCore import Qt, QThread, pyqtSignal
import time

class HiloSingsEotiv(QThread):
    signDS = pyqtSignal(int)

    def run(self):
       potencias = [20.2,30.2,10.12,12,40,3,5,2,3,4,1,2,1,3,1,2,6,3,2,1,2,1,8,56,68,79,56,89,96,98,99,96,99,98,98,20.2,30.2,10.12,40.56,50,78,20.2,40,21,78]

       for i in potencias:
        potenciaElectrodo = i
        #print("La potencia del hilo es: "+str(potenciaElectrodo))
        time.sleep(2)
        self.signDS.emit(potenciaElectrodo)