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
a=sorted(list(set(mj)),reverse=True)
#del(a[1])
#a.pop()
print(a)

#EL NULL DEBERÍA SER STRING o 0, LANZA ERROR EN EL INDICE 13
    
    
    
    
    
    