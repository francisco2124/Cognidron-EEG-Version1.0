from cotroladores.dron.controladorDron import Dron
import time

class pruebaEjercicioCompleto1():


    def __init__(self):
        super().__init__()
        self.estadoDron = 0
        self.alturaMaximaDron = 0
        self.alturaMinimaDron = 0
        self.giroDron = 0


    def ejercicioDronComplejo1(self):
        self.dron = Dron('192.168.10.1', 8889, "tello")

        while True:
            if self.estadoDron == 0:
                self.dron.despegar()
                self.estadoDron = 1
                time.sleep(3)
            elif self.giroDron <8:
                self.dron.girarderecha()
                self.giroDron = self.giroDron +1
                time.sleep(3)
            elif self.alturaMaximaDron <3:
                self.dron.elevar()
                self.alturaMaximaDron = self.alturaMaximaDron + 1
                time.sleep(3)
                if self.alturaMaximaDron == 3:
                    self.giroDron = 0
                    self.alturaMinimaDron = 0
                else:
                    print("Error con la altura Maxima")
            elif self.alturaMinimaDron <3:
                self.dron.decender()
                self.alturaMinimaDron= self.alturaMinimaDron + 1
                time.sleep(3)
                if self.alturaMinimaDron == 3:
                    self.giroDron = 0
                    self.alturaMaximaDron = 0
                else:
                    print("Error con la altura Minima")
            else:
                print("Erro con el ejercicio complejo_1")







        '''
        Ejemplo de jercicio
        print("Hasta la vista Baby ;)")
        self.dron.despegar()
        time.sleep(6)
        self.dron.girarderecha()
        time.sleep(3)
        self.dron.girarderecha()
        time.sleep(3)
        self.dron.girarderecha()
        time.sleep(3)
        self.dron.girarderecha()
        time.sleep(3)
        self.dron.girarderecha()
        time.sleep(3)
        self.dron.girarderecha()
        time.sleep(3)
        self.dron.girarderecha()
        time.sleep(3)
        self.dron.girarderecha()
        time.sleep(3)
        self.dron.elevar()
        time.sleep(3)
        self.dron.elevar()
        time.sleep(3)
        self.dron.elevar()
        time.sleep(3)
        self.dron.girarderecha()
        time.sleep(3)
        self.dron.girarderecha()
        time.sleep(3)
        self.dron.girarderecha()
        time.sleep(3)
        self.dron.girarderecha()
        time.sleep(3)
        self.dron.girarderecha()
        time.sleep(3)
        self.dron.girarderecha()
        time.sleep(3)
        self.dron.girarderecha()
        time.sleep(3)
        self.dron.girarderecha()
        '''







if __name__ == '__main__':
    ejecutarDron = pruebaEjercicioCompleto1()
    ejecutarDron.ejercicioDronComplejo1()