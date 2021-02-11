from PyQt5 import QtGui
from qgis.utils import iface
from PyQt5 import QtGui
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import*
from PyQt5.QtCore import*
from qgis.core import Qgis
from qgis.gui import QgsMapLayerComboBox
from qgis.gui import QgsFieldComboBox
from qgis.core import*
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QInputDialog
from qgis.core import QgsProject
import os
from PyQt5.QtWidgets import QMessageBox
from qgis.core import QgsProject
from datetime import datetime
import webbrowser
from qgis.PyQt.QtGui import QIcon
import os
import subprocess
import sys, os
#Este mensaje se ejecuta al iniciar el QGIS, para evidenciar la ejecución del startup
#iface.messageBar().pushMessage("ADVERTENCIA", "La informacion que contiene este proyecto es confidencial", duration=0)
icon = QIcon(r"C:/Users/rubencito/Desktop/GIS_CALCA/file.png")
iface.mainWindow().setWindowIcon(icon)
iface.mainWindow().setWindowTitle("GUAMAN POMA DE AYALA")


#subprocess.Popen("D:\GIS_GPA\QGIS_ini_GPA.exe", shell=True)
#subprocess.Popen(['D:\GIS_GPA\QGIS_ini_GPA.exe', 'option'])
#subprocess.call (["D:\GIS_GPA\QGIS_ini_GPA.exe"], shell = True)
#subprocess.call(['D:/GIS_GPA/QGIS_ini_GPA.exe'])

#os.startfile("D:\GIS_GPA\QGIS_ini_GPA.exe")
#subprocess.Popen(['D:/GIS_GPA/QGIS_ini_GPA.exe', 'https://es.stackoverflow.com/', '-new-tab'])


#os.system(r"D:/GIS_GPA/QGIS_ini_GPA.exe")


import sys, string, os
os.chdir('D:\\GIS_GPA')
os.system('"D:\GIS_GPA\QGIS_ini_GPA.exe"')





icon = 'question.svg'
data_dir = os.path.join(os.path.expanduser('~'), 'D:/GIS_GPA/svg/')
icon_path = os.path.join(data_dir, icon)
#QMessageBox.information(iface.mainWindow(), "AVISO", 'La informacion que contiene este proyecto es confidencial ' )
def select_layer_fields(vlayer):
    wcbF.setLayer(vlayer)
    field = wcbF.setLayer(vlayer)
    
def boton():    
    layer=None
    for lyr in QgsProject.instance().mapLayers().values():
        if lyr.name() == "Predios sin registro":
            layer = iface.setActiveLayer(lyr)
            #iface.messageBar().pushMessage("", 'La capa activa es ' + lyr.name(),duration=10)
            iface.actionIdentify().trigger()
            break
        if lyr.name() == "Predios sin Construccion":
            layer = iface.setActiveLayer(lyr)
            #iface.messageBar().pushMessage("", 'La capa activa es ' + lyr.name(),duration=10)
            iface.actionIdentify().trigger()
            break
        if lyr.name() == "Predios por Pisos (Individual)":
            layer = iface.setActiveLayer(lyr)
            #iface.messageBar().pushMessage("", 'La capa activa es ' + lyr.name(),duration=10)
            iface.actionIdentify().trigger()
            break
        if lyr.name() == "Predios por pisos (intervalo)":
            layer = iface.setActiveLayer(lyr)
            #iface.messageBar().pushMessage("", 'La capa activa es ' + lyr.name(),duration=10)
            iface.actionIdentify().trigger()
            break
        if lyr.name() == "Predios por Estado de Conservacion":
            layer = iface.setActiveLayer(lyr)
            #iface.messageBar().pushMessage("", 'La capa activa es ' + lyr.name(),duration=10)
            iface.actionIdentify().trigger()
            break
        if lyr.name() == "Predios Por Clasificacion":
            layer = iface.setActiveLayer(lyr)
            #iface.messageBar().pushMessage("", 'La capa activa es ' + lyr.name(),duration=10)
            iface.actionIdentify().trigger()
            break
        if lyr.name() == "Contribuyentes exonerados":
            layer = iface.setActiveLayer(lyr)
            #iface.messageBar().pushMessage("", 'La capa activa es ' + lyr.name(),duration=10)
            iface.actionIdentify().trigger()
            break
        if lyr.name() == "Contribuyentes exonerados":
            layer = iface.setActiveLayer(lyr)
            #iface.messageBar().pushMessage("", 'La capa activa es ' + lyr.name(),duration=10)
            iface.actionIdentify().trigger()
            break
        if lyr.name() == "Contribuyentes con deudas":
            layer = iface.setActiveLayer(lyr)
            #iface.messageBar().pushMessage("", 'La capa activa es ' + lyr.name(),duration=10)
            iface.actionIdentify().trigger()
            break
        #--------------
        if lyr.name() == "Tipo de Conexion":
            layer = iface.setActiveLayer(lyr)
            #iface.messageBar().pushMessage("", 'La capa activa es ' + lyr.name(),duration=10)
            iface.actionIdentify().trigger()
        if lyr.name() == "Contribuyentes por deuda":
            layer = iface.setActiveLayer(lyr)
            #iface.messageBar().pushMessage("", 'La capa activa es ' + lyr.name(),duration=10)
            iface.actionIdentify().trigger()
            break
        if lyr.name() == "Predios por el tipo de tarifa":
            layer = iface.setActiveLayer(lyr)
            #iface.messageBar().pushMessage("", 'La capa activa es ' + lyr.name(),duration=10)
            iface.actionIdentify().trigger()
            break
        if lyr.name() == "Contribuyentes con deuda":
            layer = iface.setActiveLayer(lyr)
            #iface.messageBar().pushMessage("", 'La capa activa es ' + lyr.name(),duration=10)
            iface.actionIdentify().trigger()
            break
        if lyr.name() == "Predios Conexion":
            layer = iface.setActiveLayer(lyr)
            #iface.messageBar().pushMessage("", 'La capa activa es ' + lyr.name(),duration=10)
            iface.actionIdentify().trigger()
            break
        if lyr.name() == "Situacion Actual":
            layer = iface.setActiveLayer(lyr)
            #iface.messageBar().pushMessage("", 'La capa activa es ' + lyr.name(), duration=10)
            iface.actionIdentify().trigger()
            break
        if lyr.name() == "INCIDENCIAS":
            layer = iface.setActiveLayer(lyr)
            #iface.messageBar().pushMessage("", 'La capa activa es ' + lyr.name(), duration=10)
            iface.actionIdentify().trigger()
            break
        if lyr.name() == "Medidor_S_N":
            layer = iface.setActiveLayer(lyr)
            #iface.messageBar().pushMessage("", 'La capa activa es ' + lyr.name(), duration=10)
            iface.actionIdentify().trigger()
            break
        if lyr.name() == "Ultima Lectura":
            layer = iface.setActiveLayer(lyr)
            #iface.messageBar().pushMessage("", 'La capa activa es ' + lyr.name(), duration=10)
            iface.actionIdentify().trigger()
            break
        if lyr.name() == "Lecturas":
            layer = iface.setActiveLayer(lyr)
            #iface.messageBar().pushMessage("", 'La capa activa es ' + lyr.name(), duration=10)
            iface.actionIdentify().trigger()
            break
        if lyr.name() == "LOTE_EDICION":
            layer = iface.setActiveLayer(lyr)
            #iface.messageBar().pushMessage("", 'La capa activa es ' + lyr.name(), duration=10)
            iface.actionIdentify().trigger()
            break
        if lyr.name() == "LOTE EDICION":
            layer = iface.setActiveLayer(lyr)
            #iface.messageBar().pushMessage("", 'La capa activa es ' + lyr.name(), duration=10)
            iface.actionIdentify().trigger()
            break
        if lyr.name() == "MANZANA EDICION":
            layer = iface.setActiveLayer(lyr)
            #iface.messageBar().pushMessage("", 'La capa activa es ' + lyr.name(), duration=10)
            iface.actionIdentify().trigger()
            break
        if lyr.name() == "SECTOR EDICION":
            layer = iface.setActiveLayer(lyr)
            #iface.messageBar().pushMessage("", 'La capa activa es ' + lyr.name(), duration=10)
            iface.actionIdentify().trigger()
            break
        if lyr.name() == "VIAS EDICION":
            layer = iface.setActiveLayer(lyr)
            #iface.messageBar().pushMessage("", 'La capa activa es ' + lyr.name(), duration=10)
            iface.actionIdentify().trigger()
            break
        if lyr.name() == "LECTURAS":
            layer = iface.setActiveLayer(lyr)
            #iface.messageBar().pushMessage("", 'La capa activa es ' + lyr.name(), duration=10)
            iface.actionIdentify().trigger()
            break
        if lyr.name() == "Lecturas por Predios":
            layer = iface.setActiveLayer(lyr)
            #iface.messageBar().pushMessage("", 'La capa activa es ' + lyr.name(), duration=10)
            iface.actionIdentify().trigger()
            break
        #------
        if lyr.name() == "Limpieza Registrados":
            layer = iface.setActiveLayer(lyr)
            #iface.messageBar().pushMessage("", 'La capa activa es ' + lyr.name(), duration=10)
            iface.actionIdentify().trigger()
            break
        if lyr.name() == "Por Deuda Limpieza":
            layer = iface.setActiveLayer(lyr)
            #iface.messageBar().pushMessage("", 'La capa activa es ' + lyr.name(), duration=10)
            iface.actionIdentify().trigger()
            break
        if lyr.name() == "Limpieza Deuda":
            layer = iface.setActiveLayer(lyr)
            #iface.messageBar().pushMessage("", 'La capa activa es ' + lyr.name(), duration=10)
            iface.actionIdentify().trigger()
            break
        if lyr.name() == "Limpieza Tarifa":
            layer = iface.setActiveLayer(lyr)
            #iface.messageBar().pushMessage("", 'La capa activa es ' + lyr.name(), duration=10)
            iface.actionIdentify().trigger()
            break
        if lyr.name() == "Exonerados":
            layer = iface.setActiveLayer(lyr)
            #iface.messageBar().pushMessage("", 'La capa activa es ' + lyr.name(), duration=10)
            iface.actionIdentify().trigger()
            break
        if lyr.name() == "Zona":
            layer = iface.setActiveLayer(lyr)
            #iface.messageBar().pushMessage("", 'La capa activa es ' + lyr.name(), duration=10)
            iface.actionIdentify().trigger()
            break
       
action1 = QAction('Informacion de la capa principal')
action1.triggered.connect(boton)
action1.setIcon(QIcon(icon_path))
iface.addToolBarIcon(action1)


icon1 = 'metro.svg'
data_dir1 = os.path.join(os.path.expanduser('~'), 'D:/GIS_GPA/svg/')
icon_path1 = os.path.join(data_dir1, icon1)



def show_time():
    #now = datetime.now()
    #current_time = now.strftime("%H:%M:%S")
    #iface.messageBar().pushMessage('LA HORA ES {}'.format(current_time))
    layer=None
    for lyr in QgsProject.instance().mapLayers().values():
        if lyr.name() == "Lecturas por Predios":
            layer = iface.setActiveLayer(lyr)
            lyr.setSubsetString("")
            features = lyr.getFeatures()
            mj=[]
            mj2=[]
            for feat in features:
                attrs = feat.attributes()
                mj2=mj.append(attrs[6])
                #list(set(mj2))
                #print(mj)
            periodos=sorted(list(set(mj)),reverse=True)
            periodos.pop()
            #selectionList = ['2019-08', '2020-02', '2020-03', '2020-04', '2020-05', '2020-06', '2020-07', '2020-08', '2020-09', '2020-10', '2020-11', '2020-12']
            text = QInputDialog.getItem(None, 'Periodo', 'Selecciona periodo:', periodos, current=0, editable=False)
            if text[1]:
                periodoUsuario = text[0]
                name = 'Lecturas por Predios'
                layer = QgsProject.instance().mapLayersByName( name )[0]
                layer.setSubsetString("PERIODO LIKE '"+periodoUsuario+"%'"+ 'OR PERIODO is null')
                iface.messageBar().pushMessage("Seleccionaste",'periodo '+periodoUsuario,level=3)
            else:
                iface.messageBar().pushMessage("ERROR","No seleccionaste ningun periodo",level=2)
            break
            
        if lyr.name() == "Lecturas":
            layer = iface.setActiveLayer(lyr)
            lyr.setSubsetString("")
            features = lyr.getFeatures()
            mj=[]
            mj2=[]
            for feat in features:
                attrs = feat.attributes()
                mj2=mj.append(attrs[6])
                #list(set(mj2))
                #print(mj)
            periodos=sorted(list(set(mj)),reverse=True)
            #periodos.pop()
                #selectionList = ['2019-08', '2020-02', '2020-03', '2020-04', '2020-05', '2020-06', '2020-07', '2020-08', '2020-09', '2020-10', '2020-11', '2020-12']
            text = QInputDialog.getItem(None, 'Periodo', 'Selecciona periodo:', periodos, current=0, editable=False)
            if text[1]:
                periodoUsuario = text[0]
                name = 'Lecturas'
                layer = QgsProject.instance().mapLayersByName( name )[0]
                layer.setSubsetString("PERIODO LIKE '"+periodoUsuario+"%'"+ 'OR PERIODO is null')
                iface.messageBar().pushMessage("Seleccionaste",'periodo '+periodoUsuario,level=3)
            else:
                iface.messageBar().pushMessage("ERROR","No seleccionaste ningun periodo",level=2)            

            break

action = QAction('FILTRO')
action.triggered.connect(show_time)
action.setIcon(QIcon(icon_path1))
iface.addToolBarIcon(action)
#MENU PARA RENTAS ABRIR 1-9
def abrir1():
    project1 = QgsProject.instance()
    project1.read('D://GIS_GPA//RENTAS//PREDIOS_REGISTRADOS.qgs')

def abrir2():
    project2 = QgsProject.instance()
    project2.read('D://GIS_GPA//RENTAS//PREDIOS_SINCONSTRUCCION.qgs')
def abrir3():
    project3 = QgsProject.instance()
    project3.read('D://GIS_GPA//RENTAS//PREDIOS_POR_PISO.qgs')
def abrir4():
    project4 = QgsProject.instance()
    project4.read('D://GIS_GPA//RENTAS//PREDIOS_POR_PISO_PORINTERVALOS.qgs')
def abrir5():
    project5 = QgsProject.instance()
    project5.read('D://GIS_GPA//RENTAS//PREDIOS_POR_ESTADO_CONSERVACION.qgs')
def abrir6():
    project6 = QgsProject.instance()
    project6.read('D://GIS_GPA//RENTAS//DIFERENCIA_AREA.qgs')
def abrir7():
    project7 = QgsProject.instance()
    project7.read('D://GIS_GPA//RENTAS//PREDIO_CLASIFICACION.qgs')
def abrir8():
    project8 = QgsProject.instance()
    project8.read('D://GIS_GPA//RENTAS//PREDIOS_EXONERADOS.qgs')
def abrir9():
    project9 = QgsProject.instance()
    project9.read('D://GIS_GPA//RENTAS//CONTRIBUYENTES_CON_DEUDA.qgs')
def abrir10():
    project10 = QgsProject.instance()
    project10.read('D://GIS_GPA//RENTAS//INCIDENCIAS_RENTAS.qgs')



def open_gpa():
    webbrowser.open('http://guamanpoma.org/')
menu1 = QMenu( "IR A G.P.A", iface.mainWindow().menuBar() )
gis_se_action = QAction('IR A GUAMAN POMA DE AYALA')
iface.helpMenu().addAction(gis_se_action)
gis_se_action.triggered.connect(open_gpa)
# menu rentas en la barra principal
menu = QMenu( "RENTAS", iface.mainWindow().menuBar() )
actions = iface.mainWindow().menuBar().actions()
lastAction = actions[-1]
iface.mainWindow().menuBar().insertMenu( lastAction,menu)


actionSubMenu1 = QAction('PREDIOS SIN REGISTRAR', iface.mainWindow())
menu.addAction(actionSubMenu1)
actionSubMenu1.triggered.connect(abrir1)

actionSubMenu2 = QAction('PREDIOS SIN CONSTRUCCION', iface.mainWindow())
menu.addAction(actionSubMenu2)
actionSubMenu2.triggered.connect(abrir2)


actionSubMenu3 = QAction('PREDIOS POR PISO(INDIVIDUAL)', iface.mainWindow())
menu.addAction(actionSubMenu3)
actionSubMenu3.triggered.connect(abrir3)


actionSubMenu4 = QAction('PREDIOS POR PISO(INTERVALO)', iface.mainWindow())
menu.addAction(actionSubMenu4)
actionSubMenu4.triggered.connect(abrir4)

actionSubMenu5 = QAction('PREDIOS POR ESTADO DE CONSERVACION', iface.mainWindow())
menu.addAction(actionSubMenu5)
actionSubMenu5.triggered.connect(abrir5)

actionSubMenu6 = QAction('PREDIOS POR DIFERENCIA DE AREAS', iface.mainWindow())
menu.addAction(actionSubMenu6)
actionSubMenu6.triggered.connect(abrir6)


actionSubMenu7 = QAction('PREDIOS POR CLASIFICACION', iface.mainWindow())
menu.addAction(actionSubMenu7)
actionSubMenu7.triggered.connect(abrir7)

actionSubMenu8 = QAction('PREDIOS EXONERADOS', iface.mainWindow())
menu.addAction(actionSubMenu8)
actionSubMenu8.triggered.connect(abrir8)

actionSubMenu9 = QAction('PREDIOS CON DEUDAS', iface.mainWindow())
menu.addAction(actionSubMenu9)
actionSubMenu9.triggered.connect(abrir9)

actionSubMenu10 = QAction('INCIDENCIAS', iface.mainWindow())
menu.addAction(actionSubMenu10)
actionSubMenu10.triggered.connect(abrir10)

# menu agua en la barra principal

menu2 = QMenu( "AGUA", iface.mainWindow().menuBar() )
actions = iface.mainWindow().menuBar().actions()
lastAction = actions[-1]
iface.mainWindow().menuBar().insertMenu( lastAction,menu2)


#MENU PARA AGUA open 1-5


#iface.messageBar().pushMessage("ADVERTENCIA", "COMUNIQUESE CON EL PERSONAL DE GUAMAN POMA DE AYALA PARA LA ACTIVACION DE ESTE MENÚ", duration=0)
 
def open1():
    p2 = QgsProject.instance()
    p2.read('D://GIS_GPA//AGUA//Predios_con_Conexion.qgs')
def open2():
    p2= QgsProject.instance()
    p2.read('D://GIS_GPA//AGUA//Predios_por_deuda.qgs')
def open3():
    p3 = QgsProject.instance()
    p3.read('D://GIS_GPA//AGUA//Predios_por_tipo_de_tarifa.qgs')
def open4():
    p4 = QgsProject.instance()
    p4.read('D://GIS_GPA//AGUA//Predios_con_deuda.qgs')
def open5():
    p5 = QgsProject.instance()
    p5.read('D://GIS_GPA//AGUA//Tipo_conexion.qgs') 
def open6():
    p6 = QgsProject.instance()
    p6.read('D://GIS_GPA//AGUA//Situacion_actual.qgs')
def open7():
    p7 = QgsProject.instance()
    p7.read('D://GIS_GPA//AGUA//INCIDENCIAS_AGUA.qgs')
def open8():
    p8 = QgsProject.instance()
    p8.read('D://GIS_GPA//AGUA//Ultima_Lectura_Predio.qgs')
    name = 'Lecturas por Predios'
    lyr = QgsProject.instance().mapLayersByName( name )[0]
    features = lyr.getFeatures()
    mj=[]
    mj2=[]
    for feat in features:
        attrs = feat.attributes()
        mj2=mj.append(attrs[6])
        #list(set(mj2))
        #print(mj)
    periodos=sorted(list(set(mj)),reverse=True)
    periodos.pop()
    #selectionList = ['2019-08', '2020-02', '2020-03', '2020-04', '2020-05', '2020-06', '2020-07', '2020-08', '2020-09', '2020-10', '2020-11', '2020-12']
    text = QInputDialog.getItem(None, 'Periodo', 'Selecciona periodo', periodos, current=0, editable=False)
    if text[1]:
        periodoUsuario = text[0]
        name = 'Lecturas por Predios'
        layer = QgsProject.instance().mapLayersByName( name )[0]
        layer.setSubsetString("PERIODO LIKE '"+periodoUsuario+"%'"+ 'OR PERIODO is null')
        iface.messageBar().pushMessage("Seleccionaste",'periodo '+periodoUsuario,level=3)
    else:
        iface.messageBar().pushMessage("ERROR","No seleccionaste ningun periodo",level=2)
    
def open9():
    p9 = QgsProject.instance()
    p9.read('D://GIS_GPA//AGUA//Medidor_S_N.qgs')
def open10():
    p10 = QgsProject.instance()
    p10.read('D://GIS_GPA//AGUA//Lecturas.qgs')
    name = 'Lecturas'
    lyr = QgsProject.instance().mapLayersByName( name )[0]
    features = lyr.getFeatures()
    mj=[]
    mj2=[]
    for feat in features:
        attrs = feat.attributes()
        mj2=mj.append(attrs[6])
        #list(set(mj2))
        #print(mj)
    periodos=sorted(list(set(mj)),reverse=True)
    #periodos.pop()
    #selectionList = ['2019-08', '2020-02', '2020-03', '2020-04', '2020-05', '2020-06', '2020-07', '2020-08', '2020-09', '2020-10', '2020-11', '2020-12']
    text = QInputDialog.getItem(None, 'Periodo', 'Selecciona periodo:', periodos, current=0, editable=False)
    if text[1]:
        periodoUsuario = text[0]
        name = 'Lecturas'
        layer = QgsProject.instance().mapLayersByName( name )[0]
        layer.setSubsetString("PERIODO LIKE '"+periodoUsuario+"%'")
        iface.messageBar().pushMessage("Seleccionaste",'el periodo '+periodoUsuario,level=3)
    else:
        iface.messageBar().pushMessage("ERROR","No seleccionaste ningun periodo",level=2)

       

        
actSubMenu1 = QAction('PREDIOS CON CONEXION', iface.mainWindow())
menu2.addAction(actSubMenu1)
actSubMenu1.triggered.connect(open1)

actSubMenu2 = QAction('PREDIOS POR DEUDA', iface.mainWindow())
menu2.addAction(actSubMenu2)
actSubMenu2.triggered.connect(open2)

actSubMenu4 = QAction('PREDIOS CON DEUDAS', iface.mainWindow())
menu2.addAction(actSubMenu4)
actSubMenu4.triggered.connect(open4)


actSubMenu3 = QAction('PREDIOS POR TIPO DE TARIFA', iface.mainWindow())
menu2.addAction(actSubMenu3)
actSubMenu3.triggered.connect(open3)


actSubMenu5 = QAction('TIPO DE CONEXION', iface.mainWindow())
menu2.addAction(actSubMenu5)
actSubMenu5.triggered.connect(open5)

actSubMenu6 = QAction('SITUACION ACTUAL', iface.mainWindow())
menu2.addAction(actSubMenu6)
actSubMenu6.triggered.connect(open6)

actSubMenu9 = QAction('PREDIOS CON/SIN MEDIDOR', iface.mainWindow())
menu2.addAction(actSubMenu9)
actSubMenu9.triggered.connect(open9)

actSubMenu8 = QAction('LECTURAS POR PREDIO', iface.mainWindow())
menu2.addAction(actSubMenu8)
actSubMenu8.triggered.connect(open8)

actSubMenu10 = QAction('LECTURAS POR GPS', iface.mainWindow())
menu2.addAction(actSubMenu10)
actSubMenu10.triggered.connect(open10)


actSubMenu7 = QAction('INCIDENCIAS', iface.mainWindow())
menu2.addAction(actSubMenu7)
actSubMenu7.triggered.connect(open7)



# menu limpieza en la barra principal

menu3 = QMenu( "LIMPIEZA", iface.mainWindow().menuBar() )
actions = iface.mainWindow().menuBar().actions()
lastAction = actions[-1]
iface.mainWindow().menuBar().insertMenu( lastAction,menu3)

 
def o1():
    s1 = QgsProject.instance()
    s1.read('D://GIS_GPA//LIMPIEZA//Exonerados_Limpieza.qgs')
def o2():
    s2 = QgsProject.instance()
    s2.read('D://GIS_GPA//LIMPIEZA//PorZona_Limpieza.qgs')
def o3():
    s3 = QgsProject.instance()
    s3.read('D://GIS_GPA//LIMPIEZA//Registrados_Limpieza.qgs')
def o4():
    s4 = QgsProject.instance()
    s4.read('D://GIS_GPA//LIMPIEZA//Deuda_S_N_Limpieza.qgs')  
def o5():
    s5 = QgsProject.instance()
    s5.read('D://GIS_GPA//LIMPIEZA//Tipo_de_Tarifa_Limpieza.qgs')
def o6():
    s6 = QgsProject.instance()
    s6.read('D://GIS_GPA//LIMPIEZA//Por_Deuda_Limpieza.qgs')


SubMenu1 = QAction('PREDIOS REGISTRADOS', iface.mainWindow())
menu3.addAction(SubMenu1)
SubMenu1.triggered.connect(o3)

SubMenu2 = QAction('PREDIOS POR DEUDA', iface.mainWindow())
menu3.addAction(SubMenu2)
SubMenu2.triggered.connect(o6)

SubMenu3 = QAction('PREDIOS CON DEUDA', iface.mainWindow())
menu3.addAction(SubMenu3)
SubMenu3.triggered.connect(o4)


SubMenu4 = QAction('PREDIOS POR TIPO DE TARIFA', iface.mainWindow())
menu3.addAction(SubMenu4)
SubMenu4.triggered.connect(o5)

SubMenu5 = QAction('PREDIOS EXONERADOS', iface.mainWindow())
menu3.addAction(SubMenu5)
SubMenu5.triggered.connect(o1)

SubMenu6 = QAction('PREDIOS POR ZONA', iface.mainWindow())
menu3.addAction(SubMenu6)
SubMenu6.triggered.connect(o2)
