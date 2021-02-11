import os
import subprocess
import sys, string, os
from tkinter import*
import time
ventana=Tk()
ventana.geometry("820x312")
ventana.title("GUAMAN POMA DE AYALA")
imagen=PhotoImage(file="gpa.png")
fondo=Label(ventana,image=imagen).place(x=0,y=0)
ventana.after(5000, lambda: ventana.destroy()) # Cerrar el frame despues de 5 segundos para ejecutar os
ventana.mainloop()
command  = r"C:\OSGeo4W64\bin\qgis-bin.exe"
os.system(command)

