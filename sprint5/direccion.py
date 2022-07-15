class Direccion:
    def __init__(self, **kwargs):
        self.pais= kwargs.get('pais')
        self.provincia= kwargs.get('provincia')
        self.ciudad= kwargs.get('ciudad')
        self.calle= kwargs.get('calle')
        self.numero= kwargs.get('numero')