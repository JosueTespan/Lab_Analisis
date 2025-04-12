class Empresa:
    def __init__(self, idempresa: str, nombre: str, categoria: str):
        self.idempresa = idempresa
        self.nombre = nombre
        self.categoria = categoria

    def to_JSON(self):
        return {
            "idempresa": self.idempresa,
            "nombre": self.nombre,
            "categoria": self.categoria
        }
