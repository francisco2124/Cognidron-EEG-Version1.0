from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from vistas.ejerciciosTerapiaNeurofeedback import Ui_ejercicioTerapeuticos
from PyQt5.QtGui import QIntValidator
from modelos.modeloEjercicios import Modelo_Ejercicios



#En esta clase se inserta codigo que permita a la vista realizar distintos comportamientos sin modificar el archivo principal de la vista



class Controlador_EjerciciosTerapeuticos(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        print("soy el controlador de ejercicios terapeuticos")
        self.ui= Ui_ejercicioTerapeuticos()
        self.ui.setupUi(self)
        self.modelo = Modelo_Ejercicios()
        self.InicializarGui()
        self.filtrarEjercicios()


    def InicializarGui(self):

        self.ui.btnBuscarTipoEjercicios.clicked.connect(self.filtrarEjercicios)
        self.ui.btnRealizar.clicked.connect(self.realizarTerapia)
        self.ui.tvEjercicios.cellClicked.connect(self.consultarEjercicio)


    def filtrarEjercicios(self):
        Ejercselec = self.ui.cbfiltrarEjercicios.currentText()
        if Ejercselec != "Todos":

            datos = self.modelo.filtarEjercicios(Ejercselec)

        else:
            datos = self.modelo.cargarTablaEjercicios()

        print("cargar Reportes")
        i = len(datos)
        self.ui.tvEjercicios.setRowCount(i)
        tablerow = 0
        for row in datos:
            self.ui.tvEjercicios.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tvEjercicios.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[2]))

            tablerow +=1
    def realizarTerapia(self):

        Alerta = QMessageBox.information(self, 'Alerta', "Se cargara un ejerciico de tipo -Neurofeedback-. Recuerda seleciona los electrodos necesarios, de lo contrario se cargaran por defecto F3 Y F4", QMessageBox.Ok)



    def consultarEjercicio(self):
        #textId = self.ui.etIdTerapeuta.text()

        RowTable = self.ui.tvEjercicios.currentRow()
        item = self.ui.tvEjercicios.item(RowTable, 0)
        datos = self.modelo.consultarEjercicio(item.text())
        datosEjercicio = datos[0]

        if RowTable != -1:

            print(item.text())
            print(str(datos))
            self.ui.taDescripcion.setText(str(datosEjercicio[0]))
            self.ui.lbParametro1.setText(str(datosEjercicio[1]))
            self.ui.lbParametro2.setText(str(datosEjercicio[2]))
            self.ui.lbImagenEjercicio.setStyleSheet("image: url(:/newPrefix/"+str(datosEjercicio[3])+");")
            self.ui.lbEjercicioSeecionado.setText(str(item.text()))

        #print(type,self.ui.self.ui.tableView.currentRow())