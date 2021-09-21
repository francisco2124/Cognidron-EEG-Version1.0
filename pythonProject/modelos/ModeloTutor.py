import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from pymysql import  *
from PyQt5 import QtWidgets as qtw
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

#



class Modelo_Tutor_(QtWidgets.QMainWindow):

    def __init__(self):

        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            passwd="root0",
            db="cognidroneeg"
         )





    def agregarTuor(self, app, apm, nombre,genero, date, codPostal,localidad, calle, num,
                nacionalidad, numero , correoElec, idMunicipio, borradoLogico):

        connectionAgregar = pymysql.connect(
            host="localhost",
            user="root",
            passwd="root0",
            db="cognidroneeg"
        )

        cursor = connectionAgregar.cursor()

        sql = '''INSERT INTO tutor (ape_paterno,ape_materno, nombre, genero, fecha_nacimiento, cod_postal, localidad, calle, num, nacionalidad, numero_contacto ,
         correo_electronico, Municipio_idMunicipio, borradoLogico) 
        VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}' , '{}', '{}', '{}', '{}', '{}', '{}', '{}')'''.format(app, apm, nombre,genero, date, codPostal,localidad, calle, num,
                                                                                                        nacionalidad, numero , correoElec, idMunicipio, borradoLogico)

        cursor.execute(sql)
        connectionAgregar.commit()
        connectionAgregar.close()

    def cargarTabla(self):
        connection2 = pymysql.connect(
            host="localhost",
            user="root",
            passwd="root0",
            db="cognidroneeg"
        )
        cursor = connection2.cursor()

        sql = "SELECT idTutor, nombre, ape_paterno, ape_materno, numero_contacto, correo_electronico FROM tutor " \
              " where borradoLogico = '0' and idTutor > 0"
        cursor.execute(sql)
        cursor.close()
        registro = cursor.fetchall()
        return registro

    def contenoPacientes(self):
        connection2 = pymysql.connect(
            host="localhost",
            user="root",
            passwd="root0",
            db="cognidroneeg"
        )
        cursor = connection2.cursor()

        sql = "SELECT idTutor, nombre, ape_paterno, ape_materno, numero_contacto, correo_electronico FROM tutor " \
              " where borradoLogico = '0' and idTutor > 0"
        cursor.execute(sql)
        cursor.close()
        registro = cursor.fetchall()
        return registro

    def elimina_tutor(self,idTerapeuta):
        self.connection.close()
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            passwd="root0",
            db="cognidroneeg"
        )
        cursor = self.connection.cursor()
        sql='''DELETE  FROM tutor WHERE idTutor ='{}' '''.format(idTerapeuta)
        cursor.execute(sql)
        self.connection.commit()



    #
    def editar(self, nombre,app,apm,genero,date, codPostal,localidad, calle, num, nacionalidad, numeroContc, correoelc,idMunicipio, idTerapeuta):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            passwd="root0",
            db="cognidroneeg"
        )
        cursor = self.connection.cursor()
        date2 = date.strip()
        sql ='''UPDATE terapeuta SET  nombre  ='{}', ape_paterno ='{}', ape_materno ='{}', genero ='{}', fecha_nacimiento ='{}',
         cod_postal ='{}', localidad ='{}',
        calle ='{}', num ='{}', nacionalidad ='{}',  numero_contacto ='{}', correo_electronico ='{}',
        Municipio_idMunicipio ='{}' WHERE idTrapeuta = '{}'
         '''.format(nombre,app,apm,genero,date, codPostal,localidad, calle, num, nacionalidad, numeroContc, correoelc, idMunicipio,
                    idTerapeuta)

        #calle =' {}', num =' {}', nacionalidad =' {}',  numero_contacto =' {}', correo_electronico =' {}', name_usuario =' {}',  Estadado_idEstadado =' {}'

        cursor.execute(sql)
        self.connection.commit()
        self.connection.close()


    def cargarPlaceHolder(self, user):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            passwd="root0",
            db="cognidroneeg"
        )
        cursor = self.connection.cursor()
        sql = '''SELECT ape_paterno, ape_materno, nombre, genero, fecha_nacimiento,  nacionalidad, localidad,calle, num, cod_postal, numero_contacto, correo_electronico,
        idTrapeuta, Municipio_idMunicipio, user.tipo FROM terapeuta INNER JOIN usuarios user ON (user.nombreUsuario = terapeuta.usuarios_nombreUsuario) WHERE user.nombreUsuario = '{}'  '''.format(user)
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def cargarEstados(self):
        cursor = self.connection.cursor()
        sql = '''SELECT idEstadado, nombre FROM estado '''
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def recuperarIdEstado(self, nombre):
        cursor = self.connection.cursor()
        sql = '''SELECT idEstadado, nombre FROM estado WHERE nombre = '{}'  '''.format(nombre)
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def recuperarIdMunicipio(self, nombre):
        cursor = self.connection.cursor()
        sql = '''SELECT idMunicipio FROM municipio WHERE nombre = '{}'  '''.format(nombre)
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def cargarMunicipios(self, idEstado):
        cursor = self.connection.cursor()
        sql = '''SELECT idMunicipio, nombre FROM municipio WHERE Estadado_idEstadado = '{}'  '''.format(idEstado)
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def cargarEstadoAndMunicipio(self, idMunicipio):
        cursor = self.connection.cursor()
        sql = '''SELECT est.nombre, mun.nombre FROM municipio mun INNER JOIN estado est ON (est.idEstadado = mun.Estadado_idEstadado) WHERE idMunicipio = '{}'  '''.format(idMunicipio)
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def validarUsuarioRepetido(self, usuario):
        cursor = self.connection.cursor()

        sql = "SELECT tipo FROM usuarios WHERE nombreUsuario = '{}'".format(usuario)

        cursor.execute(sql)
        registro = cursor.fetchall()
        if(len(registro) == 0):
            registro = False
        else:
            registro = True
        self.connection.commit()
        return registro

    def recuperarTutores(self):


        self.connection = pymysql.connect(
                host="localhost",
                user="root",
                passwd="root0",
                db="cognidroneeg"
            )
        cursor = self.connection.cursor()
        sql = '''SELECT nombre FROM tutor where borradoLogico = '0' and idTutor > 0'''
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro
        self.connection.close()

    def validarBorradoLigico(self, user):
        cursor = self.connection.cursor()

        sql='''SELECT idPaciente  FROM paciente WHERE Tutor_idTutor =' {}' '''.format(user)

        cursor.execute(sql)
        registro = cursor.fetchall()
        if(len(registro) == 0):
            registro = False
        else:
            registro = True
        self.connection.commit()
        return registro
    def validarBorradoLigico2(self, user):
        cursor = self.connection.cursor()

        sql="SELECT idTutor FROM tutor " \
            " WHERE correo_electronico ='{}'".format(user)

        cursor.execute(sql)
        registro = cursor.fetchall()

        self.connection.commit()
        return registro

    def elimina_tutorLogico(self,id):
        cursor = self.connection.cursor()
        sql ="UPDATE tutor SET  borradoLogico  = '1' WHERE idTutor = '{}' ".format(id)

        cursor.execute(sql)
        self.connection.commit()
        self.connection.close()

    def cargarTablaxTutor(self, nombreTep):
        cursor = self.connection.cursor()
        sql = "SELECT idTutor, nombre, ape_paterno, ape_materno, numero_contacto, correo_electronico FROM tutor " \
              " where nombre = '{}'".format(nombreTep)
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro


#--------------------------Vista consultar terapeuta seleccionado-------------------------

    def cargarTablaXSesionTera(self, idTerapeuta):

        connection2 = pymysql.connect(
            host="localhost",
            user="root",
            passwd="root0",
            db="cognidroneeg"
        )
        cursor = connection2.cursor()
        sql = "SELECT idSesionTerapeutica, identificador, fecha, ejer.nombre, tiempo, pati.nombre, tera.nombre FROM sesionterapeutica sesio " \
              "INNER JOIN ejercicios ejer ON (ejer.idEjercicios = sesio.Ejercicios_idEjercicios)" \
              "INNER JOIN paciente pati ON (pati.idPaciente = sesio.Paciente_idPaciente)" \
              "INNER JOIN terapeuta tera ON (tera.idTrapeuta = sesio.Terapeuta_idTrapeuta) WHERE Terapeuta_idTrapeuta = '{}' ".format(idTerapeuta)

        cursor.execute(sql)
        cursor.close()
        registro = cursor.fetchall()
        return registro

    def cargarTablaxTeraPaciente(self, idTerapeuta):
        cursor = self.connection.cursor()
        sql = "SELECT pati.idPaciente, pati.nombre, pati.localidad FROM terapeuta " \
              "INNER JOIN terapeuta_has_paciente TeHasPa ON (TeHasPa.terapeuta_idTrapeuta = terapeuta.idTrapeuta)"\
              "INNER JOIN paciente pati ON (pati.idPaciente = TeHasPa.paciente_idPaciente) where idTrapeuta = '{}'".format(idTerapeuta)
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro


    def cambiarPass(self,newPass,nameUser):
        connection2 = pymysql.connect(
            host="localhost",
            user="root",
            passwd="root0",
            db="cognidroneeg"
        )
        cursor = connection2.cursor()
        sql ="UPDATE usuarios SET  password  ='{}' WHERE nombreUsuario = '{}' ".format(newPass,nameUser).strip()
        cursor.execute(sql)
        connection2.commit()
