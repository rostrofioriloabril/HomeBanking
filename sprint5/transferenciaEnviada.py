import eventos
from modulos.razon import Razon

def conseguirItems(archivo, padre,num,hijo):
    return archivo.get(padre)[num][hijo]
    
t_classic = eventos.transacciones_classic
t_black = eventos.transacciones_black
t_gold = eventos.transacciones_gold

class RazonTransferenciaEnviada(Razon):
    def __init__(self, tipo):
        super().__init__(tipo)
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
            return 'No contamos con el servicio'

        for i in range(len(archivo.get('transacciones'))):
            #Classsic
            if(conseguirItems(archivo,'transacciones',i,'tipo')=='TRANSFERENCIA_ENVIADA' and tipo =='CLASSIC'):
                if(conseguirItems(archivo, 'transacciones',i,'estado')== 'RECHAZADA'):
                    respuesta = 'Clientes Classic: Fondos insuficientes para realizar la transferencia'

            #Gold
            elif(conseguirItems(archivo,'transacciones',i,'tipo')=='TRANSFERENCIA_ENVIADA' and tipo =='GOLD'):
                if(conseguirItems(archivo, 'transacciones',i,'estado')== 'RECHAZADA'):
                    respuesta = 'Cliente Gold: Fondos insuficientes para realizar la transferencia'
            #Black
            elif(conseguirItems(archivo,'transacciones',i,'tipo')=='TRANSFERENCIA_ENVIADA' and tipo =='BLACK'):
                    if(conseguirItems(archivo, 'transacciones',i,'estado')== 'RECHAZADA'):
                        respuesta = 'Cliente Black: Fondos insuficientes para realizar la transferencia'

        return respuesta

#este print devuelve del JSON el alta de la compra de dolares, si le pasan gold lee el archivo gold, si le pasan classic lo mismo, etc.