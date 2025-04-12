from database.database import get_connection
from ..models.entities.Emails import Email

class EmailModel:

    @classmethod
    def get_all_emails(cls):
        connection = None
        try:
            connection = get_connection()
            emails_list = []

            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT idemail, idcontacto, tipo, email
                    FROM emails
                    ORDER BY idemail ASC
                """)
                resultset = cursor.fetchall()
                for row in resultset:
                    email = Email(
                        idemail=row[0],
                        idcontacto=row[1],
                        tipo=row[2],
                        email=row[3]
                    )
                    emails_list.append(email.to_JSON())
            return emails_list
        except Exception as ex:
            print(f"Error en get_all_emails: {ex}")
            raise Exception(ex)
        finally:
            if connection:
                connection.close()

    @classmethod
    def add_email(cls, email: Email):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO emails (idemail, idcontacto, tipo, email)
                    VALUES (%s, %s, %s, %s)
                """, (
                    email.idemail,
                    email.idcontacto,
                    email.tipo,
                    email.email
                ))
                affected_rows = cursor.rowcount
                connection.commit()
                return affected_rows
        except Exception as ex:
            print(f"Error en add_email: {ex}")
            raise Exception(ex)
        finally:
            if connection:
                connection.close()

    @classmethod
    def update_email(cls, email: Email):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE emails
                    SET idcontacto = %s, tipo = %s, email = %s
                    WHERE idemail = %s
                """, (
                    email.idcontacto,
                    email.tipo,
                    email.email,
                    email.idemail
                ))
                affected_rows = cursor.rowcount
                connection.commit()
                return affected_rows
        except Exception as ex:
            print(f"Error en update_email: {ex}")
            raise Exception(ex)
        finally:
            if connection:
                connection.close()

    @classmethod
    def delete_email(cls, email: Email):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM emails
                    WHERE idemail = %s
                """, (email.idemail,))
                affected_rows = cursor.rowcount
                connection.commit()
                return affected_rows
        except Exception as ex:
            print(f"Error en delete_email: {ex}")
            raise Exception(ex)
        finally:
            if connection:
                connection.close()

    @classmethod
    def get_email_by_id(cls, id):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT idemail, idcontacto, tipo, email
                    FROM emails
                    WHERE idemail = %s
                """, (id,))
                row = cursor.fetchone()
                if row:
                    email = Email(
                        idemail=row[0],
                        idcontacto=row[1],
                        tipo=row[2],
                        email=row[3]
                    )
                    return email.to_JSON()
                else:
                    return None
        except Exception as ex:
            print(f"Error en get_email_by_id: {ex}")
            raise Exception(ex)
        finally:
            if connection:
                connection.close()
