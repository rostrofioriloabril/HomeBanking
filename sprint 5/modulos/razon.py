class Razon:
    def __init__(self,resolver):
        self.resolver=resolver

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
