from timeit import default_timer as timer

def add_qtde_lotes_field(layer, field_name="RU_Qtde"):
    """ Adiciona campo para armazenar a informação, caso não exista, 
    e retorna o índice """
    if field_name not in layer.fields().names():
        print ("Adicionando campo {}".format(field_name))
        from PyQt5.QtCore import QVariant
        layer_provider = layer.dataProvider()
        layer_provider.addAttributes([QgsField(field_name, QVariant.Int)])
        layer.updateFields()
    return layer.fields().names().index(field_name)

def run_qtde_lotes(metros, layer=qgis.utils.iface.activeLayer(), use_centroid=False):
    """ Calcula a quantidade de lotes que estão a um raio de <metros> metros 
    de cada lote, armazena num campo da tabela de atributos e retorna uma lista """

    inicio = timer()
    field_name = "{}m".format(str(metros))
    index = add_qtde_lotes_field(layer, field_name)
    layer_provider = layer.dataProvider()
    value = []
    layer.startEditing()
    numero = len(list(layer.getSelectedFeatures()))
    print("Calculando para {} lotes{}..."
        .format(numero, " utilizando centróides" if use_centroid else " utilizando polígonos"))
    if use_centroid:
        for f in layer.getSelectedFeatures():
            a = 0
            for ff in layer.getSelectedFeatures():
                # Se não for o mesmo lote e a geometria intersectar, incrementa
                if f.id() != ff.id() and f.geometry().centroid().buffer(metros, 10).intersects(ff.geometry()):
                    a = a + 1
            value.append([f.id(), a])
            layer_provider.changeAttributeValues({f.id():{index: a}})
    else:
        for f in layer.getSelectedFeatures():
            a = 0
            for ff in layer.getSelectedFeatures():
                # Se não for o mesmo lote e a geometria intersectar, incrementa
                if f.id() != ff.id() and f.geometry().buffer(metros, 10).intersects(ff.geometry()):
                    a = a + 1
            value.append([f.id(), a])
            layer_provider.changeAttributeValues({f.id():{index: a}})
    layer.commitChanges()
    elapsed = timer() - inicio
    print("Cálculo efetuado com sucesso em {} segundos.".format(round(elapsed, 4)))
    return value