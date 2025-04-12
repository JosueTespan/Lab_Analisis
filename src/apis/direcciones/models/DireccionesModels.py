from database.database import get_connection
from ..models.entities.Direcciones import Direccion

class DireccionModel:

    @classmethod
    def get_all_direcciones(cls):
        connection = None
        try:
            connection = get_connection()
            direcciones_list = []

            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT iddireccion, idcontacto, direccion, ciudad, estado, pais, codigo_postal
                    FROM direcciones
                    ORDER BY ciudad ASC
                """)
                resultset = cursor.fetchall()
                for row in resultset:
                    direccion = Direccion(
                        iddireccion=row[0],
                        idcontacto=row[1],
                        direccion=row[2],
                        ciudad=row[3],
                        estado=row[4],
                        pais=row[5],
                        codigo_postal=row[6]
                    )
                    direcciones_list.append(direccion.to_JSON())
            return direcciones_list
        except Exception as ex:
            print(f"Error en get_all_direcciones: {ex}")
            raise Exception(ex)
        finally:
            if connection:
                connection.close()

    @classmethod
    def add_direccion(cls, direccion: Direccion):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO direcciones (iddireccion, idcontacto, direccion, ciudad, estado, pais, codigo_postal)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (
                    direccion.iddireccion,
                    direccion.idcontacto,
                    direccion.direccion,
                    direccion.ciudad,
                    direccion.estado,
                    direccion.pais,
                    direccion.codigo_postal
                ))
                affected_rows = cursor.rowcount
                connection.commit()
                return affected_rows
        except Exception as ex:
            print(f"Error en add_direccion: {ex}")
            raise Exception(ex)
        finally:
            if connection:
                connection.close()

    @classmethod
    def update_direccion(cls, direccion: Direccion):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE direcciones
                    SET idcontacto = %s, direccion = %s, ciudad = %s, estado = %s, pais = %s, codigo_postal = %s
                    WHERE iddireccion = %s
                """, (
                    direccion.idcontacto,
                    direccion.direccion,
                    direccion.ciudad,
                    direccion.estado,
                    direccion.pais,
                    direccion.codigo_postal,
                    direccion.iddireccion
                ))
                affected_rows = cursor.rowcount
                connection.commit()
                return affected_rows
        except Exception as ex:
            print(f"Error en update_direccion: {ex}")
            raise Exception(ex)
        finally:
            if connection:
                connection.close()

    @classmethod
    def delete_direccion(cls, direccion: Direccion):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM direcciones
                    WHERE iddireccion = %s
                """, (direccion.iddireccion,))
                affected_rows = cursor.rowcount
                connection.commit()
                return affected_rows
        except Exception as ex:
            print(f"Error en delete_direccion: {ex}")
            raise Exception(ex)
        finally:
            if connection:
                connection.close()

    @classmethod
    def get_direccion_by_id(cls, id):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT iddireccion, idcontacto, direccion, ciudad, estado, pais, codigo_postal
                    FROM direcciones
                    WHERE iddireccion = %s
                """, (id,))
                row = cursor.fetchone()
                if row:
                    direccion = Direccion(
                        iddireccion=row[0],
                        idcontacto=row[1],
                        direccion=row[2],
                        ciudad=row[3],
                        estado=row[4],
                        pais=row[5],
                        codigo_postal=row[6]
                    )
                    return direccion.to_JSON()
                else:
                    return None
        except Exception as ex:
            print(f"Error en get_direccion_by_id: {ex}")
            raise Exception(ex)
        finally:
            if connection:
                connection.close()
