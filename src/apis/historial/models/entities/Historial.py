from utils.DateFormat import DateFormat

class Historial:
    def __init__(self, idhistorial: str, idcontacto: str, descripcion: str, fecha):
        self.idhistorial = idhistorial
        self.idcontacto = idcontacto
        self.descripcion = descripcion
        self.fecha = DateFormat.convert_date(fecha)  

    def to_JSON(self):
        return {
            "idhistorial": self.idhistorial,
            "idcontacto": self.idcontacto,
            "descripcion": self.descripcion,
            "fecha": self.fecha  
        }
