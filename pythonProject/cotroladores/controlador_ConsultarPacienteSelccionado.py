from PyQt5 import QtWidgets
from PyQt5.uic.properties import QtCore
import math
from datetime import date
from datetime import datetime
import time
from PyQt5.QtWidgets import QMessageBox

from vistas.consultarPacienteSelecionado import Ui_ConsultarPacienteSelec
from PyQt5.QtGui import QIntValidator

from modelos.ModeloPacientes import Modelo_Paciente_
from cotroladores.ControladorReporteEspecifico import Controlador_ConsultarReporteEspecifoco

class Control_ConsultarPaciebSelec(QtWidgets.QMainWindow):

    def __init__(self, idPaciente):
        super().__init__()
        print("soy la vista de consultar un paciente especifico")
        self.ui= Ui_ConsultarPacienteSelec()
        self.ui.setupUi(self)
        self.paciente = idPaciente
        self.modelo = Modelo_Paciente_()
        self.cargarTerapeuta()
        self.InicializarGui()
        #self.cargarReportesXTerapeuta()
        #self.cargarTablaTeraPacientes()

    def InicializarGui(self):

        #print(type, self.user)
        self.ui.lbUsuario.setText(self.paciente)
        #self.ui.pushButton.clicked.connect(self.abrirReporteEspecifico)




    def cargarTerapeuta(self):



        datos = self.modelo.cargarPlaceHolder(self.paciente)

        ListaDatos = datos[0]
        print("Soy datos 1 "+str(ListaDatos))

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
        self.ui.lbNacionalidad.setText(str(ListaDatos[10]))
        self.ui.etfDiagnostico.setText(ListaDatos[11])

        datos2 = self.modelo.cargarEstadoAndMunicipio(str(ListaDatos[14]))
        print("Soy datos 2" +str(datos2))
        ListaDatos2 = datos2[0]
        print(ListaDatos2)
        self.ui.lbEstado.setText(ListaDatos2[0])
        self.ui.lbMunicipio.setText(ListaDatos2[1])

        self.ui.lbLocalida.setText(ListaDatos[7])
        self.ui.lbDomicilio.setText(ListaDatos[8]+ " #"+str(ListaDatos[9]))
        self.ui.lbContacto.setText(str(ListaDatos[6]))
        self.ui.lbCodPostal.setText(str(ListaDatos[12]))
        self.ui.lbCorreo.setText(ListaDatos[13])

        print("El paciente tiene tutor "+ str(ListaDatos[14]))
        if str(ListaDatos[15]) == '0':
            self.ui.lbTutor.setText("Sin_Tutor")
        else:
            nombreTutor =  self.modelo.recuperarNombreTutor(str(ListaDatos[15]))
            self.ui.lbTutor.setText(str(nombreTutor[0][0])+ " "+str(nombreTutor[0][1]))

    def cargarReportesXTerapeuta(self):

        datosidT = self.modelo.cargarPlaceHolder(self.user)
        ListaDatos2 = datosidT[0]
        print("Datos del terapeuta: "+str(ListaDatos2))

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

