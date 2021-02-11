layers = QgsProject.instance().mapLayersByName('Lecturas por Predios') 
layer = layers[0]
it = layer.getFeatures()
layer.startEditing()
for feat in it:
    layer.changeAttributeValue(feat.id(), 6, '2020-07')
layer.commitChanges()