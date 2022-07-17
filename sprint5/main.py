import json
#en este archivo pasamos archivos JSON (con datos de clientes y transacciones realizadas) a diccionarios de Python para poder utilizarlos

import respuestas
#en este archivo estan las razones por las cuales fue rechazada la operacion

from cliente import NuevoCliente
#en este archivo estan las razones del retiro de efectivo

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
    print('Nombre: ' , transacciones_classic.get('nombre'),transacciones_black.get('apellido'))
    print('Numero: ' , transacciones_classic.get('numero'))
    print('Dni: ' , transacciones_classic.get('dni'))
    print('Direccion: ', transacciones_classic.get('direccion')['ciudad'],',' ,transacciones_classic.get('direccion')['calle'],transacciones_classic.get('direccion')['numero'])
    print('Tipo de cuenta: ' , transacciones_classic.get('tipo'))
    print('')
    print('-----Transacciones-----')
    contador=0
    while contador<9:
        print('Transaccion',contador+1)
        print('Tipo de transaccion: ',transacciones_classic.get('transacciones')[contador]['tipo'])
        print('Monto: ',transacciones_classic.get('transacciones')[contador]['monto'])
        print('Fecha: ',transacciones_classic.get('transacciones')[contador]['fecha'])
        print('Estado: ',transacciones_classic.get('transacciones')[contador]['estado'])
        if (transacciones_classic.get('transacciones')[contador]['tipo']=='RETIRO_EFECTIVO_CAJERO_AUTOMATICO'):
            if(transacciones_classic.get('transacciones')[contador]['estado']== 'RECHAZADA'):
                if(transacciones_classic.get('transacciones')[contador]['monto']>NuevoCliente.getDatosClassic()["limite_extraccion_diario" ]and transacciones_classic.get('transacciones')[contador]['saldoEnCuenta']>transacciones_classic.get('transacciones')[contador]['monto']):
                    print('El monto ingresado supera el límite de extraccion diaria')
                elif(transacciones_classic.get('transacciones')[contador]['monto'] > transacciones_classic.get('transacciones')[contador]['cupoDiarioRestante']):
                    print('El monto supera su cupo diario restante. Su cupo diaro ahora es de: $',transacciones_classic.get('transacciones')[contador]['cupoDiarioRestante'])
                elif(transacciones_classic.get('transacciones')[contador]['saldoEnCuenta']<transacciones_classic.get('transacciones')[contador]['monto'] or transacciones_classic.get('transacciones')[contador]['saldoEnCuenta']- transacciones_classic.get('transacciones')[contador]['monto']<0):
                    print('El monto a retirar es mayor que el saldo de su cuenta')
        elif (transacciones_classic.get('transacciones')[contador]['tipo']=='ALTA_TARJETA_CREDITO'):
            if(transacciones_classic.get('transacciones')[contador]['estado']== 'RECHAZADA'):
                respuestas.RazonAltaTarjetaCredito.validar('CLASSIC')
        elif (transacciones_classic.get('transacciones')[contador]['tipo']=='ALTA_CHEQUERA'):
            if(transacciones_classic.get('transacciones')[contador]['estado']== 'RECHAZADA'):
                respuestas.RazonAltaChequera.validar('CLASSIC')
        elif (transacciones_classic.get('transacciones')[contador]['tipo']=='COMPRA_DOLAR'):
            if(transacciones_classic.get('transacciones')[contador]['estado']== 'RECHAZADA'):
                respuestas.RazonCompraDolar.validar('CLASSIC')
        elif (transacciones_classic.get('transacciones')[contador]['tipo']=='TRANSFERENCIA_ENVIADA'):
            if(transacciones_classic.get('transacciones')[contador]['estado']== 'RECHAZADA'):
                respuestas.RazonTransferenciaEnviada.validar('CLASSIC')
        elif (transacciones_classic.get('transacciones')[contador]['tipo']=='TRANSFERENCIA_RECIBIDA'):
            if(transacciones_classic.get('transacciones')[contador]['estado']== 'RECHAZADA'):
                respuestas.RazonTransferenciaRecibida.validar('CLASSIC')
        print('')
        contador+=1


#Cliente Gold con sus datos personales y su historial de transacciones
def clienteGold():
    print('')
    print('---Datos del cliente---')
    print('Nombre: ' , transacciones_gold.get('nombre'),transacciones_black.get('apellido'))
    print('Numero: ' , transacciones_gold.get('numero'))
    print('Dni: ' , transacciones_gold.get('dni'))
    print('Direccion: ', transacciones_gold.get('direccion')['ciudad'],',' ,transacciones_gold.get('direccion')['calle'],transacciones_gold.get('direccion')['numero'])
    print('Tipo de cuenta: ' , transacciones_gold.get('tipo'))
    print('')
    print('-----Transacciones-----')
    contador=0
    while contador<9:
        print('Transaccion',contador+1)
        print('Tipo de transaccion: ',transacciones_gold.get('transacciones')[contador]['tipo'])
        print('Monto: ',transacciones_gold.get('transacciones')[contador]['monto'])
        print('Fecha: ',transacciones_gold.get('transacciones')[contador]['fecha'])
        print('Estado: ',transacciones_gold.get('transacciones')[contador]['estado'])
        if (transacciones_gold.get('transacciones')[contador]['tipo']=='RETIRO_EFECTIVO_CAJERO_AUTOMATICO'):
            if(transacciones_gold.get('transacciones')[contador]['estado']== 'RECHAZADA'):
                if(transacciones_gold.get('transacciones')[contador]['monto']>NuevoCliente.getDatosGold()["limite_extraccion_diario" ]and transacciones_gold.get('transacciones')[contador]['saldoEnCuenta']>transacciones_gold.get('transacciones')[contador]['monto']):
                    print('El monto ingresado supera el límite de extraccion diaria')
                elif(transacciones_gold.get('transacciones')[contador]['monto'] > transacciones_gold.get('transacciones')[contador]['cupoDiarioRestante']):
                    print('El monto supera su cupo diario restante. Su cupo diaro ahora es de: $',transacciones_gold.get('transacciones')[contador]['cupoDiarioRestante'])
                elif(transacciones_gold.get('transacciones')[contador]['saldoEnCuenta']<transacciones_gold.get('transacciones')[contador]['monto'] or transacciones_gold.get('transacciones')[contador]['saldoEnCuenta']- transacciones_gold.get('transacciones')[contador]['monto']<0):
                    print('El monto a retirar es mayor que el saldo de su cuenta')
        elif (transacciones_gold.get('transacciones')[contador]['tipo']=='ALTA_TARJETA_CREDITO'):
            if(transacciones_gold.get('transacciones')[contador]['estado']== 'RECHAZADA'):
                respuestas.RazonAltaTarjetaCredito.validar('GOLD')
        elif (transacciones_gold.get('transacciones')[contador]['tipo']=='ALTA_CHEQUERA'):
            if(transacciones_gold.get('transacciones')[contador]['estado']== 'RECHAZADA'):
                respuestas.RazonAltaChequera.validar('GOLD')
        elif (transacciones_gold.get('transacciones')[contador]['tipo']=='COMPRA_DOLAR'):
            if(transacciones_gold.get('transacciones')[contador]['estado']== 'RECHAZADA'):
                respuestas.RazonCompraDolar.validar('GOLD')
        elif (transacciones_gold.get('transacciones')[contador]['tipo']=='TRANSFERENCIA_ENVIADA'):
            if(transacciones_gold.get('transacciones')[contador]['estado']== 'RECHAZADA'):
                respuestas.RazonTransferenciaEnviada.validar('GOLD')
        elif (transacciones_gold.get('transacciones')[contador]['tipo']=='TRANSFERENCIA_RECIBIDA'):
            if(transacciones_gold.get('transacciones')[contador]['estado']== 'RECHAZADA'):
                respuestas.RazonTransferenciaRecibida.validar('GOLD')
        print('')
        contador+=1


#Cliente Black con sus datos personales y su historial de transacciones
def clienteBlack():
    print('')
    print('---Datos del cliente---')
    print('Nombre: ' , transacciones_black.get('nombre'),transacciones_black.get('apellido'))
    print('Numero: ' , transacciones_black.get('numero'))
    print('Dni: ' , transacciones_black.get('dni'))
    print('Direccion: ', transacciones_black.get('direccion')['ciudad'],',' ,transacciones_black.get('direccion')['calle'],transacciones_black.get('direccion')['numero'])
    print('Tipo de cuenta: ' , transacciones_black.get('tipo'))
    print('')
    print('-----Transacciones-----')
    contador=0
    while contador<9:
        print('Transaccion',contador+1)
        print('Tipo de operacion: ',transacciones_black.get('transacciones')[contador]['tipo'])
        print('Monto: ',transacciones_black.get('transacciones')[contador]['monto'])
        print('Fecha: ',transacciones_black.get('transacciones')[contador]['fecha'])
        print('Estado: ',transacciones_black.get('transacciones')[contador]['estado'])
        if (transacciones_black.get('transacciones')[contador]['tipo']=='RETIRO_EFECTIVO_CAJERO_AUTOMATICO'):
            if(transacciones_black.get('transacciones')[contador]['estado']== 'RECHAZADA'):
                if(transacciones_black.get('transacciones')[contador]['monto']>NuevoCliente.getDatosBlack()["limite_extraccion_diario" ]and transacciones_black.get('transacciones')[contador]['saldoEnCuenta']>transacciones_black.get('transacciones')[contador]['monto']):
                    print('El monto ingresado supera el límite de extraccion diaria')
                elif(transacciones_black.get('transacciones')[contador]['monto'] > transacciones_black.get('transacciones')[contador]['cupoDiarioRestante']):
                    print('El monto supera su cupo diario restante. Su cupo diaro ahora es de: $',transacciones_black.get('transacciones')[contador]['cupoDiarioRestante'])
                elif(transacciones_black.get('transacciones')[contador]['saldoEnCuenta']<transacciones_black.get('transacciones')[contador]['monto'] or transacciones_black.get('transacciones')[contador]['saldoEnCuenta']- transacciones_black.get('transacciones')[contador]['monto']<0):
                    print('El monto a retirar es mayor que el saldo de su cuenta')
        elif (transacciones_black.get('transacciones')[contador]['tipo']=='ALTA_TARJETA_CREDITO'):
            if(transacciones_black.get('transacciones')[contador]['estado']== 'RECHAZADA'):
                respuestas.RazonAltaTarjetaCredito.validar('BLACK')
        elif (transacciones_black.get('transacciones')[contador]['tipo']=='ALTA_CHEQUERA'):
            if(transacciones_black.get('transacciones')[contador]['estado']== 'RECHAZADA'):
                respuestas.RazonAltaChequera.validar('BLACK')
        elif (transacciones_black.get('transacciones')[contador]['tipo']=='COMPRA_DOLAR'):
            if(transacciones_black.get('transacciones')[contador]['estado']== 'RECHAZADA'):
                respuestas.RazonCompraDolar.validar('BLACK')
        elif (transacciones_black.get('transacciones')[contador]['tipo']=='TRANSFERENCIA_ENVIADA'):
            if(transacciones_black.get('transacciones')[contador]['estado']== 'RECHAZADA'):
                respuestas.RazonTransferenciaEnviada.validar('BLACK')
        print('')
        contador+=1


clienteClassic()
clienteGold()
clienteBlack()


#este archivo de momento es provisorio. Tal vez lo usemos para ordenar todo lo que hay que mostrar por HTML.
