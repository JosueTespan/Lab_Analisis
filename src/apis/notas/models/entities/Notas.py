from utils.DateFormat import DateFormat

class Nota:
    def __init__(self, idnota: str, idcontacto: str, nota: str, fecha: str):
        self.idnota = idnota
        self.idcontacto = idcontacto
        self.nota = nota
        self.fecha = DateFormat.convert_date(fecha)

    def to_JSON(self):
        return {
            "idnota": self.idnota,
            "idcontacto": self.idcontacto,
            "nota": self.nota,
            "fecha": self.fecha
        }
