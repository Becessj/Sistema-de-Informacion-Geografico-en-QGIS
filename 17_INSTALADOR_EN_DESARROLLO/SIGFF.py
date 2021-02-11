import os
import subprocess
from tkinter import*

ventana=Tk()
ventana.geometry("820x312")
ventana.title("GUAMAN POMA DE AYALA")
imagen=PhotoImage(file="gpa.png")

fondo=Label(ventana,image=imagen).place(x=0,y=0)
def abrir():
    os.startfile("C:\PYTHON3\QGIS.exe")

B1 = Button(text = "MUNICIPALIDAD PROVINCIAL DE CALCA", command = abrir).place(x = 100,y = 100)




