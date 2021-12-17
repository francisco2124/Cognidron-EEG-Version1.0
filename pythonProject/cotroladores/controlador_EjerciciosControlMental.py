from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from vistas.ejerciciosTerapiaControlMental import Ui_ejercicioTerapeuticos
from PyQt5.QtGui import QIntValidator
from modelos.modeloEjercicios import Modelo_Ejercicios



#En esta clase se inserta codigo que permita a la vista realizar distintos comportamientos sin modificar el archivo principal de la vista



class Controlador_EjerciciosTerapeuticosControlMental(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        print("soy el controlador de ejercicios terapeuticos de tipo Cotrol Mental")
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
            datos = self.modelo.cargarTablaEjerciciosControlMental()

        print("cargar Reportes")
        i = len(datos)
        self.ui.tvEjercicios.setRowCount(i)
        tablerow = 0
        for row in datos:
            self.ui.tvEjercicios.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tvEjercicios.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[2]))

            tablerow +=1
    def realizarTerapia(self):
        RowTable = self.ui.tvEjercicios.currentRow()
        item = self.ui.tvEjercicios.item(RowTable, 1)
        print(item.text())

        if item.text() == "Neurofeedback":
            Alerta = QMessageBox.information(self, 'Alerta', "Se cargara un ejerciico de tipo -Neurofeedback-. Recuerda seleciona los electrodos necesarios, de lo contrario se cargaran por defecto F3 Y F4", QMessageBox.Ok)

        elif item.text() == "Control Mental":
            Alerta = QMessageBox.information(self, 'Alerta', "Se cargara un ejerciico de tipo -Control Mental-. Recuerda que si no selecionas una opcion para cada comando "
                                                             "se cargara por defector lo siguiente: Comando 1- Elevar, Comando 2- Adelante, Comando 3-Girar Derecha, Comando 4-Descender ", QMessageBox.Ok)


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
            self.ui.lbEjercicioSeecionado.setText("Ejercicio Selecionado: "+str(item.text()))

            if str(item.text()) == "1-Comando mental":
                self.ui.cbcomandoMental1.setEnabled(True)
                self.ui.cbcomandoMental2.setEnabled(False)
                self.ui.cbcomandoMental3.setEnabled(False)
                self.ui.cbcomandoMental4.setEnabled(False)
            elif item.text() == "2-Comandos mentales":
                self.ui.cbcomandoMental1.setEnabled(True)
                self.ui.cbcomandoMental2.setEnabled(True)
                self.ui.cbcomandoMental3.setEnabled(False)
                self.ui.cbcomandoMental4.setEnabled(False)
            elif item.text() == "3-Comandos mentales":
                self.ui.cbcomandoMental1.setEnabled(True)
                self.ui.cbcomandoMental2.setEnabled(True)
                self.ui.cbcomandoMental3.setEnabled(True)
                self.ui.cbcomandoMental4.setEnabled(False)
            elif item.text() == "4-Comandos mentales":
                self.ui.cbcomandoMental1.setEnabled(True)
                self.ui.cbcomandoMental2.setEnabled(True)
                self.ui.cbcomandoMental3.setEnabled(True)
                self.ui.cbcomandoMental4.setEnabled(True)
            else:
                self.ui.cbcomandoMental1.setEnabled(False)
                self.ui.cbcomandoMental2.setEnabled(False)
                self.ui.cbcomandoMental3.setEnabled(False)
                self.ui.cbcomandoMental4.setEnabled(False)

        else:
            Alerta = QMessageBox.information(self, 'Alerta', "No has seleccionado un terapeuta", QMessageBox.Ok)



        #print(type,self.ui.self.ui.tableView.currentRow())