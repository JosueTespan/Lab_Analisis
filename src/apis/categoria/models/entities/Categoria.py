class Categoria:
    def __init__(self, IdCategoria: str, nombre: str, descripcion: str):
        self.IdCategoria = IdCategoria
        self.nombre = nombre
        self.descripcion = descripcion

    def to_JSON(self):
        return {
            "IdCategoria": self.IdCategoria,
            "nombre": self.nombre,
            "descripcion": self.descripcion
        }

