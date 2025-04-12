from utils.DateFormat import DateFormat
from datetime import datetime

class Notificacion:
    def __init__(self, id: str, idcontacto: str, fecha_envio: str, estado: str):
        self.id = id
        self.idcontacto = idcontacto
        self.fecha_envio = DateFormat.convert_date(fecha_envio)
        self.estado = estado

    def to_JSON(self):
        return {
            "id": self.id,
            "idcontacto": self.idcontacto,
            "fecha_envio": self.fecha_envio.strftime('%d/%m/%Y') if isinstance(self.fecha_envio, datetime) else self.fecha_envio,
            "estado": self.estado
        }
