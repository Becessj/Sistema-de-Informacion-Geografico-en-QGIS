selectionList = ['2020-01', '2020-02', '2020-03', '2020-04']
text = QInputDialog.getItem(None, 'Ingrese Periodo', 'Selecciona periodo:', selectionList, current=0, editable=False)
if text[1]:
    username = text[0]
    name = 'Lecturas'
    layer = QgsProject.instance().mapLayersByName( name )[0]
    layer.setSubsetString("PERIODO LIKE '"+username+"%'")
    