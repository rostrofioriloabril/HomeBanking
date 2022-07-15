import json
#en este archivo pasamos archivos JSON (con datos de clientes y transacciones realizadas) a diccionarios de Python para poder utilizarlos

#cliente classic datos
with open('eventos_classic.json', 'r') as eventos_classic:
    transacciones_classic = json.load(eventos_classic)
    # print('listo')

# print(transacciones_classic)

#cliente gold datos
with open('eventos_gold.json', 'r') as eventos_gold:
    transacciones_gold = json.load(eventos_gold)
    # print('gold')

# print(transacciones_gold)

#cliente black datos
with open('eventos_black.json', 'r') as eventos_black:
    transacciones_black = json.load(eventos_black)
    # print('black')

# print(transacciones_black)

# for item_transacciones_classic in transacciones_classic:
#     print(item_transacciones_classic)

# for item_transacciones_classic in transacciones_classic:
#     valor = transacciones_classic[item_transacciones_classic]
#     print(valor)

# elemento = transacciones_classic.items()[0]
# print(elemento)


#primer cliente
# print('nombre: ' , transacciones_classic.get('nombre'))
# print('numero: ' , transacciones_classic.get('numero'))
# print('dni: ' , transacciones_classic.get('dni'))
# print('tipo de cuenta: ' , transacciones_classic.get('tipo'))
# print(transacciones_classic.get('direccion')[:4])
# print(transacciones_classic.get('transacciones')[0])
# print(transacciones_classic.get('transacciones')[1]['estado'])

def cliente1(transacciones_classic):
    print('Nombre: ' , transacciones_classic.get('nombre'))
    print('Numero: ' , transacciones_classic.get('numero'))
    print('Dni: ' , transacciones_classic.get('dni'))
    print('Direccion: ', transacciones_classic.get('direccion')['ciudad'],',' ,transacciones_classic.get('direccion')['calle'],transacciones_classic.get('direccion')['numero'])
    print('Tipo de cuenta: ' , transacciones_classic.get('tipo'))
    print('Tipo de transaccion: ',transacciones_classic.get('transacciones')[0]['tipo'])
    print('Monto: ',transacciones_classic.get('transacciones')[0]['monto'])
    print('Fecha: ',transacciones_classic.get('transacciones')[0]['fecha'])
    print('Estado: ',transacciones_classic.get('transacciones')[0]['estado'])
    #print('Razon: ',transacciones_classic.get('transacciones')[0]['estado'])

cliente1()
