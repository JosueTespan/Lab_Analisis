class Telefono:
    def __init__(self, idtelefono: str, idcontacto: str, tipo: str, numero: str):
        self.idtelefono = idtelefono
        self.idcontacto = idcontacto
        self.tipo = tipo
        self.numero = numero

    def to_JSON(self):
        return {
            "idtelefono": self.idtelefono,
            "idcontacto": self.idcontacto,
            "tipo": self.tipo,
            "numero": self.numero
        }
