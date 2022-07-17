class Razon():
    def __init__(self,tipo):
        self.tipo = tipo
#puse Razon sin herencia porque es mucho mas practico, cambiaria lo de abajo por varios modulos y llamarlos acá de ultima para que se impriman las razones. Quedaría que se imprima todo lo del eventos y agregar las validaciones en caso de que el estado sea rechazado
        
class RazonAltaChequera(Razon): 
    def __init__(self,resolver):
        super().__init__(resolver)
        self.resolver= 'Alta chequera'

class RazonAltaTarjetaCredito(Razon): 
    def __init__(self,resolver):
        super().__init__(resolver)
        self.resolver= 'Alta tarjeta de credito'

class RazonCompraDolar(Razon): 
    def __init__(self,resolver):
        super().__init__(resolver)
        self.resolver= 'Compra dolares'

class RazonRetiroefectivo(Razon): 
    def __init__(self,resolver):
        super().__init__(resolver)
        self.resolver= 'Retiro efectivo'

class RazonTransferenciaEnviada(Razon): 
    def __init__(self,resolver):
        super().__init__(resolver)
        self.resolver= 'Transferencia enviada'

class RazonTransferenciaRecibida(Razon): 
    def __init__(self,resolver):
        super().__init__(resolver)
        self.resolver= 'Transferencia recibida'
