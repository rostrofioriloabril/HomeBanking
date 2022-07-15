from cliente import Cliente

class ClienteClassic(Cliente):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def crear_tarjeta_credito():
        return False
    
    def crear_chequera():
        return False
    
    def comprar_dolares():
        return False

cliente = ClienteClassic()
print(cliente)