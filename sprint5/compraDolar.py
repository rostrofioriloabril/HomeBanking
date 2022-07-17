#Classic no tiene acceso
#Gold y Black pueden comprar

import eventos
from modulos.razon import Razon

def conseguirItems(archivo, padre,num,hijo):
    return archivo.get(padre)[num][hijo]
    
t_classic = eventos.transacciones_classic
t_black = eventos.transacciones_black
t_gold = eventos.transacciones_gold

class RazonCompraDolar(Razon):
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
            if(conseguirItems(archivo,'transacciones',i,'tipo')=='COMPRA_DOLAR' and tipo =='CLASSIC'):
                if(conseguirItems(archivo, 'transacciones',i,'estado')== 'RECHAZADA'):
                    respuesta = print('Los clientes Classic no pueden comprar dolares')

            #Gold
            elif(conseguirItems(archivo,'transacciones',i,'tipo')=='COMPRA_DOLAR' and tipo =='GOLD'):
                if(conseguirItems(archivo, 'transacciones',i,'estado')== 'RECHAZADA'):
                    respuesta = print('Cliente Gold: No puede comprar esa cantidad de dolares por fondos insuficientes')
            #Black
            elif(conseguirItems(archivo,'transacciones',i,'tipo')=='COMPRA_DOLAR' and tipo =='BLACK'):
                    if(conseguirItems(archivo, 'transacciones',i,'estado')== 'RECHAZADA'):
                        respuesta = print('Cliente Black: No puede comprar esa cantidad de dolares por fondos insuficientes')

        return respuesta

RazonCompraDolar.validar('CLASSIC')
#este print devuelve del JSON el alta de la compra de dolares, si le pasan gold lee el archivo gold, si le pasan classic lo mismo, etc.