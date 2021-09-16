import pymysql

import pymysql
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from vistas.reportesGenerales import Ui_Ui_ReportesGenerales_2
from PyQt5.QtGui import QIntValidator
from modelos.modelorReportes import Modelo_Reportes


#Abrir otras vistas

from cotroladores.ControladorReporteEspecifico import Controlador_ConsultarReporteEspecifoco

class Controlador_ConsultarReportesGenerales(QtWidgets.QMainWindow):

    def __init__(self) -> object:
        super().__init__()
        print("soy la vista de consultar terapeutas")
        self.ui= Ui_Ui_ReportesGenerales_2()
        self.modelo = Modelo_Reportes()
        self.ui.setupUi(self)
        self.iniciarGui()
        self.cargarReportes()
        self.cargarCbPacientes()



    def iniciarGui(self):

        self.ui.btnConsultar.clicked.connect(self.abrirReporteEspecifico)
        self.ui.btnBuscarbaciente.clicked.connect(self.cargarReportesXPacientes)
        self.ui.btnBuscarFecha.clicked.connect(self.cargarReportesXFecha)

    def ejemplo(self):

        re = self.modelo.cargarTabla()
        print(re)



    def abrirReporteEspecifico(self):

        #textId = self.ui.etIdTerapeuta.text()

        RowTable = self.ui.tabla_pacientes.currentRow()

        if RowTable != -1:
            item = self.ui.tabla_pacientes.item(RowTable, 0)
            print(item.text())

            self.abrir = Controlador_ConsultarReporteEspecifoco(item.text())
            self.abrir.show()


        else:
            Alerta = QMessageBox.information(self, 'Alerta', "Selecciona un Reporte", QMessageBox.Ok)
            print("No selecionaste")


        #print(type,self.ui.self.ui.tableView.currentRow())

    def cargarCbPacientes(self):

        pacientes =  self.modelo.recuperarPacientes()
        print(pacientes)


        combo = self.ui.cbfiltrar
        combo.clear()
        combo.addItem("Todos")
        combo.addItems([str(x[0]) for x in pacientes])

    def cargarReportes(self):

        datos = self.modelo.cargarTabla()
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

    def cargarReportesXPacientes(self):
        pacientesselec = self.ui.cbfiltrar.currentText()

        if pacientesselec == "Todos":
            self.cargarReportes()
        else:
            datos = self.modelo.cargarTablaXPaciente(pacientesselec)
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



    def cargarReportesXFecha(self):
        date = self.ui.dateEdit.text()
        datos = self.modelo.cargarTablaXFeacha(date)
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