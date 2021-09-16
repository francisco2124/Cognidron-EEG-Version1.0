import pymysql
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from modelos.ModeloTutor import Modelo_Tutor_
from PyQt5.QtGui import QIntValidator
from vistas.consultarTutores import Ui_Consultar_Tutores
import datetime
import math
from datetime import date
from datetime import datetime
import time

from modelos.ModeloTerapeuta import Modelo_Terapeuta

#Abrir Nuevas Vistas

from cotroladores.controlador_EditarTerapeuta import Control_EditarTerapeutas
from cotroladores.controlador_ConsultarTerapeutaSelccionado import Control_ConsultarTerapectuaSelec

class Controlador_ConsultarTuotores(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        print("soy la vista de consultar tutores")
        self.ui= Ui_Consultar_Tutores()
        self.ui.setupUi(self)
        self.InicializarGui()

        self.modelo = Modelo_Tutor_()
        self.cargarTutor()
        self.cargarCbTutores()


    def InicializarGui(self):
        self.ui.btnModificar.clicked.connect(self.abrirModificar)
        self.ui.btnConsultar.clicked.connect(self.abrirConsultar)
        self.ui.btnBuscarbaciente.clicked.connect(self.cargarTutorXTutor)
        self.ui.btnEliminar.clicked.connect(self.eliminarTutor)
        self.ui.btnRefrescar.clicked.connect(self.refrescar)

    def refrescar(self):
        self.cargarTutor()
        self.cargarCbTutores()
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


    def cargarCbTutores(self):

        tutores =  self.modelo.recuperarTutores()
        #print(terapeutas)


        combo = self.ui.cbfiltrar
        combo.clear()
        combo.addItem("Todos")
        combo.addItems([str(x[0]) for x in tutores])


    def validarBorradoLogico(self, item):

        Terapeuta = self.modelo.validarBorradoLigico2(item.text())
        idTerapeuta = Terapeuta[0]
        res= self.modelo.validarBorradoLigico(idTerapeuta[0])
        return  res

    def eliminarTutor(self):

        RowTable = self.ui.tableView_2.currentRow()

        if RowTable != -1:
            item = self.ui.tableView_2.item(RowTable, 0)
            print(item.text())

            buttonReply = QMessageBox.question(self, 'Alerta', "Hola Moni! ¿Quieres eliminar a: "+item.text()+" de forma permanente?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if buttonReply == QMessageBox.Yes:
                print("se eliminara el terapeuta")

                if(self.validarBorradoLogico(item) == True):
                    print("Entre al if")
                    Terapeuta = self.modelo.validarBorradoLigico2(item.text())
                    print("id tera : "+str(Terapeuta))
                    idTerapeuta = Terapeuta[0]
                    print("id es: " + str(idTerapeuta[0]))
                    self.modelo.elimina_terapeutaLogico2(idTerapeuta[0])
                    alerta = QMessageBox.information(self, 'Alera', "El tutor tiene pasientes asignados y su borrrado fue logico", QMessageBox.Ok)
                    self.cargarTutor()
                    self.cargarCbTutores()
                else:
                    print("Entre al else")
                    Terapeuta = self.modelo.validarBorradoLigico2(item.text())
                    idTerapeuta = Terapeuta[0]
                    print(idTerapeuta)
                    self.modelo.elimina_terapeuta(idTerapeuta[0])

                    alerta = QMessageBox.information(self, 'Confirmacion', "Tutor Eliminado permanente", QMessageBox.Ok)
                    self.cargarTutor()
                    self.cargarCbTutores()


            else:
                alerta = QMessageBox.warning(self, 'Alerta', "No se elimino nada", QMessageBox.Ok)

        else:
            lerta = QMessageBox.information(self, 'Alerta', "No has seleccionado un tutor", QMessageBox.Ok)

    def cargarTutor(self):
        datos = self.modelo.cargarTabla()
        print("cargar Reportes")
        i = len(datos)
        self.ui.tableView_2.setRowCount(i)
        tablerow = 0
        for row in datos:
            self.ui.tableView_2.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableView_2.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tableView_2.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[3]))
            self.ui.tableView_2.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[4]))
            self.ui.tableView_2.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[5]))
            tablerow +=1


    def cargarTutorXTutor(self):
        teraselec = self.ui.cbfiltrar.currentText()
        print(teraselec)
        if teraselec == "Todos":
            self.cargarTutor()
        else:
            datos2 = self.modelo.cargarTablaxTutor(teraselec)

            print("cargar Reportes")
            i = len(datos2)
            self.ui.tableView_2.setRowCount(i)
            tablerow = 0
            for row in datos2:
                self.ui.tableView_2.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
                self.ui.tableView_2.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[1]))
                self.ui.tableView_2.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[2]))
                self.ui.tableView_2.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[3]))
                self.ui.tableView_2.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[4]))
                self.ui.tableView_2.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[5]))
                tablerow +=1