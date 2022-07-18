#Classic no tiene acceso
#Gold puede tener 1 sola tarjeta de credito
#Black puede tener hasta 5 tarjetas de credito

from cliente import NuevoCliente
import eventos
from modulos.razon import Razon

def conseguirItems(archivo, padre,num,hijo):
    return archivo.get(padre)[num][hijo]
    
t_classic = eventos.transacciones_classic
t_black = eventos.transacciones_black
t_gold = eventos.transacciones_gold

class RazonAltaTarjetaCredito(Razon):
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
            if(conseguirItems(archivo,'transacciones',i,'tipo')=='ALTA_TARJETA_CREDITO' and tipo =='CLASSIC'):
                if(conseguirItems(archivo, 'transacciones',i,'estado')== 'RECHAZADA'):
                        if(conseguirItems(archivo,'transacciones',i,'totalTarjetasDeCreditoActualmente')>=NuevoCliente.getDatosClassic()['total_tarjetas_credito']):
                            respuesta = "Los clientes Classic no pueden tener tarjetas de credito"

            #Gold
            elif(conseguirItems(archivo,'transacciones',i,'tipo')=='ALTA_TARJETA_CREDITO' and tipo =='GOLD'):
                if(conseguirItems(archivo, 'transacciones',i,'estado')== 'RECHAZADA'):
                        if(conseguirItems(archivo,'transacciones',i,'totalTarjetasDeCreditoActualmente')>=NuevoCliente.getDatosGold()['total_tarjetas_credito']):
                            respuesta = 'Los clientes Gold no pueden tener mas de 1 tarjeta de credito'

            #Black
            elif(conseguirItems(archivo,'transacciones',i,'tipo')=='ALTA_TARJETA_CREDITO' and tipo =='BLACK'):
                    if(conseguirItems(archivo, 'transacciones',i,'estado')== 'RECHAZADA'):
                        if(conseguirItems(archivo,'transacciones',i,'totalTarjetasDeCreditoActualmente')>=NuevoCliente.getDatosBlack()['total_tarjetas_credito']):
                            respuesta = "Los clientes Black no pueden tener mas de 5 tarjetas de credito"
        return respuesta

#este print devuelve del JSON el alta de las tarjetas de credito, si le pasan gold lee el archivo gold, si le pasan classic lo mismo, etc.