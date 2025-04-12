class Direccion:
    def __init__(self, iddireccion: str, idcontacto: str, direccion: str, ciudad: str, estado: str, pais: str, codigo_postal: str):
        self.iddireccion = iddireccion
        self.idcontacto = idcontacto
        self.direccion = direccion
        self.ciudad = ciudad
        self.estado = estado
        self.pais = pais
        self.codigo_postal = codigo_postal

    def to_JSON(self):
        return {
            "iddireccion": self.iddireccion,
            "idcontacto": self.idcontacto,
            "direccion": self.direccion,
            "ciudad": self.ciudad,
            "estado": self.estado,
            "pais": self.pais,
            "codigo_postal": self.codigo_postal
        }
