import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from pymysql import  *
from PyQt5 import QtWidgets as qtw
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton




class Modelo_Ejercicios(QtWidgets.QMainWindow):

    def __init__(self):

        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            passwd="root0",
            db="cognidroneeg"
        )

    def recuperarEjercicios(self):
        cursor = self.connection.cursor()
        sql = "SELECT idEjercicios, nombre FROM ejercicios"
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def cargarTablaEjercicios(self):
        cursor = self.connection.cursor()
        sql = "SELECT idEjercicios, nombre, tipo  FROM ejercicios "
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def filtarEjercicios(self, tipoEjer):
        cursor = self.connection.cursor()
        sql = "SELECT idEjercicios, nombre, tipo  FROM ejercicios WHERE tipo = '{}'  ".format(tipoEjer)
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def consultarEjercicio(self, nombre):
        cursor = self.connection.cursor()
        sql = "SELECT descripccion, parametro1, parametro2, imagenes  FROM ejercicios WHERE nombre = '{}'  ".format(nombre)
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro




