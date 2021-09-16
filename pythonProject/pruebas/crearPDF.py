from PaPDF import PaPDF

def crear_pdf(archivo):
    with PaPDF(archivo) as pdf:
        pdf.setFontSize(18)
        pdf.addImage("idea-genial.png", 15,270,20,20)
        pdf.addText(40, 280, "CogniDron-EEG")
        pdf.setFontSize(10)
        pdf.addText(50, 275, "Reporte Terapeutico")

        pdf.addTrueTypeFont("DejaVuSans", "DejaVuSans.ttf")
        pdf.setFont("DejaVuSans")
        pdf.setFontSize(9)

        pdf.addText(200, 28, "Fecha")

        pdf.addImage("reporte.png", 15,242,8,8)
        pdf.addText(24, 244, "Datos de la sesión")
        pdf.addText(24, 236, "Numero de la sesión:")
        pdf.addText(24, 230, "Funcion Cognitiva:")
        pdf.addText(24, 224, "Tipo de bandas:")
        pdf.addText(24, 218, "Division Theta/Beta:")
        pdf.addText(24, 212, "Area del cerebo:")
        pdf.addText(24, 206, "Duracion de la sesión:")
        pdf.addText(24, 200, "Nombre del ejercicio:")
        pdf.addText(24, 194, "Numero de aciertos:")

        #Datos de la sesion obtenidos de la bas de datos

        text = ("")
        pdf.addText(65, 236, "xxxx")
        pdf.addText(65, 230, "xxxx")
        pdf.addText(65, 224, "xxxx")
        pdf.addText(65, 218, "xxxx")
        pdf.addText(65, 212, "xxxx")
        pdf.addText(65, 206, "xxxx")
        pdf.addText(65, 200, "xxxx")
        pdf.addText(65, 194, "xxxx")


        #Datos del terapeuta
        pdf.addImage("terapeuta.png", 15,175,8,8)
        pdf.addText(24, 177, "Datos del terapeuta")

        pdf.addText(24, 169, "Nombre:")
        pdf.addText(24, 163, "Contacto:")
        pdf.addText(24, 157, "Estatus:")

        #Datos recumerados e insertados
        pdf.addText(65, 169, "xxxx")
        pdf.addText(65, 163, "xxxx")
        pdf.addText(65, 157, "xxxx")

        #Datos de paciente
        pdf.addImage("paciente.png", 15,135,8,8)
        pdf.addText(24, 137, "Datos del paciente")
        pdf.addText(24, 129, "Nombre:")
        pdf.addText(24, 123, "Edada:")
        pdf.addText(24, 117, "Tutor:")
        pdf.addText(24, 111, "Localidad:")
        pdf.addText(24, 105, "Contacto:")

        #Datos recumerados e insertados
        pdf.addText(65, 129, "xxxx")
        pdf.addText(65, 123, "xxxx")
        pdf.addText(65, 117, "xxxx")
        pdf.addText(65, 111, "xxxx")
        pdf.addText(65, 105, "xxxx")


        pdf.setLineThickness(0.5)
        pdf.setFontSize(12)
        pdf.addText(20,160,text)
        w = pdf.getTextWidth(text)

        pdf.addLine(20,158.5,20,158.5)


#crear_pdf("archivo2.pdf")