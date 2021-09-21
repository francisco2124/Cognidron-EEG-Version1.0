


from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore
from vistas.agregarTutor import Ui_DialogAgregarTerapeuta
from modelos.ModeloTutor import Modelo_Tutor_
from modelos.ModeloTerapeuta import Modelo_Terapeuta
from PyQt5.QtGui import QIntValidator
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
import re



#En esta clase se inserta codigo que permita a la vista realizar distintos comportamientos sin modificar el archivo principal de la vista

class Controlador_AgrgarTutor(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        print("soy la vista de agregar terapeutas")
        self.ui= Ui_DialogAgregarTerapeuta()
        self.modelo = Modelo_Tutor_()
        self.ui.setupUi(self)
        self.inicializarGUI()
        self.cargarMunicipio()
        self.ui.cbEstado.currentIndexChanged[str].connect(self.cargarMunicipio)

    #Inicializar elemntos por ejemplo darle funcionamiento a los botones
    def inicializarGUI(self):
        # self.pp = self.ui.leApellidoPaterno.text()
        self.cargarEstados()
        self.ui.btnRegistrar.clicked.connect(self.agregarterapeuta)
        self.ui.btnCancelar.clicked.connect(self.limpiarCampos)

        self.validarNumero = QRegExpValidator(QRegExp("^[0-9]+$ ") , self)
        self.validarCadenaSinEspacio= QRegExpValidator(QRegExp("[a-zA-Zñ]+"), self)
        self.validarCadenaEspacio= QRegExpValidator(QRegExp("[a-zA-Z  ñ]+"), self)

        self.ui.leNumeroContacto.setValidator(self.validarNumero)
        self.ui.leCodigoPostal.setValidator(self.validarNumero)
        self.ui.leNacionalidad.setValidator(self.validarCadenaSinEspacio)
        self.ui.leApellidoPaterno.setValidator(self.validarCadenaEspacio)
        self.ui.leApellidoMaterno.setValidator(self.validarCadenaEspacio)




    #Cargar comb box con estados
    def cargarEstados(self):

        estados =  self.modelo.cargarEstados()
        #print(estados)

        combo = self.ui.cbEstado
        combo.clear()
        combo.addItems([str(x[1]) for x in estados])

    #llenar el combo box de municipios con base al estado
    def cargarMunicipio(self):

        Estado = self.modelo.recuperarIdEstado(self.ui.cbEstado.currentText())
        #print(Estado)
        idEstado = Estado[0]
        #print(idEstado[0])

        municipios =  self.modelo.cargarMunicipios(idEstado[0])
       # print(municipios)

        combo = self.ui.cbMunicipio
        combo.clear()
        combo.addItems([str(x[1]) for x in municipios])


    #Obtener un tecxto del campo de fecha
    def getdate(self):

        date = self.ui.dateEdit.text()

        #print(date)

    #Funcion principal para agregar un terapeuta
    def agregarterapeuta(self):


        #Funcion para validar si es numero
        def validrSiesNum(cadena):

            try:
                int(cadena)
                return False
            except ValueError:
                return True
        #Funcion para validar si el correo tiene un @

        def validarCamposConEspacios(campo):

            if len(campo) == 0 or not re.fullmatch(r"[A-Za-zñ ]{1,500}", campo) :
                return True
            else:
                return False
        def validarCamposConEspaciosNoObligatorios(campo):

            if not re.fullmatch(r"[A-Za-zñ ]{1,500}", campo) :
                return True
            else:
                return False

        def validarCorreo(campo):

            if not re.fullmatch(r"[0-9-A-Za-zñ@.]{1,500}", campo) :
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

        #Obtener el texto de los elementos del formulario para gregar un terapeuta
        nombre = self.ui.leNombres.text().strip()
        app = self.ui.leApellidoPaterno.text().strip()
        apm = self.ui.leApellidoMaterno.text().strip()
   #---------------------------------------------------------------
        #Obtener el tipo de genero seleccionado
        if self.ui.rbMasculino.isChecked()==True:
            genero = self.ui.rbMasculino.text().strip()

        elif self.ui.rbFemenino.isChecked()==True:
            genero = self.ui.rbFemenino.text().strip()
    #--------------------------------------------------------------------
        codPostal = self.ui.leCodigoPostal.text().strip()
        localidad = self.ui.leLoclidad.text().strip()
        calle = self.ui.leCalle.text().strip()
        num = self.ui.leNumeroCalle.text().strip()
        nacionalidad = self.ui.leNacionalidad.text().strip()
        contacto = self.ui.leNumeroContacto.text().strip()
        correoElec = self.ui.leCorreoElectronico.text().strip()

        idEstado = self.ui.cbEstado.currentText()
        date = self.ui.dateEdit.text()

        #Almacenar directamente una cantidad determinada de caracteres caracteres
        #cadena1 = "Hola Mundo"
        #cadena2 = cadena1[1:8]

        #Validarcion de los campos
        #El campo Nacionalidad, Estado, Municipio, Localidad, codigo postal y Domicilio con numero NO SON OBLIGATORIOS
        if validarCamposConEspacios(app):
            Alerta = QMessageBox.information(self, 'Alerta', "Ingresa un Apellido Paterno", QMessageBox.Ok)
        elif validarCamposConEspacios(apm):
            Alerta = QMessageBox.information(self, 'Alerta', "Ingresa un Apellido Materno", QMessageBox.Ok)
        elif validarCamposConEspacios(nombre):
            Alerta = QMessageBox.information(self, 'Alerta', "Ingresa el Nombre usando letras y espacios", QMessageBox.Ok)
        #Validar Genero
        elif self.ui.rbMasculino.isChecked()==False and self.ui.rbFemenino.isChecked()==False:
            Alerta = QMessageBox.information(self, 'Alerta', "Selecciona un genero", QMessageBox.Ok)
        elif date == "01/01/1921":
            Alerta = QMessageBox.information(self, 'Alerta', "Selecciona la fecha", QMessageBox.Ok)
        #Validar campo no obligatorios
        elif len(nacionalidad) >= 1 and nacionalidad.isalpha() == False:
            Alerta = QMessageBox.information(self, 'Alerta', "Ingresa la Nacionalidad usando solo letras", QMessageBox.Ok)
        elif len(localidad) >= 1 and validarCamposConEspaciosNoObligatorios(localidad):
            Alerta = QMessageBox.information(self, 'Alerta', "Ingresa la Localidad usando letras y espacios", QMessageBox.Ok)
        elif len(calle) >= 1 and validarCamposConEspaciosNoObligatorios(calle):
            Alerta = QMessageBox.information(self, 'Alerta', "Ingresa la Calle usando letras y espacios", QMessageBox.Ok)
        elif len(num) > 0 and validrSiesNum(num):
            Alerta = QMessageBox.information(self, 'Alerta', "Ingresa el numero de vivienda usando solo numero", QMessageBox.Ok)
        elif len(codPostal) > 0 and len(codPostal) != 5:
            Alerta = QMessageBox.information(self, 'Alerta', "El campo codigo postal debe tener 5 numeros", QMessageBox.Ok)
        #Continuar validadno campos obligatorios
        elif len(contacto) != 10 :
            Alerta = QMessageBox.information(self, 'Alerta', "Ingresa un numero de contacto de 10 digitos solo usando numero ", QMessageBox.Ok)
        elif len(correoElec) == 0 or validarCorreo(correoElec) or validarCorreo2(correoElec) or validararroba(correoElec) ==  False or validarpunto(correoElec) ==False:
            Alerta = QMessageBox.information(self, 'Alerta', "Ingresa un correo electronico con entradas alfanumericas, puntos y un @ ", QMessageBox.Ok)

        else:

                print("Datos extras")
                idMun = self.modelo.recuperarIdMunicipio(self.ui.cbMunicipio.currentText())
                idMunicipio = idMun[0]
                print("El id de municipio es: "+str(idMunicipio[0]))

                if self.ui.rbMasculino.isChecked()==True:
                    genero = "Masculino"
                else:
                  genero = "Femenino"

                borradoLogico = "0"

                #Asignar un valor en blanco a los campos no obligatorios
                if len(nacionalidad) == 0:
                    nacionalidad = ""
                if len(localidad) == 0:
                    localidad = ""
                if len(calle) == 0:
                    calle = ""
                if len(num) == 0:
                    num = 0
                if len(codPostal) == 0:
                    codPostal = 0


                self.modelo.agregarTuor(app, apm, nombre,genero, date, codPostal,localidad, calle, num,
                                nacionalidad, contacto, correoElec, idMunicipio[0], borradoLogico)

                Alerta = QMessageBox.information(self, 'Confirmacion', "Se ha registrado un nuevo usuario", QMessageBox.Ok)
                self.limpiarCampos()
    #Colocar los campos de texto en blanco

    def limpiarCampos(self):
        self.ui.leApellidoPaterno.setText("")
        self.ui.leApellidoMaterno.setText("")
        self.ui.leNombres.setText("")
        self.ui.leNacionalidad.setText("")
        self.ui.leLoclidad.setText("")
        self.ui.leCalle.setText("")
        self.ui.leNumeroContacto.setText("")
        self.ui.leNumeroCalle.setText("")
        self.ui.leCodigoPostal.setText("")
        self.ui.leNumeroContacto.setText("")
        self.ui.leCorreoElectronico.setText("")








