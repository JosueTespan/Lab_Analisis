from utils.DateFormat import DateFormat

class Recordatorios:
    def __init__(self, idrecordatorio: str, idcontacto: str, descripcion: str, 
                 fecha_recordatorio: str, completado: bool):
        self.idrecordatorio = idrecordatorio
        self.idcontacto = idcontacto
        self.descripcion = descripcion
        self.fecha_recordatorio = DateFormat.convert_date(fecha_recordatorio)  
        self.completado = completado

    def to_JSON(self):
        return {
            "idrecordatorio": self.idrecordatorio,
            "idcontacto": self.idcontacto,
            "descripcion": self.descripcion,
            "fecha_recordatorio": self.fecha_recordatorio,
            "completado": self.completado
        }
