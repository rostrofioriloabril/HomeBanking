import json
#en este archivo pasamos archivos JSON (con datos de clientes y transacciones realizadas) a diccionarios de Python para poder utilizarlos

#cliente classic datos
with open('sprint5/eventos_classic.json', 'r') as eventos_classic:
    transacciones_classic = json.load(eventos_classic)

#cliente gold datos
with open('sprint5/eventos_gold.json', 'r') as eventos_gold:
    transacciones_gold = json.load(eventos_gold)

#cliente black datos
with open('sprint5/eventos_black.json', 'r') as eventos_black:
    transacciones_black = json.load(eventos_black)

