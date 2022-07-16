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

#Cliente Classic con sus datos personales y su historial de transacciones
def clienteClassic():
    print('---Datos del cliente---')
    print('Nombre: ' , transacciones_classic.get('nombre'))
    print('Numero: ' , transacciones_classic.get('numero'))
    print('Dni: ' , transacciones_classic.get('dni'))
    print('Direccion: ', transacciones_classic.get('direccion')['ciudad'],',' ,transacciones_classic.get('direccion')['calle'],transacciones_classic.get('direccion')['numero'])
    print('Tipo de cuenta: ' , transacciones_classic.get('tipo'))
    print('')
    print('-----Transacciones-----')
    contador=0
    while contador<10:
        print('Transaccion',contador+1)
        print('Tipo de transaccion: ',transacciones_classic.get('transacciones')[contador]['tipo'])
        print('Monto: ',transacciones_classic.get('transacciones')[contador]['monto'])
        print('Fecha: ',transacciones_classic.get('transacciones')[contador]['fecha'])
        print('Estado: ',transacciones_classic.get('transacciones')[contador]['estado'])
        print('')
        contador+=1
    #print('Razon: ',transacciones_classic.get('transacciones')[0]['estado'])


#Cliente Gold con sus datos personales y su historial de transacciones
def clienteGold():
    print('')
    print('---Datos del cliente---')
    print('Nombre: ' , transacciones_gold.get('nombre'))
    print('Numero: ' , transacciones_gold.get('numero'))
    print('Dni: ' , transacciones_gold.get('dni'))
    print('Direccion: ', transacciones_gold.get('direccion')['ciudad'],',' ,transacciones_gold.get('direccion')['calle'],transacciones_gold.get('direccion')['numero'])
    print('Tipo de cuenta: ' , transacciones_gold.get('tipo'))
    print('')
    print('-----Transacciones-----')
    contador=0
    while contador<10:
        print('Transaccion',contador+1)
        print('Tipo de transaccion: ',transacciones_gold.get('transacciones')[contador]['tipo'])
        print('Monto: ',transacciones_gold.get('transacciones')[contador]['monto'])
        print('Fecha: ',transacciones_gold.get('transacciones')[contador]['fecha'])
        print('Estado: ',transacciones_gold.get('transacciones')[contador]['estado'])
        print('')
        contador+=1
    #print('Razon: ',transacciones_gold.get('transacciones')[0]['estado'])


#Cliente Black con sus datos personales y su historial de transacciones
def clienteBlack():
    print('')
    print('---Datos del cliente---')
    print('Nombre: ' , transacciones_black.get('nombre'))
    print('Numero: ' , transacciones_black.get('numero'))
    print('Dni: ' , transacciones_black.get('dni'))
    print('Direccion: ', transacciones_black.get('direccion')['ciudad'],',' ,transacciones_black.get('direccion')['calle'],transacciones_black.get('direccion')['numero'])
    print('Tipo de cuenta: ' , transacciones_black.get('tipo'))
    print('')
    print('-----Transacciones-----')
    contador=0
    while contador<10:
        print('Transaccion',contador+1)
        print('Tipo de transaccion: ',transacciones_black.get('transacciones')[contador]['tipo'])
        print('Monto: ',transacciones_black.get('transacciones')[contador]['monto'])
        print('Fecha: ',transacciones_black.get('transacciones')[contador]['fecha'])
        print('Estado: ',transacciones_black.get('transacciones')[contador]['estado'])
        print('')
        contador+=1
    #print('Razon: ',transacciones_black.get('transacciones')[0]['estado'])

clienteClassic()
clienteGold()
clienteBlack()
