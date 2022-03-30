from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from vistas.recuperarTerapeutas import Ui_RecuperarTerapeutas
from PyQt5.QtGui import QIntValidator

from modelos.ModeloTerapeuta import Modelo_Terapeuta


#En esta clase se inserta codigo que permita a la vista realizar distintos comportamientos sin modificar el archivo principal de la vista



class Controlador_RecuperarTerapeutasEliminados(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        print("soy la vista de consultar terapeutas")
        self.ui= Ui_RecuperarTerapeutas()
        self.ui.setupUi(self)
        self.modelo = Modelo_Terapeuta()
        self.InicializarGui()
        self.listarTerapeutasEliminados()


    def InicializarGui(self):

        self.ui.btnRefrescar.clicked.connect(self.listarTerapeutasEliminados)
        self.ui.btnRecuperarTerapeuta.clicked.connect(self.recuperarUnTerapeutaEliminado)
        self.ui.btnBuscarTerapeutas.clicked.connect(self.listarTerapeutasEliminadosXTipo)




    def listarTerapeutasEliminados(self):
        datos = self.modelo.cargarTablaTerapeutasEliminados()
        print(str(datos))
        print("cargar terapeutas eliminados")
        i = len(datos)
        self.ui.tvRecuperarTerapeutas.setRowCount(i)
        tablerow = 0
        for row in datos:
            self.ui.tvRecuperarTerapeutas.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.tvRecuperarTerapeutas.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tvRecuperarTerapeutas.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tvRecuperarTerapeutas.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
            self.ui.tvRecuperarTerapeutas.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[4]))
            if str(row[5]) == "0":
                tipo = "Normal"
            else:
                tipo = "Administrador"
            self.ui.tvRecuperarTerapeutas.setItem(tablerow,5,QtWidgets.QTableWidgetItem(tipo))
            tablerow +=1

    def listarTerapeutasEliminadosXTipo(self):
        tipoTerapeuta = self.ui.cbfiltrar.currentText()
        print(tipoTerapeuta)
        if tipoTerapeuta == "Todos":
            self.listarTerapeutasEliminados()
        else:
            if tipoTerapeuta == "Administrador":
                datos = self.modelo.cargarTablaTerapeutasEliminadosXTipo(1)
            else:
                datos = self.modelo.cargarTablaTerapeutasEliminadosXTipo(0)

            print(str(datos))
            print("cargar terapeutas eliminados")
            i = len(datos)
            self.ui.tvRecuperarTerapeutas.setRowCount(i)
            tablerow = 0
            for row in datos:
                self.ui.tvRecuperarTerapeutas.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[0])))
                self.ui.tvRecuperarTerapeutas.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
                self.ui.tvRecuperarTerapeutas.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
                self.ui.tvRecuperarTerapeutas.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
                self.ui.tvRecuperarTerapeutas.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[4]))
                if str(row[5]) == "0":
                    tipo = "Normal"
                else:
                    tipo = "Administrador"
                self.ui.tvRecuperarTerapeutas.setItem(tablerow,5,QtWidgets.QTableWidgetItem(tipo))
                tablerow +=1


    def recuperarUnTerapeutaEliminado(self):
        RowTable = self.ui.tvRecuperarTerapeutas.currentRow()
        item = self.ui.tvRecuperarTerapeutas.item(RowTable, 0)
        print("valor recuperado "+str(item.text()))

        self.modelo.recuperarTerapeutaConBorradoLogico(item.text(), 0)

        Alerta = QMessageBox.information(self, 'Confirmacion', "Se ha recuperado el terapeuta con el Id: "+item.text(), QMessageBox.Ok)
        self.listarTerapeutasEliminados()
