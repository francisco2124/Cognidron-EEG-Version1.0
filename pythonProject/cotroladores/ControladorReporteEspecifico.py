
from PyQt5 import QtWidgets
import os
from modelos.modelorReportes import Modelo_Reportes
from vistas.reporteEspecifico import Ui_ReporteEspecifico
from vistas.reporteParaTerapeuta import Ui_Dialog
from cotroladores.controlodor_ReporteParaUsuario import Controlador_ReporteParaTerapeuta
import pandas as pd
import matplotlib.pyplot as plt
import math
from datetime import date
from datetime import datetime
import time
#Abrir otras vistas
from PaPDF import PaPDF


class Controlador_ConsultarReporteEspecifoco(QtWidgets.QMainWindow):

    def __init__(self, idetificadorReporte):
        super().__init__()
        print("soy la vista de consultar terapeutas especificos")
        self.ui= Ui_ReporteEspecifico()
        # self.control = Control_Terapeuta()
        self.modelo = Modelo_Reportes()

        self.ui.setupUi(self)
        self.identificador = idetificadorReporte
        self.iniciarGui()
        self.cargarReportePrincipal()


    def iniciarGui(self):

        pass
        #self.ui.btnAbrirGrafico.clicked.connect(self.cargarReporteGrafico)
        #self.ui.btnReportes.clicked.connect(self.abrirReporteTera)
        #self.ui.btnVideo.clicked.connect(self.reproducirVideos)
        self.ui.btnEmviarReporte.clicked.connect(self.abrir_PDF)


    def cargarReportePrincipal(self):

        self.ui.lbIdentificador.setText(self.identificador)

        datos = self.modelo.busca_reporte(self.identificador)

        ListDatos = datos[0]

        print("Los datos son: "+str(ListDatos))

      #-------------------------------------------Datos del Paciente----------------------------------------------

        #---Nombre---
        self.ui.lbNombrePaciente.setText(ListDatos[0]+" "+ListDatos[1])
        #---Obtener Edad---
        fecha_dt = datetime.strptime(str(ListDatos[2]).strip(), '%d/%m/%Y')
        datetime.date(fecha_dt)
        age = (datetime.now() - fecha_dt)
        dias = age.days
        edad = math.floor(dias/365)
        self.ui.lbEdadPaciente.setText(str(edad)+ " años")
        #---Localidad---
        self.ui.lbLocalidaPaciente.setText(ListDatos[3])
        #---Tutor---
        self.ui.lbTutorPaciente.setText(ListDatos[4]+ " "+ListDatos[5])
        #---Contacto---
        self.ui.lbContactoPaciente.setText(ListDatos[6])

      #-------------------------------------------Datos del Terapeuta--------------------------------------------------

        #---Nombre---
        self.ui.lbNombreTera.setText(ListDatos[7]+" "+ListDatos[8])
        #---Obtener Edad---
        fecha_dt = datetime.strptime(str(ListDatos[9]).strip(), '%d/%m/%Y')
        datetime.date(fecha_dt)
        age = (datetime.now() - fecha_dt)
        dias = age.days
        edad = math.floor(dias/365)
        self.ui.lbEdadPaciente.setText(str(edad)+ " años")
        #---Localidad---
        self.ui.lbLocalidadTera.setText(ListDatos[10])
        #---Estatus---
        estatus = ""
        if str(ListDatos[11]) == "0":
            estatus = "Activo"
        else:
            estatus = "Inactivo"
        self.ui.lbestatusTera.setText(estatus)
        #---Contacto---
        self.ui.lbcontactoTera.setText(ListDatos[12])

      #-------------------------------------------Datos de la terapia--------------------------------------------------

        #---Tipo de Terapia---
        self.ui.lbTipoTerapia.setText("Neurofeedback")
        #---Fecha de terapia---
        self.ui.lbFecha.setText(ListDatos[13])
        #---Tipo de entorno---
        self.ui.lbTipoTerapia.setText("Real")
        #---Robot---
        self.ui.lbRobot.setText("Dron Tello")
        #---Nombre de ejercicio---
        self.ui.lbNombreEjercicio.setText(ListDatos[14])
        #---Funcion Cognitiva---
        self.ui.lbFuncionesCognitivas.setText(ListDatos[15])
        #---Elctrodos---
        self.ui.lbElectrodos.setText(ListDatos[16])
        #---Tipo de ejercicio---
        self.ui.lbTipoEjericio.setText(ListDatos[17])
        #---Duracion de la sesion---
        self.ui.lbDuracion.setText(ListDatos[18]+" Minutos")
        #---Promedio de potencias---
        self.ui.lbPromedioPotencia.setText(str(ListDatos[19]))
        #---Banda Trabajada---
        self.ui.lbBandaTrabajada.setText(ListDatos[20])
        #---Menor Umbral---
        self.ui.lbMenorUmbral.setText(str(ListDatos[21]))
        #---Mayor Umbral---
        self.ui.lbMoyorUmbral.setText(str(ListDatos[22]))
        #---Promedio Umbral---
        self.ui.lbPromedioUmbral.setText(str(ListDatos[23]))
        #---Porcentaje logrado---
        self.ui.lbPorcentajeLogrado.setText(str(ListDatos[24]))
        #---Observaciones de la terapia---
        self.ui.tpObservaciones.setPlainText(ListDatos[25])

    '''
    def cargarReporteGrafico(self):

        y=[1,2,3,4,5,6,7,8,9,10]
        datosM = self.modelo.busca_reporte(self.identificador)

        ListDatos = datosM[0]
        datos = self.modelo.recuperarMetasAlcanzadas(ListDatos[10])
        print("El paciente logro: "+str(datos))
        numDato = len(datos)
        listaX = []

        for i in range(numDato):
            datosLista = datos[i]
            listaX.append(int(datosLista[0]))

        if self.ui.rbGrafLIneal.isChecked() == True:

            plt.plot(listaX)
            plt.show()
        else:
            if len(listaX) < 10:
                numeroDeCeros =  10 - len(listaX)
                for i in range(numeroDeCeros):
                    listaX.append(0)

            print("La lista tiene: "+str(listaX))


            plt.bar(y,listaX)
            plt.show()



    def abrirReporteTera(self):


        self.abrir = Controlador_ReporteParaTerapeuta(self.identificador)
        self.abrir.show()



    def reproducirVideos(self):

        os.startfile("C:\Cognidron-EEG_Software\pythonProject\multimedia\ielectro.png")
    '''
    def abrir_PDF(self):

        datos = self.modelo.busca_reporte(self.identificador)
        ListDatos = datos[0]
        print("Reportes Datos: "+str(ListDatos))

        def crear_pdf(text):
            with PaPDF(text) as pdf:
                pdf.setFontSize(18)
                pdf.addImage("C:\Cognidron-EEG_Software\pythonProject\pruebas\idea-genial.png", 15,270,20,20)
                pdf.addText(40, 280, "CogniDron-EEG")
                pdf.setFontSize(10)
                pdf.addText(50, 275, "Reporte Terapeutico")

                pdf.addTrueTypeFont("DejaVuSans", "C:\Cognidron-EEG_Software\pythonProject\pruebas\DejaVuSans.ttf")
                pdf.setFont("DejaVuSans")
                pdf.setFontSize(9)

                pdf.addText(170, 285, "Num. Reporte: "+self.identificador)

                pdf.addImage("C:\Cognidron-EEG_Software\pythonProject\pruebas\paciente.png", 15,250,8,8)
                pdf.addText(24, 250, "Datos del Paciente:")
                pdf.addText(24, 242, "Nombre:")
                pdf.addText(24, 236, "Edad:")
                pdf.addText(24, 230, "Localidad:")
                pdf.addText(24, 224, "Tutor:")
                pdf.addText(24, 218, "Contacto:")

                #Datos de la sesion obtenidos de la bas de datos

                text = ("")
                pdf.addText(65, 242, ListDatos[0]+" "+ListDatos[1]+" "+ListDatos[26])
                #---Obtener Edad---
                fecha_dt = datetime.strptime(str(ListDatos[2]).strip(), '%d/%m/%Y')
                datetime.date(fecha_dt)
                age = (datetime.now() - fecha_dt)
                dias = age.days
                edad = math.floor(dias/365)
                pdf.addText(65, 236, str(edad)+" años")
                pdf.addText(65, 230, ListDatos[3])
                pdf.addText(65, 224, ListDatos[4]+" "+ListDatos[5])
                pdf.addText(65, 218, ListDatos[6])


                #Datos del terapeuta
                pdf.addImage("C:\Cognidron-EEG_Software\pythonProject\pruebas\iterapeuta.png", 15,198,8,8)
                pdf.addText(24, 198, "Datos del terapeuta")
                pdf.addText(24, 192, "Nombre:")
                pdf.addText(24, 186, "Edad:")
                pdf.addText(24, 180, "Localidad:")
                pdf.addText(24, 174, "Contacto:")

                pdf.addText(65, 192, ListDatos[7]+" "+ListDatos[8])
                #---Obtener Edad---
                fecha_dt = datetime.strptime(str(ListDatos[9]).strip(), '%d/%m/%Y')
                datetime.date(fecha_dt)
                age = (datetime.now() - fecha_dt)
                dias = age.days
                edad = math.floor(dias/365)
                pdf.addText(65, 186, str(edad)+" años")
                pdf.addText(65, 180, ListDatos[10])
                pdf.addText(65, 174, ListDatos[12])


                #Datos de Sesion
                pdf.addImage("C:\Cognidron-EEG_Software\pythonProject\pruebas\ireporte.png", 15,154,8,8)
                pdf.addText(24, 154, "Datos de la terapia")

                pdf.addText(24, 146, "Tipo de terapia:")
                pdf.addText(24, 140, "Fecha de terapia:")
                pdf.addText(24, 134, "Tipo de entorno")
                pdf.addText(24, 128, "Robot ")
                pdf.addText(24, 122, "Nombre de ejercicio:")
                pdf.addText(24, 116, "Funciones cognitivas:")
                pdf.addText(24, 110, "Electrodos:")
                pdf.addText(24, 104, "Tipo de ejercicio:")
                pdf.addText(24, 98, "Duración de la sesión:")
                pdf.addText(24, 92, "Promedio de potencia:")
                pdf.addText(24, 86, "Banda trabajada:")
                pdf.addText(115, 104, "Menor Umbral:")
                pdf.addText(115, 98, "Mayor Umbral:")
                pdf.addText(115, 92, "Promedio Umbral:")
                pdf.addText(115, 86, "Porcentaje logrado:")

                pdf.addText(65, 146, "Neorofeedback")
                pdf.addText(65, 140, ListDatos[13])
                pdf.addText(65, 134, "Entorno real")
                pdf.addText(65, 128, "Dron tello")
                pdf.addText(65, 122, ListDatos[14])
                pdf.addText(65, 116, ListDatos[15])
                pdf.addText(65, 110, ListDatos[16])
                pdf.addText(65, 104, ListDatos[17])
                pdf.addText(65, 98, ListDatos[18]+" Minutos")
                pdf.addText(65, 92, str(ListDatos[19]))
                pdf.addText(65, 86, str(ListDatos[20]))
                pdf.addText(155, 104, str(ListDatos[21]))
                pdf.addText(155, 98, str(ListDatos[22]))
                pdf.addText(155, 92, str(ListDatos[23]))
                pdf.addText(155, 86, str(ListDatos[24]))

                pdf.addImage("C:\Cognidron-EEG_Software\pythonProject\pruebas\iarchivo.png", 15,66,8,8)
                pdf.addText(24, 62, "Observaciones")
                pdf.addText(28, 54, ListDatos[25])


                pdf.setLineThickness(0.5)
                pdf.setFontSize(12)
                pdf.addText(20,160,text)
                w = pdf.getTextWidth(text)

                pdf.addLine(20,158.5,20,158.5)

        crear_pdf("ReporteCogniDron-EEG.pdf")
        print("Ya lo imprimi")
        os.startfile("C:\Cognidron-EEG-Software-Pruebas-Moni\pythonProject\ReporteCogniDron-EEG.pdf")
