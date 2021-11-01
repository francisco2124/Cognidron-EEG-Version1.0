from PyQt5 import QtWidgets
from PyQt5.uic.properties import QtCore
import math
from datetime import date
from datetime import datetime
import time
from PyQt5.QtWidgets import QMessageBox

from vistas.consultarTutorSelecionado import Ui_ConsultarTutorSelec
from PyQt5.QtGui import QIntValidator

from modelos.ModeloTutor import Modelo_Tutor_

class Control_ConsultarTutorSelec(QtWidgets.QMainWindow):

    def __init__(self, idTerapeuta):
        super().__init__()
        print("soy la vista de consultaR un tutorespecifico")
        self.ui= Ui_ConsultarTutorSelec()
        self.ui.setupUi(self)
        self.user = idTerapeuta
        self.modelo = Modelo_Tutor_()
        self.cargarTutor()
        self.InicializarGui()
        #self.cargarReportesXTerapeuta()
        #self.cargarTablaTeraPacientes()

    def InicializarGui(self):

        #print(type, self.user)
        self.ui.lbUsuario.setText(self.user)
        self.ui.pushButton.clicked.connect(self.abrirReporteEspecifico)




    def cargarTutor(self):



        datos = self.modelo.cargarPlaceHolder(self.user)

        ListaDatos = datos[0]
        print("Los datos del tutor son: "+ str(ListaDatos))

        self.ui.lbNombre.setText(ListaDatos[1]+" "+ListaDatos[2]+" "+ListaDatos[3])
        self.ui.lbGenero.setText(ListaDatos[4])
        self.ui.lbFechaNaimiento.setText(ListaDatos[5])

        fecha_dt = datetime.strptime(str(ListaDatos[5]).strip(), '%d/%m/%Y')
        print(fecha_dt)
        datetime.date(fecha_dt)
        age = (datetime.now() - fecha_dt)
        dias = age.days
        edad = math.floor(dias/365)
        #print(edad)
        self.ui.lbEdad.setText(str(edad))
        self.ui.lbNacionalidad.setText(ListaDatos[6])

        datos2 = self.modelo.cargarEstadoAndMunicipio(str(ListaDatos[13]))
        ListaDatos2 = datos2[0]
        print(ListaDatos2)
        self.ui.lbEstado.setText(ListaDatos2[0])
        self.ui.lbMunicipio.setText(ListaDatos2[1])

        self.ui.lbLocalida.setText(ListaDatos[7])

        self.ui.lbDomicilio.setText(str(ListaDatos[8])+ " # "+str(ListaDatos[9]))
        self.ui.lbContacto.setText(str(ListaDatos[10]))
        self.ui.lbCodPostal.setText(str(ListaDatos[11]))
        self.ui.lbCorreo.setText(ListaDatos[12])



    def cargarReportesXTerapeuta(self):

        datosidT = self.modelo.cargarPlaceHolder(self.user)
        ListaDatos2 = datosidT[0]

        datos = self.modelo.cargarTablaXSesionTera(str(ListaDatos2[12]))
        print("cargar Reportes")
        i = len(datos)
        self.ui.tabla_pacientes.setRowCount(i)
        tablerow = 0
        for row in datos:
            self.ui.tabla_pacientes.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tabla_pacientes.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tabla_pacientes.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[3]))
            self.ui.tabla_pacientes.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[4]))
            self.ui.tabla_pacientes.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[5]))
            self.ui.tabla_pacientes.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[6]))


            tablerow +=1

    def cargarTablaTeraPacientes(self):

        datosidT = self.modelo.cargarPlaceHolder(self.user)
        ListaDatos3 = datosidT[0]

        datos3 = self.modelo.cargarTablaxTeraPaciente(str(ListaDatos3[12]))


        #print(datos3[0])

        if len(datos3) > 0:
            i = len(datos3)
            self.ui.tabla_pacientes_2.setRowCount(i)
            tablerow = 0
            for row in datos3:
                self.ui.tabla_pacientes_2.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[1]))
                self.ui.tabla_pacientes_2.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[2]))
                #self.ui.tabla_pacientes_2.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[3]))
                tablerow +=1

    def abrirReporteEspecifico(self):

        #textId = self.ui.etIdTerapeuta.text()
        RowTable = self.ui.tabla_pacientes.currentRow()
        if RowTable != -1:
            item = self.ui.tabla_pacientes.item(RowTable, 0)
            print(item.text())

            self.abrir = Controlador_ConsultarReporteEspecifoco(item.text())
            self.abrir.show()

        else:
            Alerta = QMessageBox.information(self, 'Alerta', "Selecciona un rreporte", QMessageBox.Ok)
            print("No selecionaste")

