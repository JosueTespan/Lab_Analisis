from database.database import get_connection
from utils.DateFormat import DateFormat
from ..models.entities.Historial import Historial

class HistorialModel:

    @classmethod
    def get_all_historiales(cls):
        connection = None
        try:
            connection = get_connection()
            historial_list = []

            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT idhistorial, idcontacto, descripcion, fecha
                    FROM historial
                    ORDER BY fecha DESC
                """)
                resultset = cursor.fetchall()
                for row in resultset:
                    historial = Historial(
                        idhistorial=row[0],
                        idcontacto=row[1],
                        descripcion=row[2],
                        fecha=DateFormat.convert_date(row[3])
                    )
                    historial_list.append(historial.to_JSON())
            return historial_list
        except Exception as ex:
            print(f"Error en get_all_historiales: {ex}")
            raise
        finally:
            if connection:
                connection.close()

    @classmethod
    def get_historial_by_id(cls, idhistorial: str):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT idhistorial, idcontacto, descripcion, fecha
                    FROM historial
                    WHERE idhistorial = %s
                """, (idhistorial,))
                row = cursor.fetchone()
                if row:
                    historial = Historial(
                        idhistorial=row[0],
                        idcontacto=row[1],
                        descripcion=row[2],
                        fecha=DateFormat.convert_date(row[3])
                    )
                    return historial.to_JSON()
                return None
        except Exception as ex:
            print(f"Error en get_historial_by_id: {ex}")
            raise
        finally:
            if connection:
                connection.close()

    @classmethod
    def add_historial(cls, historial: Historial):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO historial (idhistorial, idcontacto, descripcion, fecha)
                    VALUES (%s, %s, %s, %s)
                """, (
                    historial.idhistorial,
                    historial.idcontacto,
                    historial.descripcion,
                    historial.fecha
                ))
                connection.commit()
                return cursor.rowcount
        except Exception as ex:
            print(f"Error en add_historial: {ex}")
            raise
        finally:
            if connection:
                connection.close()

    @classmethod
    def update_historial(cls, historial: Historial):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE historial
                    SET idcontacto = %s, descripcion = %s, fecha = %s
                    WHERE idhistorial = %s
                """, (
                    historial.idcontacto,
                    historial.descripcion,
                    historial.fecha,
                    historial.idhistorial
                ))
                connection.commit()
                return cursor.rowcount
        except Exception as ex:
            print(f"Error en update_historial: {ex}")
            raise
        finally:
            if connection:
                connection.close()

    @classmethod
    def delete_historial(cls, historial: Historial):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM historial
                    WHERE idhistorial = %s
                """, (historial.idhistorial,))
                connection.commit()
                return cursor.rowcount
        except Exception as ex:
            print(f"Error en delete_historial: {ex}")
            raise
        finally:
            if connection:
                connection.close()
