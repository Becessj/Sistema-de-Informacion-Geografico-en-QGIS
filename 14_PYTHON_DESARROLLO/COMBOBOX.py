from PyQt5.QtGui import *
cb = QComboBox()
cb.setWindowTitle ( 'INGRESE PERIODO' )
cb.addItems(["2020-01", "2020-02", "2020-03", "2020-07"])
cb.resize(280,50)
cb.show()
periodo = cb.currentText()
name = 'Lecturas'
layer = QgsProject.instance().mapLayersByName( name )[0]
layer.setSubsetString('PERIODO='+ 'periodo')