from database.database import get_connection
from ..models.entities.Telefonos import Telefono

class TelefonoModel:

    @classmethod
    def get_all_telefonos(cls):
        connection = None
        try:
            connection = get_connection()
            telefonos_list = []

            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT idtelefono, idcontacto, tipo, numero
                    FROM telefonos
                    ORDER BY idtelefono ASC
                """)
                resultset = cursor.fetchall()
                for row in resultset:
                    telefono = Telefono(
                        idtelefono=row[0],
                        idcontacto=row[1],
                        tipo=row[2],
                        numero=row[3]
                    )
                    telefonos_list.append(telefono.to_JSON())
            return telefonos_list
        except Exception as ex:
            print(f"Error en get_all_telefonos: {ex}")
            raise Exception(ex)
        finally:
            if connection:
                connection.close()

    @classmethod
    def add_telefono(cls, telefono: Telefono):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO telefonos (idtelefono, idcontacto, tipo, numero)
                    VALUES (%s, %s, %s, %s)
                """, (
                    telefono.idtelefono,
                    telefono.idcontacto,
                    telefono.tipo,
                    telefono.numero
                ))
                affected_rows = cursor.rowcount
                connection.commit()
                return affected_rows
        except Exception as ex:
            print(f"Error en add_telefono: {ex}")
            raise Exception(ex)
        finally:
            if connection:
                connection.close()

    @classmethod
    def update_telefono(cls, telefono: Telefono):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE telefonos
                    SET idcontacto = %s, tipo = %s, numero = %s
                    WHERE idtelefono = %s
                """, (
                    telefono.idcontacto,
                    telefono.tipo,
                    telefono.numero,
                    telefono.idtelefono
                ))
                affected_rows = cursor.rowcount
                connection.commit()
                return affected_rows
        except Exception as ex:
            print(f"Error en update_telefono: {ex}")
            raise Exception(ex)
        finally:
            if connection:
                connection.close()

    @classmethod
    def delete_telefono(cls, telefono: Telefono):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM telefonos
                    WHERE idtelefono = %s
                """, (telefono.idtelefono,))
                affected_rows = cursor.rowcount
                connection.commit()
                return affected_rows
        except Exception as ex:
            print(f"Error en delete_telefono: {ex}")
            raise Exception(ex)
        finally:
            if connection:
                connection.close()

    @classmethod
    def get_telefono_by_id(cls, id):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT idtelefono, idcontacto, tipo, numero
                    FROM telefonos
                    WHERE idtelefono = %s
                """, (id,))
                row = cursor.fetchone()
                if row:
                    telefono = Telefono(
                        idtelefono=row[0],
                        idcontacto=row[1],
                        tipo=row[2],
                        numero=row[3]
                    )
                    return telefono.to_JSON()
                else:
                    return None
        except Exception as ex:
            print(f"Error en get_telefono_by_id: {ex}")
            raise Exception(ex)
        finally:
            if connection:
                connection.close()
