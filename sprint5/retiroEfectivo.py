from cliente import NuevoCliente
import eventos
from modulos.razon import Razon

def conseguirItems(archivo, padre,num,hijo):
    return archivo.get(padre)[num][hijo]
    
t_classic = eventos.transacciones_classic
t_black = eventos.transacciones_black
t_gold = eventos.transacciones_gold

class RazonRetiroEfectivo(Razon):
    def __init__(self, tipo):
        super().__init__(self,tipo)
        pass
    def validar(tipo):
        respuesta = ""
        if(tipo =='CLASSIC'):
            archivo = t_classic

        elif(tipo == 'GOLD'):
            archivo = t_gold
        elif(tipo == 'BLACK'):
            archivo = t_black
        else:
            print('No contamos con el servicio')

        for i in range(len(archivo.get('transacciones'))):
            #Classsic
            if(conseguirItems(archivo,'transacciones',i,'tipo')=='RETIRO_EFECTIVO_CAJERO_AUTOMATICO' and tipo =='CLASSIC'):
                if(conseguirItems(archivo, 'transacciones',i,'estado')== 'RECHAZADA'):
                        if(conseguirItems(archivo,'transacciones',i,'monto')>NuevoCliente.getDatosClassic()["limite_extraccion_diario" ]and conseguirItems(archivo,'transacciones',i,'saldoEnCuenta')>conseguirItems(archivo,'transacciones',i,'monto')):
                            respuesta = "El monto ingresado supera el límite de extraccion diaria"
                        elif(conseguirItems(archivo,'transacciones',i,'monto') > conseguirItems(archivo,'transacciones',i,'cupoDiarioRestante')):
                            respuesta = "El monto supera su cupo diario restante. Su cupo diaro ahora es de: ${}'.format(conseguirItems(archivo,'transacciones',i,'cupoDiarioRestante))"
                        elif(conseguirItems(archivo,'transacciones',i,'saldoEnCuenta')<conseguirItems(archivo,'transacciones',i,'monto') or conseguirItems(archivo,'transacciones',i,'saldoEnCuenta')- conseguirItems(archivo,'transacciones',i,'monto')<0):
                            respuesta = "El monto a retirar es mayor que el saldo de su cuenta"

            #Gold
            elif(conseguirItems(archivo,'transacciones',i,'tipo')=='RETIRO_EFECTIVO_CAJERO_AUTOMATICO' and tipo =='GOLD'):
                if(conseguirItems(archivo, 'transacciones',i,'estado')== 'RECHAZADA'):
                        if(conseguirItems(archivo,'transacciones',i,'monto')>NuevoCliente.getDatosGold()["limite_extraccion_diario"]):
                            respuesta = "El monto ingresado supera el límite de extraccion diaria"
                        elif(conseguirItems(archivo,'transacciones',i,'monto')> conseguirItems(archivo,'transacciones',i,'cupoDiarioRestante')):
                            respuesta = print('El máximo de saldo que puede retirar hoy es de: ${}'.format(conseguirItems(archivo,'transacciones',i,'cupoDiarioRestante')))
                        elif(conseguirItems(archivo,'transacciones',i,'saldoEnCuenta')<conseguirItems(archivo,'transacciones',i,'monto') or conseguirItems(archivo,'transacciones',i,'saldoEnCuenta')- conseguirItems(archivo,'transacciones',i,'monto')<0):
                            respuesta = "El monto a retirar es mayor que el saldo de su cuenta"

            #Black
            elif(conseguirItems(archivo,'transacciones',i,'tipo')=='RETIRO_EFECTIVO_CAJERO_AUTOMATICO' and tipo =='BLACK'):
                    if(conseguirItems(archivo, 'transacciones',i,'estado')== 'RECHAZADA'):
                        if(conseguirItems(archivo,'transacciones',i,'monto')>NuevoCliente.getDatosBlack()["limite_extraccion_diario"]):
                            respuesta = print('El monto ingresado supera el límite de extraccion diaria')
                        elif(conseguirItems(archivo,'transacciones',i,'monto')> conseguirItems(archivo,'transacciones',i,'cupoDiarioRestante')):
                            respuesta = "El máximo de saldo que puede retirar hoy es de: ${}".format(conseguirItems(archivo,'transacciones',i,'cupoDiarioRestante'))
                        elif(conseguirItems(archivo,'transacciones',i,'saldoEnCuenta')<conseguirItems(archivo,'transacciones',i,'monto') or conseguirItems(archivo,'transacciones',i,'saldoEnCuenta')- conseguirItems(archivo,'transacciones',i,'monto')<0):
                            respuesta = "El monto a retirar es mayor que el saldo de su cuenta"


        return respuesta

#este print devuelve del JSON las extracciones por cajero, si le pasan gold lee el archivo gold, si le pasan classic lo mismo, etc.