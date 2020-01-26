def add_qtde_lotes_field(layer):
    field_name = "RU_Qtde"
    fields = layer.fields().names()
    if field_name not in fields:
        from PyQt5.QtCore import QVariant
        layer_provider = layer.dataProvider()
        layer_provider.addAttributes([QgsField(field_name, QVariant.Int)])
        layer.updateFields()
    return fields.index(field_name)

def run_qtde_lotes(metros):
    """ Calcula a quantidade de lotes que estão a 
    um raio de <metros> metros de cada lote """
    
    layer = qgis.utils.iface.activeLayer()
    index = add_qtde_lotes_field(layer)
    layer_provider = layer.dataProvider()
    # features = layer.getSelectedFeatures()
    value = []
    layer.startEditing()
    for f in layer.getSelectedFeatures():
        a = 0
        for ff in layer.getSelectedFeatures():
            # Se não for o mesmo lote e a geometria intersectar, incrementa
            if f.id() != ff.id() and f.geometry().buffer(metros, 10).intersects(ff.geometry()):
                a = a + 1
        value.append([f.id(), a])
        layer_provider.changeAttributeValues({f.id():{index: a}})
    layer.commitChanges()
    return value