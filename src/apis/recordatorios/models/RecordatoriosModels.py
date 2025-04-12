from database.database import get_connection
from utils.DateFormat import DateFormat
from ..models.entities.Recordatorios import Recordatorios

class RecordatoriosModels:

    @classmethod
    def get_all_recordatorios(cls):
        connection = None
        try:
            connection = get_connection()
            recordatorios_list = []

            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT idrecordatorio, idcontacto, descripcion, fecha_recordatorio, completado
                    FROM recordatorios
                    ORDER BY fecha_recordatorio ASC
                """)
                resultset = cursor.fetchall()
                for row in resultset:
                    recordatorio = Recordatorios(
                        idrecordatorio=row[0],
                        idcontacto=row[1],
                        descripcion=row[2],
                        fecha_recordatorio=DateFormat.convert_date(row[3]),
                        completado=row[4]
                    )
                    recordatorios_list.append(recordatorio.to_JSON())
            return recordatorios_list
        except Exception as ex:
            print(f"[Error] get_all_recordatorios: {ex}")
            raise
        finally:
            if connection:
                connection.close()

    @classmethod
    def get_recordatorio_by_id(cls, idrecordatorio: str):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT idrecordatorio, idcontacto, descripcion, fecha_recordatorio, completado
                    FROM recordatorios
                    WHERE idrecordatorio = %s
                """, (idrecordatorio,))
                row = cursor.fetchone()
                if row:
                    recordatorio = Recordatorios(
                        idrecordatorio=row[0],
                        idcontacto=row[1],
                        descripcion=row[2],
                        fecha_recordatorio=DateFormat.convert_date(row[3]),
                        completado=row[4]
                    )
                    return recordatorio.to_JSON()
                return None
        except Exception as ex:
            print(f"[Error] get_recordatorio_by_id: {ex}")
            raise
        finally:
            if connection:
                connection.close()

    @classmethod
    def add_recordatorio(cls, recordatorio: Recordatorios):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO recordatorios (idrecordatorio, idcontacto, descripcion, fecha_recordatorio, completado)
                    VALUES (%s, %s, %s, %s, %s)
                """, (
                    recordatorio.idrecordatorio,
                    recordatorio.idcontacto,
                    recordatorio.descripcion,
                    recordatorio.fecha_recordatorio,
                    recordatorio.completado
                ))
                connection.commit()
                return cursor.rowcount
        except Exception as ex:
            print(f"[Error] add_recordatorio: {ex}")
            raise
        finally:
            if connection:
                connection.close()

    @classmethod
    def update_recordatorio(cls, recordatorio: Recordatorios):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE recordatorios
                    SET idcontacto = %s, descripcion = %s, fecha_recordatorio = %s, completado = %s
                    WHERE idrecordatorio = %s
                """, (
                    recordatorio.idcontacto,
                    recordatorio.descripcion,
                    recordatorio.fecha_recordatorio,
                    recordatorio.completado,
                    recordatorio.idrecordatorio
                ))
                connection.commit()
                return cursor.rowcount
        except Exception as ex:
            print(f"[Error] update_recordatorio: {ex}")
            raise
        finally:
            if connection:
                connection.close()

    @classmethod
    def delete_recordatorio(cls, idrecordatorio: str):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM recordatorios
                    WHERE idrecordatorio = %s
                """, (idrecordatorio,))
                connection.commit()
                return cursor.rowcount
        except Exception as ex:
            print(f"[Error] delete_recordatorio: {ex}")
            raise
        finally:
            if connection:
                connection.close()
