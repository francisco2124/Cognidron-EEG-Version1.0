from PyQt5.QtCore import Qt, QThread, pyqtSignal
import time

class HiloSingsEotiv(QThread):
    signDS = pyqtSignal(int)

    def run(self):
       #potencias = [20.2,30.2,10.12,12,40,8,20.2,30.2,10.12,12,40,8,20.2,30.2,10.12,12,40,8,20.2,30.2,10.12,12,40,8,56,58,59,56,20.2,30.2,10.12,40.56,50,58,20.2,40,21,58]
       potencias = [10,20,30,40,50,60,70,80,90,1,1,2,3,4,5,6,7,8,9,1,2,3]
       for i in potencias:
        potenciaElectrodo = i
        #print("La potencia del hilo es: "+str(potenciaElectrodo))
        time.sleep(2)
        self.signDS.emit(potenciaElectrodo)