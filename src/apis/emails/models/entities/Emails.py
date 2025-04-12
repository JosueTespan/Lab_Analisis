class Email:
    def __init__(self, idemail: str, idcontacto: str, tipo: str, email: str):
        self.idemail = idemail
        self.idcontacto = idcontacto
        self.tipo = tipo
        self.email = email

    def to_JSON(self):
        return {
            "idemail": self.idemail,
            "idcontacto": self.idcontacto,
            "tipo": self.tipo,
            "email": self.email
        }
