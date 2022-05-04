from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from vistas.capturarObservaciones import Ui_capturarObservaciones
from PyQt5.QtGui import QIntValidator

#Modelos
from modelos.modeloEjercicios import Modelo_Ejercicios
from modelos.modelorReportes import Modelo_Reportes



#En esta clase se inserta codigo que permita a la vista realizar distintos comportamientos sin modificar el archivo principal de la vista



class Controlador_Observaciones(QtWidgets.QMainWindow):

    def __init__(self, tiempoSesion, puntos, promedioPotencias, electrodos, mayorTiempo, menorTiempo, promedioTiempo, porcentajeTiempo,
                 fecha, tipoEjercicio, frecuencia, ejercicio,robot, paciente, primerUmbral, numVecesUmbral):
        super().__init__()
        print("soy la vista de capturar observaciones")
        self.ui= Ui_capturarObservaciones()
        self.ui.setupUi(self)
        self.modelo = Modelo_Reportes()
        self.modeloEjericicio = Modelo_Ejercicios()


        #Resultados de Sesio
        self.tiempoSesion = tiempoSesion
        self.promedioPotencias = promedioPotencias
        self.electrodos = electrodos
        self.puntosSesion = puntos
        self.mayorTiempo = mayorTiempo
        self.menorTiempo = menorTiempo
        self.promedioTiepo = promedioTiempo
        self.porcentajeTiempo = porcentajeTiempo
        self.fecha = fecha
        self.tipoEjercicio = tipoEjercicio
        self.frecuencia  = frecuencia
        self.ejercicio = ejercicio
        self.robot = robot
        self.paciente = paciente
        self.primerUmbral = primerUmbral
        self.numVecesUmbral = numVecesUmbral

        self.InicializarGui()

    def InicializarGui(self):
        print("Hola mundo :)")
        self.ui.lbDuracioSesion.setText(str(self.tiempoSesion)+" Minutos")
        self.ui.lbPromedioPotencias.setText(str(self.promedioPotencias))
        self.ui.lbPuntos.setText(str(self.puntosSesion))
        self.ui.lbMayorTiempo.setText(str(self.mayorTiempo))
        self.ui.lbMenorTiempo.setText(str(self.menorTiempo))
        self.ui.lbPromedioTiempo.setText(str(self.promedioTiepo))
        self.ui.lbTiempoUmbralObtenido.setText(str(self.porcentajeTiempo)+" %")
        self.ui.lbPrimerUmbral.setText(self.primerUmbral)
        self.ui.lbNumeroUmbrales.setText(str(self.numVecesUmbral))

        self.ui.btnRegistar.clicked.connect(self.capturarObservaciones)

        print("Los datos extras son los siguientes------------------------------- ")
        print("Fecha: "+self.fecha)
        print("Tipo ejercicio: "+self.tipoEjercicio)
        print("Frecuencia: "+self.frecuencia)
        print("Ejercicio: "+self.ejercicio)
        print("Robto: "+self.robot)
        print("Paciente: "+str(self.paciente))
        print("---------------------------------------------------------------------")


    def capturarObservaciones(self):
        observaciones = str(self.ui.tekObservaciones.toPlainText())
        funcionCognitiva = self.ui.etFuncionCognitiva.text()

        if len(funcionCognitiva) == 0:
            Alerta = QMessageBox.information(self, 'Alerta', "Ingresa la funcion cognitiva trabajada en la terapia", QMessageBox.Ok)

        elif len(observaciones) == 0:
            Alerta = QMessageBox.information(self, 'Alerta', "Ingresa las observaciones de la terapia para continuar", QMessageBox.Ok)

        else:
            #try:

            datos = self.modeloEjericicio.recuperarIdEjercicio(str(self.ejercicio))
            idEjercicio = datos[0]
            print(str(idEjercicio[0]))

            self.modelo.registarTerpaiaNeurofeedback(self.fecha, funcionCognitiva, self.tiempoSesion,self.tipoEjercicio,
                                                    self.puntosSesion, self.frecuencia,observaciones,
                                                    self.promedioPotencias, self.electrodos, self.mayorTiempo, self.promedioTiepo,
                                                    self.menorTiempo, self.porcentajeTiempo, self.paciente, 1,idEjercicio[0])
            Alerta = QMessageBox.information(self, 'Conformacion', "Se registraron correctamente los datos", QMessageBox.Ok)

            #except:
             #   Alerta = QMessageBox.information(self, 'Alerta', "Ocurrio un problema al registrar los datos", QMessageBox.Ok)

