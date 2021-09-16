import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from pymysql import  *
from PyQt5 import QtWidgets as qtw
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton




class Modelo_conexion(QtWidgets.QMainWindow):

    def __init__(self):

        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            passwd="root0",
            db="cognidroneeg"
        )


    def cargarDatos(self):
        cursor = self.connection.cursor()
        sql = "SELECT clientId, secretId FROM parametros "
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro


    def editar(self, clientId,secretId):

        cursor = self.connection.cursor()

        sql ='''UPDATE parametros SET  clientId  ='{}', secretId ='{}' WHERE idparametros ='1' '''.format(clientId,secretId)

        cursor.execute(sql)
        self.connection.commit()
        self.connection.close()

