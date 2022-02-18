# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from PyQt5 import QtWidgets
from cotroladores.Controladores_Login import Controlador_Login
from cotroladores.Controlador_PrincipalCognidron import Controlador_PrincipalCognidron
import sys


#Agregar o actualizar una vistas
# pyuic5 -x .ui -o .py


#Agrear o actualizar un archivo de imagenes
#pyrcc5 image.qrc -o images.py


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    app = QtWidgets.QApplication(sys.argv)
    controladorCognidron = Controlador_PrincipalCognidron()
    windowExample = Controlador_Login(controladorCognidron)
    windowExample.setWindowTitle('Login')
    windowExample.show()
    sys.exit(app.exec_())


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
