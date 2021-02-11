agno = QInputDialog.getText(None, 'INGRESE AÑO', 'Introduce año que quieras visualizar')
mes = QInputDialog.getText(None, 'INGRESE MES', 'Introduce mes que quieras visualizar')
agno= agno [0]
mes= mes [0]
name = 'Lecturas'
layer = QgsProject.instance().mapLayersByName( name )[0]
layer.setSubsetString('agno = '+ agno +' AND '+ ' mes='+mes)

#AGNO =2020  AND  "mes" = 7

lyr = iface.activeLayer()
mj1=[]
features = lyr.getFeatures()
for feat in features:
    attrs = feat.attributes()
    mj=attrs[6]
    print(mj)