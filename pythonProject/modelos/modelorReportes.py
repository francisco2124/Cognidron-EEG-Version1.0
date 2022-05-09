import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from pymysql import  *
from PyQt5 import QtWidgets as qtw
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton




class Modelo_Reportes(QtWidgets.QMainWindow):

    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            passwd="root0",
            db="cognidroneeg"
        )
    #Funciones

    def cargarTabla(self):

        connection2 = pymysql.connect(
            host="localhost",
            user="root",
            passwd="root0",
            db="cognidroneeg"
        )
        cursor = connection2.cursor()
        sql = "SELECT idSesionTerapeutica, fecha, ejer.nombre, tiempo, pati.nombre, tera.nombre FROM sesionterapeutica sesio " \
              "INNER JOIN ejercicios ejer ON (ejer.idEjercicios = sesio.Ejercicios_idEjercicios)" \
              "INNER JOIN paciente pati ON (pati.idPaciente = sesio.Paciente_idPaciente)" \
              "INNER JOIN terapeuta tera ON (tera.idTrapeuta = sesio.Terapeuta_idTrapeuta)"

        cursor.execute(sql)
        cursor.close()
        registro = cursor.fetchall()
        return registro

    def cargarTablaXPaciente(self, nombre):

        connection2 = pymysql.connect(
            host="localhost",
            user="root",
            passwd="root0",
            db="cognidroneeg"
        )
        cursor = connection2.cursor()
        sql = "SELECT idSesionTerapeutica, fecha, ejer.nombre, tiempo, pati.nombre, tera.nombre FROM sesionterapeutica sesio " \
              "INNER JOIN ejercicios ejer ON (ejer.idEjercicios = sesio.Ejercicios_idEjercicios)" \
              "INNER JOIN paciente pati ON (pati.idPaciente = sesio.Paciente_idPaciente)" \
              "INNER JOIN terapeuta tera ON (tera.idTrapeuta = sesio.Terapeuta_idTrapeuta) WHERE pati.nombre = '{}' ".format(nombre)

        cursor.execute(sql)
        cursor.close()
        registro = cursor.fetchall()
        return registro



        cursor.execute(sql)
        cursor.close()
        registro = cursor.fetchall()
        return registro

    def cargarTablaXFeacha(self, Fecha):

        connection2 = pymysql.connect(
            host="localhost",
            user="root",
            passwd="root0",
            db="cognidroneeg"
        )
        cursor = connection2.cursor()
        sql = "SELECT idSesionTerapeutica, fecha, ejer.nombre, tiempo, pati.nombre, tera.nombre FROM sesionterapeutica sesio " \
              "INNER JOIN ejercicios ejer ON (ejer.idEjercicios = sesio.Ejercicios_idEjercicios)" \
              "INNER JOIN paciente pati ON (pati.idPaciente = sesio.Paciente_idPaciente)" \
              "INNER JOIN terapeuta tera ON (tera.idTrapeuta = sesio.Terapeuta_idTrapeuta) WHERE fecha = '{}' ".format(Fecha)

        cursor.execute(sql)
        cursor.close()
        registro = cursor.fetchall()
        return registro

    def busca_reporte(self, identificador):

    #fecha, ejer.tipo, tipoOndas, metaAlcanzada, metaEstablecida, tiempo, comentarios, ejer.idEjercicios, Paciente_idPaciente,
    #ejer.nombre
        cursor = self.connection.cursor()
        sql = '''SELECT pati.nombre, pati.ape_paterno, pati.fecha_nacimiento, pati.localidad, tuto.nombre, tuto.ape_paterno, pati.numero_contacto,
         tera.nombre, tera.ape_paterno, tera.fecha_nacimiento, tera.localidad, tera.borradoLogico, tera.numero_contacto,  
         sesio.fecha, ejer.nombre, sesio.funcionCognitiva , sesio.electrodosUtilizados ,sesio.tipoEjercicio, sesio.tiempo,
          sesio.promedioPotencia , sesio.frecuencia ,sesio.menorUmbral ,sesio.mejorUmbral, sesio.promedioUmbral, sesio.porcentajeUmbralTerapia
            ,sesio.comentarios, sesio.numUmbrales, sesio.primerUmbral FROM sesionterapeutica sesio ''' \
              '''INNER JOIN ejercicios ejer ON (ejer.idEjercicios = sesio.Ejercicios_idEjercicios)''' \
              '''INNER JOIN paciente pati ON (pati.idPaciente = sesio.Paciente_idPaciente) ''' \
              '''INNER JOIN tutor tuto ON (tuto.idTutor = pati.Tutor_idTutor) ''' \
              '''INNER JOIN terapeuta tera ON (tera.idTrapeuta = sesio.Terapeuta_idTrapeuta) WHERE idSesionTerapeutica = {}'''.format(identificador)
        cursor.execute(sql)
        registro = cursor.fetchall()

        return registro

    def recuperarPacientes(self):
        cursor = self.connection.cursor()
        sql = '''SELECT nombre FROM paciente '''
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def recuperarMetasAlcanzadas(self, idPaciente):
        cursor = self.connection.cursor()
        sql = '''SELECT metaAlcanzada FROM sesionterapeutica WHERE Paciente_idPaciente = {}'''.format(idPaciente)
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def cargar_reporte(self, identificador):


        cursor = self.connection.cursor()
        sql = '''SELECT  fecha,identificador, sesio.funcionCognitiva, tipoOndas, divisionThtaDeta, areaTrabajada, tiempo,  tera.nombre, ejer.tipo,  ejer.nombre, ejer.descripccion, 
        metaAlcanzada, metaEstablecida, tera.nombre, tera.numero_contacto, tera.borradoLogico, pati.nombre, pati.fecha_nacimiento, pati.localidad,
         pati.numero_contacto, comentarios, pati.idPaciente FROM sesionterapeutica sesio ''' \
              '''INNER JOIN ejercicios ejer ON (ejer.idEjercicios = sesio.Ejercicios_idEjercicios)''' \
              '''INNER JOIN paciente pati ON (pati.idPaciente = sesio.Paciente_idPaciente) ''' \
              '''INNER JOIN terapeuta tera ON (tera.idTrapeuta = sesio.Terapeuta_idTrapeuta) WHERE identificador = {}'''.format(identificador)
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def datosPaciente(self, identificador):
        cursor = self.connection.cursor()
        sql = '''SELECT  pat.fecha_nacimiento, tut.nombre, tut.ape_paterno FROM paciente pat ''' \
              '''INNER JOIN tutor tut ON (tut.idTutor = pat.Tutor_idTutor) WHERE idPaciente = {}'''.format(identificador)
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def registarTerpaiaNeurofeedback(self, fecha, funcionCognitiva, tiempo, tipoEjericio, puntosObtenidos, frecuencia,
                                    observaciones, promedioPotencia, elestrodos, mejorUmbral, promedioUmbral,
                                     menorUmbral, numUmbrales, primerUmbral, porcentajeUmbral, idPaciente, idTerapeuta, idEjercicio):
        connectionAgregar = pymysql.connect(
            host="localhost",
            user="root",
            passwd="root0",
            db="cognidroneeg"
        )

        cursor = connectionAgregar.cursor()

        sql = '''INSERT INTO sesionterapeutica (fecha, funcionCognitiva, tiempo, tipoEjercicio, puntosObtenidos, frecuencia, 
        comentarios, promedioPotencia, electrodosUtilizados, mejorUmbral, promedioUmbral, menorUmbral, numUmbrales, primerUmbral,
        porcentajeUmbralTerapia, Paciente_idPaciente, 
        Terapeuta_idTrapeuta, Ejercicios_idEjercicios) VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', 
        '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')'''.format(fecha, funcionCognitiva, tiempo, tipoEjericio, puntosObtenidos,
                                frecuencia, observaciones, promedioPotencia,elestrodos, mejorUmbral, promedioUmbral, menorUmbral,numUmbrales, primerUmbral,
                                                                                    porcentajeUmbral,idPaciente, idTerapeuta, idEjercicio)

        cursor.execute(sql)
        connectionAgregar.commit()
        connectionAgregar.close()



