from database.database import get_connection

def get_notification_data(contacto_id):
    connection = get_connection()
    query = """
        SELECT nombre, apellido, idcategoria, idempresa, fecha_nacimiento
        FROM contactos
        WHERE idcontacto = %s
    """
    results = []
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, (contacto_id,))
            rows = cursor.fetchall()
            for row in rows:
                results.append({
                    "nombre": row[0],
                    "apellido": row[1],
                    "idcategoria": row[2],
                    "idempresa": row[3],
                    "fecha_nacimiento": row[4]
                })
    except Exception as e:
        raise Exception(f"Error al ejecutar get_notification_data: {str(e)}")
    finally:
        connection.close()
    return results
