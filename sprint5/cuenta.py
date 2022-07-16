#acá también creamos restricciones de cuenta, pero a nivel general. Si no encuentra el valor, devuelve 0
class Cuenta:
    def __init__(self, **kwargs):
        self.tipo = kwargs.get('tipo', 0)
        self.limite_extraccion_diario = kwargs.get('limite_extraccion_diario', 0)
        self.limite_transferencia_recibida = kwargs.get('limite_transferencia_recibida', 0)
        self.costo_transferencia = kwargs.get('costo_transferencia', 0)
        self.saldo_descubierto_disponible = kwargs.get('saldo_descubierto_disponible', 0)

    def mostrarTipo(self):
        return print(self.tipo)