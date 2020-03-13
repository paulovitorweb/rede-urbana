""" Script desenvolvido para carregar dados de uma api 
com resposta json em geojson para usar no QGIS """


from qgis.core import QgsVectorLayer
from urllib.request import urlopen
import json

"""
@url: url da api
@path: diretório para armazenar a resposta convertida em geojson (sem a barra final)
@archive: nome do arquivo (sem extensão)
"""

# Definição das variáveis
url = ""
path = ""
archive = ""

# Leitura dos dados da api
response = urlopen(url)
data = json.loads(response.read())

# Conversão em formato geojson
geojson = {
  "type": "FeatureCollection",
  "features": [{
      "type": "Feature",
      "properties": {
        "id": registro['id'],
        "nome": registro['nome']
      },
      "geometry": ""
    } for registro in data]
}

# Armazenamento em arquivo
with open("{}/{}.geojson".format(path, archive), 'w', encoding='utf-8') as outfile:
    json.dump(geojson, outfile)

# Adição do arquivo ao projeto no QGIS
vlayer = iface.addVectorLayer(path, "api", "ogr")

# Teste do resultado
if not vlayer:
  print ("Ocorreu um erro ao carregar o json.")
else:
  print ("Json salvo em {} com o nome {} e carregado com sucesso."
          .format(path, archive))
