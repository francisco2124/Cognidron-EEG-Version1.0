
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

        self.ui.btnAbrirGrafico.clicked.connect(self.cargarReporteGrafico)
        self.ui.btnReportes.clicked.connect(self.abrirReporteTera)
        self.ui.btnVideo.clicked.connect(self.reproducirVideos)
        self.ui.btnEmviarReporte.clicked.connect(self.abrir_PDF)

    def cargarReportePrincipal(self):

        self.ui.lbIdentificador.setText(self.identificador)

        datos = self.modelo.busca_reporte(self.identificador)

        ListDatos = datos[0]


        self.ui.lbTerapeuta.setText(ListDatos[0])
        self.ui.lbPaciente.setText(ListDatos[1])
        self.ui.lbFecha.setText(ListDatos[2])


        datos2 = self.modelo.datosPaciente(ListDatos[10])
        ListDatosPciente = datos2[0]
        fecha_dt = datetime.strptime(str(ListDatosPciente[0]).strip(), '%d/%m/%Y')
        datetime.date(fecha_dt)
        age = (datetime.now() - fecha_dt)
        dias = age.days
        edad = math.floor(dias/365)

        self.ui.lbTutor.setText(ListDatosPciente[1] + " "+ ListDatosPciente[2])
        #print(edad)
        self.ui.lbFecha_2.setText(str(edad)+ " años")
        self.ui.lbTipo.setText(ListDatos[3])
        self.ui.lbTipoOnda.setText(ListDatos[4])
        self.ui.lbMetaAlcanza.setText(ListDatos[5])
        self.ui.lbMetaPropuesta.setText(ListDatos[6])
        self.ui.lbDuracion.setText(ListDatos[7])
        self.ui.lbComentarios.setText(ListDatos[8])
        self.ui.lbTipo_2.setText(ListDatos[11])

        if(ListDatos[9] == 1):
            self.ui.label_7.setStyleSheet("image: url(:/newPrefix/EjerElevar.png);")
        elif(ListDatos[9] == 2):
            self.ui.label_7.setStyleSheet("image: url(:/newPrefix/EjerDecender.png);")
        elif(ListDatos[9] == 3):
            self.ui.label_7.setStyleSheet("image: url(:/newPrefix/EjerAdelante.png);")


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

    def abrir_PDF(self):

        datos = self.modelo.cargar_reporte(self.identificador)
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

                pdf.addText(180, 285, str(ListDatos[0]))

                pdf.addImage("C:\Cognidron-EEG_Software\pythonProject\pruebas\ireporte.png", 15,242,8,8)
                pdf.addText(24, 244, "Datos de la sesión")
                pdf.addText(24, 236, "Número de la sesión:")
                pdf.addText(24, 230, "Función Cognitiva:")
                pdf.addText(24, 224, "Tipo de bandas:")
                pdf.addText(24, 218, "Division Theta/Beta:")
                pdf.addText(24, 212, "Área del cerebo:")
                pdf.addText(24, 206, "Duración de la sesión:")
                pdf.addText(24, 200, "Tipo de ejercicio:")
                pdf.addText(24, 194, "Nombre del ejercicio:")
                pdf.addText(24, 188, "Descripción del ejercicio:")
                pdf.addText(24, 182, "Nómero de aciertos:")

                #Datos de la sesion obtenidos de la bas de datos

                text = ("")
                pdf.addText(65, 236, str(ListDatos[1]))
                pdf.addText(65, 230, str(ListDatos[2]))
                pdf.addText(65, 224, str(ListDatos[3]))
                pdf.addText(65, 218, str(ListDatos[4]))
                pdf.addText(65, 212, str(ListDatos[5]))
                pdf.addText(65, 206, str(ListDatos[6]))
                pdf.addText(65, 200, str(ListDatos[8]))
                pdf.addText(65, 194, str(ListDatos[9]))
                descEjercico = str(ListDatos[10])
                pdf.addText(65, 188, descEjercico[0:74])
                pdf.addText(65, 182, str(ListDatos[11])+ " de " +str(ListDatos[12]))


                #Datos del terapeuta
                pdf.addImage("C:\Cognidron-EEG_Software\pythonProject\pruebas\iterapeuta.png", 15,155,8,8)
                pdf.addText(24, 157, "Datos del terapeuta")

                pdf.addText(24, 149, "Nombre:")
                pdf.addText(24, 143, "Contacto:")
                pdf.addText(24, 137, "Estatus:")

                #Datos recumerados e insertados
                pdf.addText(65, 149, str(ListDatos[13]))
                pdf.addText(65, 143, str(ListDatos[14]))
                if ListDatos[15] == 0:
                    estatus = "Activo"
                else:
                    estatus = "No Activo"
                pdf.addText(65, 137, estatus)

                #Datos de paciente
                pdf.addImage("C:\Cognidron-EEG_Software\pythonProject\pruebas\paciente.png", 15,115,8,8)
                pdf.addText(24, 117, "Datos del paciente")
                pdf.addText(24, 109, "Nombre:")
                pdf.addText(24, 103, "Edada:")
                pdf.addText(24, 97, "Tutor:")
                pdf.addText(24, 91, "Localidad:")
                pdf.addText(24, 85, "Contacto:")

                #Datos recumerados e insertados
                pdf.addText(65, 109, str(ListDatos[16]))
                datos2 = self.modelo.datosPaciente(ListDatos[21])
                ListDatosPciente = datos2[0]
                fecha_dt = datetime.strptime(str(ListDatosPciente[0]).strip(), '%d/%m/%Y')
                datetime.date(fecha_dt)
                age = (datetime.now() - fecha_dt)
                dias = age.days
                edad = math.floor(dias/365)
                pdf.addText(65, 103, str(edad)+ " años")
                pdf.addText(65, 97, ListDatosPciente[1]+ " "+ListDatosPciente[2])
                pdf.addText(65, 91, str(ListDatos[18]))
                pdf.addText(65, 85, str(ListDatos[19]))

                pdf.addImage("C:\Cognidron-EEG_Software\pythonProject\pruebas\iarchivo.png", 15,60,8,8)
                pdf.addText(24, 62, "Observaciones")
                pdf.addText(35, 54, str(ListDatos[20]))


                pdf.setLineThickness(0.5)
                pdf.setFontSize(12)
                pdf.addText(20,160,text)
                w = pdf.getTextWidth(text)

                pdf.addLine(20,158.5,20,158.5)

        crear_pdf("ReporteCogniDron-EEG.pdf")
        print("Ya lo imprimi")
        os.startfile("C:\Cognidron-EEG_Software\pythonProject\ReporteCogniDron-EEG.pdf")

