from database.database import get_connection
from utils.DateFormat import DateFormat
from ..models.entities.Notas import Nota  
class NotaModel:

    @classmethod
    def get_all_notas(cls):
        connection = None
        try:
            connection = get_connection()
            notas_list = []

            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT idnota, idcontacto, nota, fecha
                    FROM notas
                    ORDER BY fecha DESC
                """)
                resultset = cursor.fetchall()
                for row in resultset:
                    nota = Nota(
                        idnota=row[0],
                        idcontacto=row[1],
                        nota=row[2],
                        fecha=DateFormat.convert_date(row[3])
                    )
                    notas_list.append(nota.to_JSON())
            return notas_list
        except Exception as ex:
            print(f"Error en get_all_notas: {ex}")
            raise
        finally:
            if connection:
                connection.close()

    @classmethod
    def add_nota(cls, nota: Nota):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO notas (idnota, idcontacto, nota, fecha)
                    VALUES (%s, %s, %s, %s)
                """, (
                    nota.idnota,
                    nota.idcontacto,
                    nota.nota,
                    nota.fecha
                ))
                connection.commit()
                return cursor.rowcount
        except Exception as ex:
            print(f"Error en add_nota: {ex}")
            raise
        finally:
            if connection:
                connection.close()

    @classmethod
    def update_nota(cls, nota: Nota):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE notas
                    SET idcontacto = %s, nota = %s, fecha = %s
                    WHERE idnota = %s
                """, (
                    nota.idcontacto,
                    nota.nota,
                    nota.fecha,
                    nota.idnota
                ))
                connection.commit()
                return cursor.rowcount
        except Exception as ex:
            print(f"Error en update_nota: {ex}")
            raise
        finally:
            if connection:
                connection.close()

    @classmethod
    def delete_nota(cls, nota: Nota):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM notas
                    WHERE idnota = %s
                """, (nota.idnota,))
                connection.commit()
                return cursor.rowcount
        except Exception as ex:
            print(f"Error en delete_nota: {ex}")
            raise
        finally:
            if connection:
                connection.close()

    @classmethod
    def get_nota_by_id(cls, idnota: str):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT idnota, idcontacto, nota, fecha
                    FROM notas
                    WHERE idnota = %s
                """, (idnota,))
                row = cursor.fetchone()
                if row:
                    nota = Nota(
                        idnota=row[0],
                        idcontacto=row[1],
                        nota=row[2],
                        fecha=DateFormat.convert_date(row[3])
                    )
                    return nota.to_JSON()
                return None
        except Exception as ex:
            print(f"Error en get_nota_by_id: {ex}")
            raise
        finally:
            if connection:
                connection.close()
