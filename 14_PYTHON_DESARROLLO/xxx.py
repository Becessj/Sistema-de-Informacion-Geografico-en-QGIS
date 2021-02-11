name = 'Lecturas'
lyr = QgsProject.instance().mapLayersByName( name )[0]
if lyr.name()=="Lecturas":
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
   # periodos.pop()
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
else:
    name = 'Lecturas por Predios'
    lyr = QgsProject.instance().mapLayersByName( name )[0]
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
        name = 'Lecturas'
        layer = QgsProject.instance().mapLayersByName( name )[0]
        layer.setSubsetString("PERIODO LIKE '"+periodoUsuario+"%'"+ 'OR PERIODO is null')
        iface.messageBar().pushMessage("Seleccionaste",'periodo '+periodoUsuario,level=3)
    else:
        iface.messageBar().pushMessage("ERROR","No seleccionaste ningun periodo",level=2)