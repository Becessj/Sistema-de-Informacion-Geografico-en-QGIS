import os
import subprocess
import sys, string, os
from tkinter import*
import time
ventana=Tk()
w=ventana.winfo_screenwidth()
h=ventana.winfo_screenheight()
ventana.geometry("%dx%d+0+0"%(w,h))
ventana.title("GUAMAN POMA DE AYALA")
imagen=PhotoImage(file="gpa.png")
fondo=Label(ventana,image=imagen).place(x=0,y=0)
ventana.after(5000, lambda: ventana.destroy()) # Destroy the widget after 30 seconds
ventana.mainloop()
command  = r"C:\OSGeo4W64\bin\qgis-bin.exe"
os.system(command)

