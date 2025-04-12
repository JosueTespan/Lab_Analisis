from database.database import get_connection
from utils.DateFormat import DateFormat
from ..models.entities.Contactos import Contacto

class ContactoModel:

    @classmethod
    def get_all_contactos(cls):
        connection = None
        try:
            connection = get_connection()
            contactos_list = []

            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT idcontacto, nombre, apellido, idcategoria, idempresa, fecha_nacimiento
                    FROM contactos
                    ORDER BY nombre ASC
                """)
                resultset = cursor.fetchall()
                for row in resultset:
                    contacto = Contacto(
                        idcontacto=row[0],
                        nombre=row[1],
                        apellido=row[2],
                        idcategoria=row[3],
                        idempresa=row[4],
                        fecha_nacimiento=DateFormat.convert_date(row[5])
                    )
                    contactos_list.append(contacto.to_JSON())
            return contactos_list
        except Exception as ex:
            print(f"Error en get_all_contactos: {ex}")
            raise
        finally:
            if connection:
                connection.close()

    @classmethod
    def add_contacto(cls, contacto: Contacto):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO contactos (idcontacto, nombre, apellido, idcategoria, idempresa, fecha_nacimiento)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (
                    contacto.idcontacto,
                    contacto.nombre,
                    contacto.apellido,
                    contacto.idcategoria,
                    contacto.idempresa,
                    contacto.fecha_nacimiento
                ))
                connection.commit()
                return cursor.rowcount
        except Exception as ex:
            print(f"Error en add_contacto: {ex}")
            raise
        finally:
            if connection:
                connection.close()

    @classmethod
    def update_contacto(cls, contacto: Contacto):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE contactos
                    SET nombre = %s, apellido = %s, idcategoria = %s, idempresa = %s, fecha_nacimiento = %s
                    WHERE idcontacto = %s
                """, (
                    contacto.nombre,
                    contacto.apellido,
                    contacto.idcategoria,
                    contacto.idempresa,
                    contacto.fecha_nacimiento,
                    contacto.idcontacto
                ))
                connection.commit()
                return cursor.rowcount
        except Exception as ex:
            print(f"Error en update_contacto: {ex}")
            raise
        finally:
            if connection:
                connection.close()

    @classmethod
    def delete_contacto(cls, contacto: Contacto):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM contactos
                    WHERE idcontacto = %s
                """, (contacto.idcontacto,))
                connection.commit()
                return cursor.rowcount
        except Exception as ex:
            print(f"Error en delete_contacto: {ex}")
            raise
        finally:
            if connection:
                connection.close()

    @classmethod
    def get_contacto_by_id(cls, idcontacto: str):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT idcontacto, nombre, apellido, idcategoria, idempresa, fecha_nacimiento
                    FROM contactos
                    WHERE idcontacto = %s
                """, (idcontacto,))
                row = cursor.fetchone()
                if row:
                    contacto = Contacto(
                        idcontacto=row[0],
                        nombre=row[1],
                        apellido=row[2],
                        idcategoria=row[3],
                        idempresa=row[4],
                        fecha_nacimiento=DateFormat.convert_date(row[5])
                    )
                    return contacto.to_JSON()
                return None
        except Exception as ex:
            print(f"Error en get_contacto_by_id: {ex}")
            raise
        finally:
            if connection:
                connection.close()
