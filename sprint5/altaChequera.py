#Classic no tiene acceso
#Gold puede tener 1 chequera
#Black puede tener 2 chequeras

from cliente import NuevoCliente
import eventos
from modulos.razon import Razon

def conseguirItems(archivo, padre,num,hijo):
    return archivo.get(padre)[num][hijo]
    
t_classic = eventos.transacciones_classic
t_black = eventos.transacciones_black
t_gold = eventos.transacciones_gold

class RazonAltaChequera(Razon):
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
            if(conseguirItems(archivo,'transacciones',i,'tipo')=='ALTA_CHEQUERA' and tipo =='CLASSIC'):
                if(conseguirItems(archivo, 'transacciones',i,'estado')== 'RECHAZADA'):
                        if(conseguirItems(archivo,'transacciones',i,'totalChequerasActualmente')>=NuevoCliente.getDatosClassic()['total_chequeras']):
                            respuesta = print('Los clientes Classic no pueden tener chequeras')

            #Gold
            elif(conseguirItems(archivo,'transacciones',i,'tipo')=='ALTA_CHEQUERA' and tipo =='GOLD'):
                if(conseguirItems(archivo, 'transacciones',i,'estado')== 'RECHAZADA'):
                        if(conseguirItems(archivo,'transacciones',i,'totalChequerasActualmente')>=NuevoCliente.getDatosGold()['total_chequeras']):
                            respuesta = print('Los clientes Gold no pueden tener mas de 1 chequeras')

            #Black
            elif(conseguirItems(archivo,'transacciones',i,'tipo')=='ALTA_CHEQUERA' and tipo =='BLACK'):
                    if(conseguirItems(archivo, 'transacciones',i,'estado')== 'RECHAZADA'):
                        if(conseguirItems(archivo,'transacciones',i,'totalChequerasActualmente')>=NuevoCliente.getDatosBlack()['total_chequeras']):
                            respuesta = print('Los clientes Black no pueden tener mas de 2 chequeras')
        return respuesta

RazonAltaChequera.validar('CLASSIC')
#este print devuelve del JSON el alta de las chequeras, si le pasan gold lee el archivo gold, si le pasan classic lo mismo, etc.