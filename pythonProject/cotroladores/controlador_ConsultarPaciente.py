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

from cotroladores.controlador_EditarTerapeuta import Control_EditarTerapeutas
from cotroladores.controlador_ConsultarTerapeutaSelccionado import Control_ConsultarTerapectuaSelec

class Controlador_ConsultarPaciente(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        print("soy la vista de consultar terapeutas")
        self.ui= Ui_Consultar_Pacientes()
        self.ui.setupUi(self)
        self.InicializarGui()

        self.modelo = Modelo_Terapeuta()
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
        self.cargarTerapeutas()
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

            self.abrir = Control_EditarTerapeutas(item.text())
            self.abrir.show()
        else:
            lerta = QMessageBox.information(self, 'Alerta', "No has seleccionado un terapeuta", QMessageBox.Ok)


    def abrirConsultar(self):
        #textId = self.ui.etIdTerapeuta.text()

        RowTable = self.ui.tableView_2.currentRow()

        if RowTable != -1:
            item = self.ui.tableView_2.item(RowTable, 0)
            print(item.text())

            self.abrir = Control_ConsultarTerapectuaSelec(item.text())
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

        Terapeuta = self.modelo.validarBorradoLigico2(item.text())
        idTerapeuta = Terapeuta[0]
        res= self.modelo.validarBorradoLigico(idTerapeuta[0])
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
                    Terapeuta = self.modelo.validarBorradoLigico2(item.text())
                    print("id tera : "+str(Terapeuta))
                    idTerapeuta = Terapeuta[0]
                    print("id es: " + str(idTerapeuta[0]))
                    self.modelo.elimina_terapeutaLogico2(idTerapeuta[0])
                    alerta = QMessageBox.information(self, 'Alera', "El terapeuta tiene sesiones terapeuticas y su borrrado fue logico", QMessageBox.Ok)
                    self.cargarTerapeutas()
                    self.cargarCbPacientes()
                else:
                    print("Entre al else")
                    Terapeuta = self.modelo.validarBorradoLigico2(item.text())
                    idTerapeuta = Terapeuta[0]
                    print(idTerapeuta)
                    self.modelo.elimina_terapeuta(idTerapeuta[0])

                    alerta = QMessageBox.information(self, 'Confirmacion', "Terapeuta Eliminado permanente", QMessageBox.Ok)
                    self.cargarTerapeutas()
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