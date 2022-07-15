from multiprocessing.connection import Client
from cuenta import Cuenta
from direccion import Direccion
# from modulos.classic import ClienteClassic


class Cliente:
    def __init__(self, **kwargs):
        self.cuenta = Cuenta(**kwargs)
        self.numero_de_cuenta = kwargs.get('numero_de_cuenta')  # composicion
        self.direccion = Direccion(**kwargs)  # composicion


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

    def getDatosCliente():
        return{
            "limite_extraccion_diario": 10000,
            "limite_transferencia_recibida": 150000,
            "costo_transferencia": 1,
            "saldo_descubierto_disponible": 0,
            "total_tarjetas_credito": 0,
            "total_chequeras": 0,
            "total_dolares": 0,
            "numero_de_cuenta": 0
        }

cliente1 = NuevoCliente.getDatosCliente()

print(cliente1)

#falta imprimir el nombre del cliente, hay que buscar una forma de imprimir tanto la class Cliente como NuevoCliente


