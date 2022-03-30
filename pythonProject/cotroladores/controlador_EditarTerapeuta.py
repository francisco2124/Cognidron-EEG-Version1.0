from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from vistas.editarTerapeuta import Ui_Dialog_EditarTerapeuta
#from cotroladores.ControladorTerapeuta import Control_Terapeuta
from PyQt5.QtGui import QIntValidator
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from cotroladores.controlador_CambiarPass import Controlador_CambiarPass

import math
from datetime import date
from datetime import datetime
import time

from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
import re


from modelos.ModeloTerapeuta import Modelo_Terapeuta
from zope.interface import named


class Control_EditarTerapeutas(QtWidgets.QMainWindow):

    def __init__(self, userTerapeuta):
        super().__init__()
        print("soy la vista de consultar terapeutas")
        self.ui= Ui_Dialog_EditarTerapeuta()
        self.ui.setupUi(self)
        self.NombreUsuario = userTerapeuta

        self.modelo = Modelo_Terapeuta()
        self.cargarPlaceHolder()
        self.InicializarGui()
        self.cargarMunicipio()
        self.ui.cbEstado.currentIndexChanged[str].connect(self.cargarMunicipio)

    def InicializarGui(self):

        self.cargarEstados()
        self.ui.btnAceptar.clicked.connect(self.editar)
        self.ui.btnCancelar.clicked.connect(self.limpiarCampos)
        self.ui.btnCambiarPass.clicked.connect(self.abrirCambiarPass)
        #self.ui.leUserName.setPlaceholderText(self.NombreUsuario)

        self.validarNumero = QRegExpValidator(QRegExp("^[0-9]+$ ") , self)
        self.validarCadenaSinEspacio= QRegExpValidator(QRegExp("[a-zA-Z  ñ]+"), self)

        self.ui.leNumeroContacto.setValidator(self.validarNumero)
        self.ui.leCodigoPostal.setValidator(self.validarNumero)
        self.ui.leNacionalidad.setValidator(self.validarCadenaSinEspacio)

        #Cargar comb box con estados
    def cargarEstados(self):

        datos = self.modelo.cargarPlaceHolder(self.NombreUsuario)

        ListaDatos = datos[0]

       # print("el ide del mun es: "+str(ListaDatos[13]))
        nombreEstado = self.modelo.cargarEstadoAndMunicipio(str(ListaDatos[13]))
        nameEstado = nombreEstado[0]
       # print("Recupere"+str(nameEstado[0]))

        estados =  self.modelo.cargarEstados()
        #print(estados)

        combo = self.ui.cbEstado
        combo.clear()
        combo.addItem(nameEstado[0])
        combo.addItems([str(x[1]) for x in estados])

    #llenar el combo box de municipios con base al estado
    def cargarMunicipio(self):

        Estado = self.modelo.recuperarIdEstado(self.ui.cbEstado.currentText())
        #print(Estado)
        idEstado = Estado[0]
        #print(idEstado[0])

        municipios =  self.modelo.cargarMunicipios(idEstado[0])
        # print(municipios)

        datos = self.modelo.cargarPlaceHolder(self.NombreUsuario)

        #Cargar primer elemnto
        ListaDatos = datos[0]

        nombreEstado = self.modelo.cargarEstadoAndMunicipio(str(ListaDatos[13]))
        nameEstado = nombreEstado[0]

        combo = self.ui.cbMunicipio
        combo.clear()
        combo.addItem(nameEstado[1])
        combo.addItems([str(x[1]) for x in municipios])

    def editar(self):

        datos = self.modelo.cargarPlaceHolder(self.NombreUsuario)

        ListaDatos = datos[0]
        print(ListaDatos[10])

        print("Se deitar el terapeuta")

        nombre = self.ui.leNombre.text().strip()
        if len(nombre) == 0:
            nombre = ListaDatos[2].strip()
        app = self.ui.leApePaterno.text().strip()
        if len(app) == 0:
            app = ListaDatos[0].strip()
        apm = self.ui.leApeMaterno.text().strip()
        if len(apm) == 0:
            apm = ListaDatos[1].strip()

        if self.ui.rbMasculino.isChecked()==True:
            genero = "Masculino"

        elif self.ui.rbFemenino.isChecked()==True:
            genero = "Femenino"
        dateMo = self.ui.dateEdit.text()
        dateM = str(dateMo).strip()



        nacionalidad = self.ui.leNacionalidad.text()
        if len(nacionalidad) == 0:
            nacionalidad = ListaDatos[5].strip()
        localidad = self.ui.leLocalidad.text()
        if len(localidad) == 0:
            localidad = ListaDatos[6].strip()
        calle = self.ui.leCalle.text()
        if len(calle) == 0:
            calle = ListaDatos[7].strip()
        num = self.ui.leNumero.text()
        if len(num) == 0:
            num = ListaDatos[8]
        codPostal = self.ui.leCodigoPostal.text()
        if len(codPostal) == 0:
            codPostal = ListaDatos[9]
        contacto = self.ui.leNumeroContacto.text()
        if len(contacto) == 0:
            contacto = ListaDatos[10].strip()
        correoElec = self.ui.leCorreoElectronico.text()
        if len(correoElec) == 0:
            correoElec = ListaDatos[11].strip()

        print("Datos extras")
        idMun = self.modelo.recuperarIdMunicipio(self.ui.cbMunicipio.currentText())
        idMunicipio = idMun[0]
        print("El id de municipio es: "+str(idMunicipio[0]))

        #genero = self.text()
        #fecha = self.leApellidoPaterno.text()

        idTerapeuta = ListaDatos[12]
        generoF = genero.strip()
        print("----"+dateM+"-----")

        def validarCamposConEspaciosNoObligatorios(campo):

            if not re.fullmatch(r"[A-Za-zñ ]{1,500}", campo) :
                return True
            else:
                return False

        #Funcion para validar si es numero
        def validrSiesNum(cadena):

            try:
                int(cadena)
                return False
            except ValueError:
                return True
        def validarCorreo(campo):

            if not re.fullmatch(r"[A-Za-zñ@.-0123456789]{1,500}", campo) :
                return True
            else:
                return False

        def validarCorreo2(campo):
            contador  = 0
            for i in campo:
                if i == "@":
                    contador = contador + 1
            if contador > 1:
                return True
            else:
                return False
        def validararroba(campo):

            if '@' in campo:
                return True
            else:
                return False

        def validarpunto(campo):

            if '.' in campo:
                return True
            else:
                return False
        def validarCodPostal(campo):
            if len(campo) != 5:
                return True
            else:
                return False

        if len(app) >= 1 and validarCamposConEspaciosNoObligatorios(app):
            Alerta = QMessageBox.information(self, 'Alerta', "Ingresa la Apellido Paterno usando letras y espacios", QMessageBox.Ok)

        elif len(apm) >= 1 and validarCamposConEspaciosNoObligatorios(apm):
            Alerta = QMessageBox.information(self, 'Alerta', "Ingresa la Apellido Materno letras y espacios", QMessageBox.Ok)

        elif len(nombre) >= 1 and validarCamposConEspaciosNoObligatorios(nombre):
            Alerta = QMessageBox.information(self, 'Alerta', "Ingresa la Nombre usando letras y espacios", QMessageBox.Ok)

        elif len(localidad) >= 1 and validarCamposConEspaciosNoObligatorios(localidad):
            Alerta = QMessageBox.information(self, 'Alerta', "Ingresa la Localidad usando letras y espacios", QMessageBox.Ok)

        elif len(calle) >= 1 and validarCamposConEspaciosNoObligatorios(calle):
            Alerta = QMessageBox.information(self, 'Alerta', "Ingresa la Calle usando letras y espacios", QMessageBox.Ok)

        elif len(nacionalidad) >= 1 and validarCamposConEspaciosNoObligatorios(nacionalidad):
            Alerta = QMessageBox.information(self, 'Alerta', "Ingresa la Nacionalidad usando letras y espacios", QMessageBox.Ok)
        elif len(str(codPostal)) > 0 and len(str(codPostal)) != 5:
            Alerta = QMessageBox.information(self, 'Alerta', "El campo codigo postal debe tener 5 numeros", QMessageBox.Ok)
        #Continuar validadno campos obligatorios
        elif len(contacto) != 10 :
            Alerta = QMessageBox.information(self, 'Alerta', "Ingresa un numero de contacto de 10 digitos solo usando numero ", QMessageBox.Ok)
        elif len(correoElec) == 0 or validarCorreo(correoElec) or validarCorreo2(correoElec) or validararroba(correoElec) ==  False or validarpunto(correoElec) ==False:
            Alerta = QMessageBox.information(self, 'Alerta', "Ingresa un correo electronico con entradas alfanumericas, puntos y un @ ", QMessageBox.Ok)

        else:


            self.modelo.editar(nombre,app,apm,generoF, dateM, codPostal,localidad, calle,num,nacionalidad,contacto,
                           correoElec,idMunicipio[0],idTerapeuta)

            if self.ui.cbAdmin.isChecked() == True:
                admin = 1
            else:
                admin = 0

            self.modelo.editarTipoUsuario(admin, self.NombreUsuario)

            Alerta = QMessageBox.information(self, 'Confirmacion', "Se edito el terapeuta", QMessageBox.Ok)
            self.cargarPlaceHolder()

    def cargarPlaceHolder(self):

        datos = self.modelo.cargarPlaceHolder(self.NombreUsuario)

        ListaDatos = datos[0]



        self.ui.leApePaterno.setPlaceholderText(str(ListaDatos[0]).strip())
        self.ui.leApeMaterno.setPlaceholderText(str(ListaDatos[1]).strip())
        self.ui.leNombre.setPlaceholderText(str(ListaDatos[2]).strip())
        if str(ListaDatos[3]).strip() == "Masculino" :

            self.ui.rbFemenino.setChecked(False)
            self.ui.rbMasculino.setChecked(True)
        print("El valor es:" + ListaDatos[4])

        fecha_dt = datetime.strptime(str(ListaDatos[4]).strip(), '%d/%m/%Y')
        self.ui.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(fecha_dt), QtCore.QTime(0, 0, 0)))
        self.ui.dateEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1920, 9, 26), QtCore.QTime(1, 0, 0)))

        self.ui.leNacionalidad.setPlaceholderText(str(ListaDatos[5]).strip())
        self.ui.leLocalidad.setPlaceholderText(str(ListaDatos[6]).strip())
        self.ui.leCalle.setPlaceholderText(str(ListaDatos[7]).strip())
        self.ui.leNumero.setPlaceholderText(str(ListaDatos[8]).strip())
        self.ui.leCodigoPostal.setPlaceholderText(str(ListaDatos[9]).strip())
        self.ui.leNumeroContacto.setPlaceholderText(str(ListaDatos[10]).strip())
        self.ui.leCorreoElectronico.setPlaceholderText(str(ListaDatos[11]).strip())

        print("Tipo = "+str(ListaDatos))

        if str(ListaDatos[14]) == "1":
            self.ui.cbAdmin.setChecked(True)
        else:
            self.ui.cbAdmin.setChecked(False)

    def limpiarCampos(self):
        self.ui.leApePaterno.setText("")
        self.ui.leApeMaterno.setText("")
        self.ui.leNombre.setText("")
        self.ui.leNacionalidad.setText("")
        self.ui.leLocalidad.setText("")
        self.ui.leCalle.setText("")
        self.ui.leNumeroContacto.setText("")
        self.ui.leNumero.setText("")
        self.ui.leCodigoPostal.setText("")
        self.ui.leCorreoElectronico.setText("")

    def abrirCambiarPass(self):


        self.abrir = Controlador_CambiarPass(self.NombreUsuario)
        self.abrir.show()



