from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from vistas.reporteParaTerapeuta import Ui_Dialog
from PyQt5.QtGui import QIntValidator

from modelos.modelorReportes import Modelo_Reportes
import math
from datetime import date
from datetime import datetime
import time

#En esta clase se inserta codigo que permita a la vista realizar distintos comportamientos sin modificar el archivo principal de la vista



class Controlador_ReporteParaTerapeuta(QtWidgets.QMainWindow):

    def __init__(self, idTerapeuta):
        super().__init__()

        self.ui= Ui_Dialog()
        self.modelo = Modelo_Reportes()
        self.idTerapeuta = idTerapeuta
        self.ui.setupUi(self)
        self.InicializarGui()



    def InicializarGui(self):

        print("IdRepot "+str(self.idTerapeuta))
        self.cargarReporte()

    def cargarReporte(self):

        datos = self.modelo.cargar_reporte(self.idTerapeuta)
        ListDatos = datos[0]
        print("Reportes Datos desde RU: "+str(ListDatos))

        self.ui.label_18.setText(ListDatos[0])

        self.ui.lbNumeroSesion.setText(ListDatos[1])
        self.ui.lbFuncionCognitiva.setText(ListDatos[2])
        self.ui.lbTipoOnda.setText(ListDatos[3])
        self.ui.lbDivision.setText(ListDatos[4])
        self.ui.lbAreaCerebro.setText(ListDatos[5])
        self.ui.lbDuracion.setText(ListDatos[6])
        self.ui.lbEjercicio.setText(ListDatos[9])
        self.ui.lbNumeroAciertos.setText(ListDatos[11]+ " de 10")

        #Datos del Terapeuta
        self.ui.lbNombreTera.setText(ListDatos[13])
        self.ui.contactoTera.setText(ListDatos[14])
        if ListDatos[15] == 0:
            estatus = "Activo"
        else:
            estatus = "No Activo"
        self.ui.estatusTera.setText(estatus)

        #Datos del Paciente

        datos2 = self.modelo.datosPaciente(ListDatos[21])
        ListDatosPciente = datos2[0]
        fecha_dt = datetime.strptime(str(ListDatosPciente[0]).strip(), '%d/%m/%Y')
        datetime.date(fecha_dt)
        age = (datetime.now() - fecha_dt)
        dias = age.days
        edad = math.floor(dias/365)
        self.ui.nombrePaciente.setText(ListDatos[16])
        self.ui.lbEdad.setText(str(edad)+ " años")

        self.ui.lbLocalida.setText(ListDatos[18])
        self.ui.lbTutor.setText(ListDatosPciente[1]+ " "+ListDatosPciente[2])
        self.ui.lbContacto.setText(ListDatos[19])

        self.ui.lbObservaciones.setText(ListDatos[20])









