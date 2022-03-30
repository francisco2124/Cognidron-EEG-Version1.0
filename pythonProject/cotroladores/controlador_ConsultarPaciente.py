import pymysql
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from modelos.ModeloTerapeuta import Modelo_Terapeuta
from PyQt5.QtGui import QIntValidator
from vistas.consultarPacientes import Ui_Consultar_Pacientes
import datetime
import math
from datetime import date
from datetime import datetime
import time

from modelos.ModeloTerapeuta import Modelo_Terapeuta
from modelos.ModeloPacientes import Modelo_Paciente_

#Abrir Nuevas Vistas

from cotroladores.controlador_EditarPacienter import Control_EditarPaciente
from cotroladores.controlador_ConsultarPacienteSelccionado import Control_ConsultarPaciebSelec

class Controlador_ConsultarPaciente(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        print("soy la vista de consultar terapeutas")
        self.ui= Ui_Consultar_Pacientes()
        self.ui.setupUi(self)
        self.InicializarGui()

        self.modeloP = Modelo_Paciente_()
        self.cargarPacientes()
        self.cargarCbPacientes()


    def InicializarGui(self):
        self.ui.btnModificar.clicked.connect(self.abrirModificar)
        self.ui.btnConsultar.clicked.connect(self.abrirConsultar)
        self.ui.btnBuscarpaciente.clicked.connect(self.cargarPacienteXPaciente)
        self.ui.btnEliminar.clicked.connect(self.eliminarTerapeuta)
        self.ui.btnRefrescar.clicked.connect(self.refrescar)

    def refrescar(self):
        self.cargarPacientes()
        self.cargarCbPacientes()
    def eda(self):

        d = datetime.date(1997, 6, 11)
        age = (date.today() - d)
        dias = age.days
        edad = math.floor(dias/365)
        print(edad)
        self.ui.label_2.setText(str(edad))


    def abrirModificar(self):


        RowTable = self.ui.tableView_2.currentRow()

        if RowTable != -1:
            item = self.ui.tableView_2.item(RowTable, 0)
            print(item.text())

            self.abrir = Control_EditarPaciente(item.text())
            self.abrir.show()
        else:
            lerta = QMessageBox.information(self, 'Alerta', "No has seleccionado un paciente", QMessageBox.Ok)


    def abrirConsultar(self):
        #textId = self.ui.etIdTerapeuta.text()

        RowTable = self.ui.tableView_2.currentRow()

        if RowTable != -1:
            item = self.ui.tableView_2.item(RowTable, 0)
            print(item.text())

            self.abrir = Control_ConsultarPaciebSelec(item.text())
            self.abrir.show()
        else:
            lerta = QMessageBox.information(self, 'Alerta', "No has seleccionado un terapeuta", QMessageBox.Ok)


        #print(type,self.ui.self.ui.tableView.currentRow())


    def cargarCbPacientes(self):

        terapeutas =  self.modeloP.recuperarPacientes()
        #print(terapeutas)


        combo = self.ui.cbfiltrar
        combo.clear()
        combo.addItem("Todos")
        combo.addItems([str(x[1]) for x in terapeutas])


    def validarBorradoLogico(self, item):

        paciente = self.modeloP.validarBorradoLigico2(item.text())
        print("El resultado es: "+str(paciente))
        if len(paciente) != 0:
            res = True
        else:
            res = False

        return  res

    def eliminarTerapeuta(self):

        RowTable = self.ui.tableView_2.currentRow()

        if RowTable != -1:
            item = self.ui.tableView_2.item(RowTable, 0)
            print(item.text())

            buttonReply = QMessageBox.question(self, 'Alerta', "¿Quieres eliminar a: "+item.text()+" de forma permanente?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if buttonReply == QMessageBox.Yes:
                print("se eliminara el terapeuta")

                if(self.validarBorradoLogico(item) == True):
                    print("Entre al if")
                    self.modeloP.elimina_PacienteLogico(item.text())
                    alerta = QMessageBox.information(self, 'Alera', "El paciente tiene sesiones terapeuticas y su borrrado fue logico", QMessageBox.Ok)
                    self.cargarPacientes()
                    self.cargarCbPacientes()
                else:
                    print("Entre al else")
                    '''
                    Terapeuta = self.modeloP.validarBorradoLigico2(item.text())
                    idTerapeuta = Terapeuta[0]
                    print(idTerapeuta)
                    '''
                    self.modeloP.eliminar_Paciente(item.text())

                    alerta = QMessageBox.information(self, 'Confirmacion', "El paciente se ha eliminado permanentemente", QMessageBox.Ok)
                    self.cargarCbPacientes()
                    self.cargarCbPacientes()


            else:
                alerta = QMessageBox.warning(self, 'Alerta', "No se elimino nada", QMessageBox.Ok)

        else:
            lerta = QMessageBox.information(self, 'Alerta', "No has seleccionado un terapeuta", QMessageBox.Ok)

    def cargarPacientes(self):
        datos = self.modeloP.cargarTabla()
        print("cargar Reportes")
        i = len(datos)
        self.ui.tableView_2.setRowCount(i)
        tablerow = 0
        for row in datos:
            self.ui.tableView_2.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.tableView_2.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableView_2.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tableView_2.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
            self.ui.tableView_2.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[4]))
            self.ui.tableView_2.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[5]))

            tablerow +=1


    def cargarPacienteXPaciente(self):
        pacienteselec = self.ui.cbfiltrar.currentText()
        print("El paciente es "+pacienteselec)

        if pacienteselec == "Todos":
            datos = self.modeloP.cargarTabla()
        else:
            datos = self.modeloP.cargarTablaxUnPaciente(pacienteselec)


        print("cargar Reportes :"+str(datos))
        i = len(datos)
        self.ui.tableView_2.setRowCount(i)
        tablerow = 0
        for row in datos:
            self.ui.tableView_2.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.tableView_2.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableView_2.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tableView_2.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
            self.ui.tableView_2.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[4]))
            self.ui.tableView_2.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[5]))
            tablerow +=1