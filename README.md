# Scrips PyQGIS da Rede Urbana

Este repositório reúne alguns códigos construídos pela equipe da [Rede Urbana](https://aredeurbana.com)
 para rodarem dentro do **Terminal Python integrado** do QGIS.

## run-qtde-lotes

Função que calcula a quantidade de lotes que estão a um raio de <metros> metros de cada lote, armazena em um campo da tabela de atributos e retorna uma lista com os ids dos lotes acessíveis no raio para cada lote. Opcionalmente, o usuário pode utilizar os centróides dos lotes para calcular o buffer. Por padrão, são utilizados os polígonos. É necessário selecionar os lotes. Testado no QGIS 3.4 Madeira.

### Como usar
1. Importar o código no terminal;
2. Executar `run_qtde_lotes(metros, layer, use_centroid)`, sendo **metros** um número inteiro que representa o tamanho do buffer (argumento obrigatório), **layer** uma instância da camada de lotes (argumento opcional, por padrão é a camada ativa) e **use_centroid** um valor booleano (True/False) que representa a opção de usar ou não os centróides dos lotes em vez dos polígonos.

### Exemplo
1. Calcular considerando um buffer de 500 metros, utilizando a camada ativa e as feições originais (polígonos):
`run_qtde_lotes(500)`

1. Calcular considerando um buffer de 400 metros, utilizando a camada ativa e os centróides dos lotes:
`run_qtde_lotes(500, use_centroid=True)`
