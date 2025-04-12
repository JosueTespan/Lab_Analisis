from database.database import get_connection
from utils.DateFormat import DateFormat
from ..models.entities.Notificaciones import Notificacion

class NotificacionModel:

    @classmethod
    def contacto_existe(cls, idcontacto: str):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1 FROM contactos WHERE idcontacto = %s", (idcontacto,))
                return cursor.fetchone() is not None
        except Exception as ex:
            print(f"Error en contacto_existe: {ex}")
            raise
        finally:
            if connection:
                connection.close()

    @classmethod
    def get_all_notificaciones(cls):
        connection = None
        try:
            connection = get_connection()
            notifications_list = []

            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id, idcontacto, fecha_envio, estado
                    FROM notificaciones
                    ORDER BY fecha_envio DESC
                """)
                resultset = cursor.fetchall()
                for row in resultset:
                    notification = Notificacion(
                        id=row[0],
                        idcontacto=row[1],
                        fecha_envio=row[2],
                        estado=row[3]
                    )
                    notifications_list.append(notification.to_JSON())
            return notifications_list
        except Exception as ex:
            print(f"Error en get_all_notificaciones: {ex}")
            raise
        finally:
            if connection:
                connection.close()

    @classmethod
    def add_notification(cls, notification: Notificacion):
        connection = None
        try:
            if not cls.contacto_existe(notification.idcontacto):
                raise ValueError(f"El contacto con ID {notification.idcontacto} no existe.")

            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO notificaciones (id, idcontacto, fecha_envio, estado)
                    VALUES (%s, %s, %s, %s)
                """, (
                    notification.id,
                    notification.idcontacto,
                    notification.fecha_envio,
                    notification.estado
                ))
                connection.commit()
                return cursor.rowcount
        except Exception as ex:
            print(f"Error en add_notification: {ex}")
            raise
        finally:
            if connection:
                connection.close()

    @classmethod
    def update_notification(cls, notification: Notificacion):
        connection = None
        try:
            if not cls.contacto_existe(notification.idcontacto):
                raise ValueError(f"El contacto con ID {notification.idcontacto} no existe.")

            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE notificaciones
                    SET idcontacto = %s, fecha_envio = %s, estado = %s
                    WHERE id = %s
                """, (
                    notification.idcontacto,
                    notification.fecha_envio,
                    notification.estado,
                    notification.id
                ))
                connection.commit()
                return cursor.rowcount
        except Exception as ex:
            print(f"Error en update_notification: {ex}")
            raise
        finally:
            if connection:
                connection.close()

    @classmethod
    def delete_notification(cls, notification: Notificacion):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM notificaciones
                    WHERE id = %s
                """, (notification.id,))
                connection.commit()
                return cursor.rowcount
        except Exception as ex:
            print(f"Error en delete_notification: {ex}")
            raise
        finally:
            if connection:
                connection.close()

    @classmethod
    def get_notification_by_id(cls, id: str):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id, idcontacto, fecha_envio, estado
                    FROM notificaciones
                    WHERE id = %s
                """, (id,))
                row = cursor.fetchone()
                if row:
                    notification = Notificacion(
                        id=row[0],
                        idcontacto=row[1],
                        fecha_envio=row[2],
                        estado=row[3]
                    )
                    return notification.to_JSON()
                return None
        except Exception as ex:
            print(f"Error en get_notification_by_id: {ex}")
            raise
        finally:
            if connection:
                connection.close()
