from multiprocessing.connection import Client
from cuenta import Cuenta
from direccion import Direccion
# from modulos.classic import ClienteClassic

#creamos una clase Cliente que va a tener los atributos generales de todos los clientes del banco
class Cliente:
    def __init__(self, **kwargs): #kwargs lo usamos para no tener que escribir todos los atributos entre paréntesis y lo hacemos directamente abajo
        self.cuenta = Cuenta(**kwargs)
        self.numero_de_cuenta = kwargs.get('numero_de_cuenta')  # composicion
        self.direccion = Direccion(**kwargs)  # composicion

#ahora vamos a buscar los datos del cliente
    def inicializar(self, datos):
        self.numero = datos['numero']
        self.nombre = datos['nombre']
        self.apellido = datos['apellido']
        self.dni = datos['dni']
        
    def crear_tarjeta_debito(tarjetaDebito):
        tarjetaDebito = True
    
    def mostrar_nombre(self):
        return print(self.nombre,self.apellido)

    # otros metodos

class NuevoCliente(Cliente):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def getDatosClassic():
        datos_classic= {"limite_extraccion_diario": 10000,
            "limite_transferencia_recibida": 150000,
            "costo_transferencia": 1,
            "saldo_descubierto_disponible": 0,
            "total_tarjetas_credito": 0,
            "total_chequeras": 0,
            "total_caja_dolares": 0,
            "numero_de_cuenta": 0}
        return datos_classic
    def getDatosGold():
        datos_gold= {"limite_extraccion_diario": 20000,
            "limite_transferencia_recibida": 500000,
            "costo_transferencia": 0.5,
            "saldo_descubierto_disponible": 10000,
            "total_tarjetas_credito": 1,
            "total_chequeras": 1,
            "total_caja_dolares": 1,
            "numero_de_cuenta": 0}
        return datos_gold
    def getDatosBlack():
        datos_gold= {"limite_extraccion_diario": 100000,
            "limite_transferencia_recibida": None,
            "costo_transferencia": 0,
            "saldo_descubierto_disponible": 10000,
            "total_tarjetas_credito": 5,
            "total_chequeras": 2,
            "total_caja_dolares": 1,
            "numero_de_cuenta": 0}
        return datos_gold
#Hice 3 funciones a los que podamos acceder, dentro hay diccionarios, uno para cada clase para poder tomar sus elementos en las validaciones. para acceder a ellos ponemos: NuevoCliente.getDatosClassic()["numero_de_cuenta"]  #asi con cada parte que queramos usar.
#falta imprimir el nombre del cliente, hay que buscar una forma de imprimir tanto la class Cliente como NuevoCliente
