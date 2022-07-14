import json
#en este archivo pasamos archivos JSON (con datos de clientes y transacciones realizadas) a diccionarios de Python para poder utilizarlos

#cliente classic datos
with open('eventos_classic.json', 'r') as eventos_classic:
    transacciones_classic = json.load(eventos_classic)
    print('listo')

print(transacciones_classic)

#cliente gold datos
with open('eventos_gold.json', 'r') as eventos_gold:
    transacciones_gold = json.load(eventos_gold)
    print('gold')

print(transacciones_gold)

#cliente black datos
with open('eventos_black.json', 'r') as eventos_black:
    transacciones_black = json.load(eventos_black)
    print('black')

print(transacciones_black)