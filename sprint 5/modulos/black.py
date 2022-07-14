from cliente import Cliente

class ClienteBlack(Cliente):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def crear_tarjeta_credito():
        return True
    
    def crear_chequera():
        return True
    
    def comprar_dolares():
        return True

cliente = ClienteBlack()
print(cliente)