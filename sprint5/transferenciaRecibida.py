#Classic puede recibir mas de 150.000
#Gold puede recibir mas de 500.000
#Black puede recibir cualquier cantidad

from cliente import NuevoCliente
import eventos
from modulos.razon import Razon

def conseguirItems(archivo, padre,num,hijo):
    return archivo.get(padre)[num][hijo]
    
t_classic = eventos.transacciones_classic
t_black = eventos.transacciones_black
t_gold = eventos.transacciones_gold

class RazonTransferenciaRecibida(Razon):
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
            if(conseguirItems(archivo,'transacciones',i,'tipo')=='TRANSFERENCIA_RECIBIDA' and tipo =='CLASSIC'):
                if(conseguirItems(archivo, 'transacciones',i,'estado')== 'RECHAZADA'):
                        if(conseguirItems(archivo,'transacciones',i,'monto')>NuevoCliente.getDatosClassic()['limite_transferencia_recibida']):
                            respuesta = print('Los clientes Classic no pueden recibir mas de $150.000')

            #Gold
            elif(conseguirItems(archivo,'transacciones',i,'tipo')=='TRANSFERENCIA_RECIBIDA' and tipo =='GOLD'):
                if(conseguirItems(archivo, 'transacciones',i,'estado')== 'RECHAZADA'):
                        if(conseguirItems(archivo,'transacciones',i,'monto')>NuevoCliente.getDatosGold()['limite_transferencia_recibida']):
                            respuesta = print('Los clientes Gold no pueden recibir mas de $500.000')

            #Black no tiene limite
        return respuesta

#este print devuelve del JSON el alta de las transferencias recibidas, si le pasan gold lee el archivo gold, si le pasan classic lo mismo, etc.