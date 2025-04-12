from database.database import get_connection
from ..models.entities.Categoria import Categoria

class CategoriaModel:

    @classmethod
    def get_all_categoria(cls):
        connection = None
        try:
            connection = get_connection()
            categorias_list = []

            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT IdCategoria, nombre, descripcion
                    FROM categorias
                    ORDER BY nombre ASC
                """)
                resultset = cursor.fetchall()
                for row in resultset:
                    categoria = Categoria(
                        IdCategoria=row[0],
                        nombre=row[1],
                        descripcion=row[2]
                    )
                    categorias_list.append(categoria.to_JSON())
            return categorias_list
        except Exception as ex:
            print(f"Error en get_all_categoria: {ex}")
            raise Exception(ex)
        finally:
            if connection:
                connection.close()

    @classmethod
    def add_categoria(cls, categoria: Categoria):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO categorias (IdCategoria, nombre, descripcion)
                    VALUES (%s, %s, %s)
                """, (
                    categoria.IdCategoria,
                    categoria.nombre,
                    categoria.descripcion
                ))
                affected_rows = cursor.rowcount
                connection.commit()
                return affected_rows
        except Exception as ex:
            print(f"Error en add_categoria: {ex}")
            raise Exception(ex)
        finally:
            if connection:
                connection.close()

    @classmethod
    def update_categoria(cls, categoria: Categoria):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE categorias
                    SET nombre = %s, descripcion = %s
                    WHERE IdCategoria = %s
                """, (
                    categoria.nombre,
                    categoria.descripcion,
                    categoria.IdCategoria
                ))
                affected_rows = cursor.rowcount
                connection.commit()
                return affected_rows
        except Exception as ex:
            print(f"Error en update_categoria: {ex}")
            raise Exception(ex)
        finally:
            if connection:
                connection.close()

    @classmethod
    def delete_categoria(cls, categoria: Categoria):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM categorias
                    WHERE IdCategoria = %s
                """, (categoria.IdCategoria,))
                affected_rows = cursor.rowcount
                connection.commit()
                return affected_rows
        except Exception as ex:
            print(f"Error en delete_categoria: {ex}")
            raise Exception(ex)
        finally:
            if connection:
                connection.close()

    @classmethod
    def get_categoria_by_id(cls, id):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT IdCategoria, nombre, descripcion
                    FROM categorias
                    WHERE IdCategoria = %s
                """, (id,))
                row = cursor.fetchone()
                if row:
                    categoria = Categoria(
                        IdCategoria=row[0],
                        nombre=row[1],
                        descripcion=row[2]
                    )
                    return categoria.to_JSON()
                else:
                    return None
        except Exception as ex:
            print(f"Error en get_categoria_by_id: {ex}")
            raise Exception(ex)
        finally:
            if connection:
                connection.close()

