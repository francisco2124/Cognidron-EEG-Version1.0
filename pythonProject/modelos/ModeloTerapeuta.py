import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from pymysql import  *
from PyQt5 import QtWidgets as qtw
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

#



class Modelo_Terapeuta(QtWidgets.QMainWindow):

    def __init__(self):

        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            passwd="root0",
            db="cognidroneeg"
         )

    def validarLogin(self, usuario, password):



        cursor = self.connection.cursor()

        sql = "SELECT tipo FROM usuarios WHERE nombreUsuario = '{}' AND password = '{}'".format(password, usuario)

        cursor.execute(sql)
        registro = cursor.fetchall()
        if(len(registro) == 0):
            registro = False
        else:
            registro = True
        self.connection.commit()
        #self.connection.close()
        return registro

    def agregarUsario(self, user, password,tipo):

        connectionAgregar = pymysql.connect(
            host="localhost",
            user="root",
            passwd="root0",
            db="cognidroneeg"
        )

        cursor = connectionAgregar.cursor()

        sql = '''INSERT INTO usuarios (nombreUsuario, password, tipo) 
        VALUES('{}', '{}','{}')'''.format(user, password, tipo)

        cursor.execute(sql)
        connectionAgregar.commit()
        connectionAgregar.close()



    def agregar(self, app, apm, nombre,genero, date, codPostal,localidad, calle, num,
                nacionalidad, numero , correoElec, borradoLogico, idMunicipio, nombreUsuario):

        connectionAgregar = pymysql.connect(
            host="localhost",
            user="root",
            passwd="root0",
            db="cognidroneeg"
        )

        cursor = connectionAgregar.cursor()

        sql = '''INSERT INTO terapeuta (ape_paterno,ape_materno, nombre, genero, fecha_nacimiento, cod_postal, localidad, calle, num, nacionalidad, numero_contacto ,
         correo_electronico, borradoLogico, Municipio_idMunicipio, usuarios_nombreUsuario) 
        VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}' , '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')'''.format(app, apm, nombre,genero, date, codPostal,localidad, calle, num,
                                                                                                        nacionalidad, numero , correoElec, borradoLogico, idMunicipio, nombreUsuario)

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

        sql = "SELECT idTrapeuta, user.nombreUsuario, nombre, ape_paterno, ape_materno, numero_contacto FROM terapeuta " \
              "INNER JOIN usuarios user ON (user.nombreUsuario = terapeuta.usuarios_nombreUsuario) where borradoLogico = '0' "
        cursor.execute(sql)
        cursor.close()
        registro = cursor.fetchall()
        return registro

    def cargarTablaTerapeutasEliminados(self):
        connection2 = pymysql.connect(
            host="localhost",
            user="root",
            passwd="root0",
            db="cognidroneeg"
        )
        cursor = connection2.cursor()

        sql = "SELECT idTrapeuta, user.nombreUsuario, nombre, ape_paterno, ape_materno, user.tipo FROM terapeuta " \
              "INNER JOIN usuarios user ON (user.nombreUsuario = terapeuta.usuarios_nombreUsuario) where borradoLogico = '1'"
        cursor.execute(sql)
        cursor.close()
        registro = cursor.fetchall()
        return registro
    def cargarTablaTerapeutasEliminados(self):
        connection2 = pymysql.connect(
            host="localhost",
            user="root",
            passwd="root0",
            db="cognidroneeg"
        )
        cursor = connection2.cursor()

        sql = "SELECT idTrapeuta, user.nombreUsuario, nombre, ape_paterno, ape_materno, user.tipo FROM terapeuta " \
              "INNER JOIN usuarios user ON (user.nombreUsuario = terapeuta.usuarios_nombreUsuario) where borradoLogico = '1'"
        cursor.execute(sql)
        cursor.close()
        registro = cursor.fetchall()
        return registro

    def cargarTablaTerapeutasEliminadosXTipo(self,tipo):
        connection2 = pymysql.connect(
            host="localhost",
            user="root",
            passwd="root0",
            db="cognidroneeg"
        )
        cursor = connection2.cursor()

        sql = "SELECT idTrapeuta, user.nombreUsuario, nombre, ape_paterno, ape_materno, user.tipo FROM terapeuta " \
              "INNER JOIN usuarios user ON (user.nombreUsuario = terapeuta.usuarios_nombreUsuario) where borradoLogico = '1' and user.tipo = '{}'  ".format(tipo)
        cursor.execute(sql)
        cursor.close()
        registro = cursor.fetchall()
        return registro

    def elimina_terapeuta(self,idTerapeuta):
        self.connection.close()
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            passwd="root0",
            db="cognidroneeg"
        )
        cursor = self.connection.cursor()
        sql='''DELETE  FROM terapeuta WHERE idTrapeuta = '{}' '''.format(idTerapeuta)
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

    def editarTipoUsuario(self, tipoUusario, nombreUsuario):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            passwd="root0",
            db="cognidroneeg"
        )
        cursor = self.connection.cursor()

        sql ='''UPDATE  usuarios SET   tipo ='{}' WHERE nombreUsuario = '{}' '''.format(tipoUusario, nombreUsuario)

        cursor.execute(sql)
        self.connection.commit()
        self.connection.close()



    def recuperarTerapeutaConBorradoLogico(self, idTerapeuta, desactivarBorradoLogico):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            passwd="root0",
            db="cognidroneeg"
        )
        cursor = self.connection.cursor()
        sql ='''UPDATE terapeuta SET  borradoLogico  ='{}' WHERE idTrapeuta = '{}' '''.format(desactivarBorradoLogico, idTerapeuta)
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
        sql = '''SELECT idEstado, nombre FROM estado'''
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def recuperarIdEstado(self, nombre):
        cursor = self.connection.cursor()
        sql = '''SELECT idEstado, nombre FROM estado WHERE nombre = '{}'  '''.format(nombre)
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
        sql = '''SELECT idMunicipio, nombre FROM municipio WHERE Estadado_idEstado = '{}'  '''.format(idEstado)
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def cargarEstadoAndMunicipio(self, idMunicipio):
        cursor = self.connection.cursor()

        sql = '''SELECT est.nombre, mun.nombre FROM municipio mun INNER JOIN estado est ON (est.idEstado = mun.Estadado_idEstado) WHERE idMunicipio = '{}'  '''.format(idMunicipio)
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

    def recuperarTerapeutas(self):


        self.connection = pymysql.connect(
                host="localhost",
                user="root",
                passwd="root0",
                db="cognidroneeg"
            )
        cursor = self.connection.cursor()
        sql = '''SELECT nombre FROM terapeuta where borradoLogico = '0' '''
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro
        self.connection.close()

    def validarBorradoLigico(self, user):
        cursor = self.connection.cursor()

        sql='''SELECT Terapeuta_idTrapeuta  FROM sesionterapeutica WHERE Terapeuta_idTrapeuta =' {}' '''.format(user)

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

        sql="SELECT idTrapeuta FROM terapeuta " \
            "INNER JOIN usuarios user ON (user.nombreUsuario = terapeuta.usuarios_nombreUsuario) where usuarios_nombreUsuario = '{}'".format(user)

        cursor.execute(sql)
        registro = cursor.fetchall()

        self.connection.commit()
        return registro

    def elimina_terapeutaLogico2(self,id):
        cursor = self.connection.cursor()
        sql ="UPDATE terapeuta SET  borradoLogico  = '1' WHERE idTrapeuta = '{}' ".format(id)

        cursor.execute(sql)
        self.connection.commit()
        self.connection.close()

    def cargarTablaxTerapeuta(self, nombreTep):
        cursor = self.connection.cursor()
        sql = "SELECT idTrapeuta, user.nombreUsuario, nombre, ape_paterno, ape_materno, numero_contacto FROM terapeuta " \
              "INNER JOIN usuarios user ON (user.nombreUsuario = terapeuta.usuarios_nombreUsuario) where nombre = '{}'".format(nombreTep)
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
        sql = "SELECT idSesionTerapeutica, idSesionTerapeutica, fecha, ejer.nombre, tiempo, pati.nombre, tera.nombre FROM sesionterapeutica sesio " \
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

    def recuperarCredenciales(self, correo):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            passwd="root0",
            db="cognidroneeg"
        )
        cursor = self.connection.cursor()
        sql = '''SELECT user.nombreUsuario, user.password  FROM terapeuta tera INNER JOIN usuarios user ON
         (user.nombreUsuario = tera.usuarios_nombreUsuario) WHERE tera.correo_electronico = '{}'  '''.format(correo)
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro