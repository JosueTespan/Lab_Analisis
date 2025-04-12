from database.database import get_connection
from ..models.entities.Empresa import Empresa

class EmpresaModel:

    @classmethod
    def get_all_empresas(cls):
        connection = None
        try:
            connection = get_connection()
            empresas_list = []

            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT idempresa, nombre, categoria
                    FROM empresas
                    ORDER BY nombre ASC
                """)
                resultset = cursor.fetchall()
                for row in resultset:
                    empresa = Empresa(
                        idempresa=row[0],
                        nombre=row[1],
                        categoria=row[2]
                    )
                    empresas_list.append(empresa.to_JSON())
            return empresas_list
        except Exception as ex:
            print(f"Error en get_all_empresas: {ex}")
            raise Exception(ex)
        finally:
            if connection:
                connection.close()

    @classmethod
    def add_empresa(cls, empresa: Empresa):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO empresas (idempresa, nombre, categoria)
                    VALUES (%s, %s, %s)
                """, (
                    empresa.idempresa,
                    empresa.nombre,
                    empresa.categoria
                ))
                affected_rows = cursor.rowcount
                connection.commit()
                return affected_rows
        except Exception as ex:
            print(f"Error en add_empresa: {ex}")
            raise Exception(ex)
        finally:
            if connection:
                connection.close()

    @classmethod
    def update_empresa(cls, empresa: Empresa):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE empresas
                    SET nombre = %s, categoria = %s
                    WHERE idempresa = %s
                """, (
                    empresa.nombre,
                    empresa.categoria,
                    empresa.idempresa
                ))
                affected_rows = cursor.rowcount
                connection.commit()
                return affected_rows
        except Exception as ex:
            print(f"Error en update_empresa: {ex}")
            raise Exception(ex)
        finally:
            if connection:
                connection.close()

    @classmethod
    def delete_empresa(cls, empresa: Empresa):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM empresas
                    WHERE idempresa = %s
                """, (empresa.idempresa,))
                affected_rows = cursor.rowcount
                connection.commit()
                return affected_rows
        except Exception as ex:
            print(f"Error en delete_empresa: {ex}")
            raise Exception(ex)
        finally:
            if connection:
                connection.close()

    @classmethod
    def get_empresa_by_id(cls, id):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT idempresa, nombre, categoria
                    FROM empresas
                    WHERE idempresa = %s
                """, (id,))
                row = cursor.fetchone()
                if row:
                    empresa = Empresa(
                        idempresa=row[0],
                        nombre=row[1],
                        categoria=row[2]
                    )
                    return empresa.to_JSON()
                else:
                    return None
        except Exception as ex:
            print(f"Error en get_empresa_by_id: {ex}")
            raise Exception(ex)
        finally:
            if connection:
                connection.close()
