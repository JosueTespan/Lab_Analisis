from utils.DateFormat import DateFormat

class Contacto:
    def __init__(self, idcontacto: str = None, nombre: str = "", apellido: str = "", 
                 idcategoria: str = "", idempresa: str = "", fecha_nacimiento: str = ""):
        self.idcontacto = idcontacto
        self.nombre = nombre
        self.apellido = apellido
        self.idcategoria = idcategoria
        self.idempresa = idempresa
        self.fecha_nacimiento = DateFormat.convert_date(fecha_nacimiento)

    def to_JSON(self):
        return {
            "idcontacto": self.idcontacto,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "idcategoria": self.idcategoria,
            "idempresa": self.idempresa,
            "fecha_nacimiento": self.fecha_nacimiento.strftime('%d/%m/%Y')
        }


