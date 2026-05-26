from models.database import Database


class SugerenciasCtrl:

    def obtener_sugerencias():
        connection = Database.get_connection()
        if not connection:
            return []
        cursor = connection.cursor(dictionary=True)
        query = """ SELECT * FROM sugerencias """
        cursor.execute(query)
        sugerencias = cursor.fetchall()
        cursor.close()
        connection.close()
        return sugerencias


    def obtener_sugerencia(id_sugerencia):
        connection = Database.get_connection()
        if not connection:
            return None
        cursor = connection.cursor(dictionary=True)
        query = """ SELECT * FROM sugerencias WHERE id_sugerencia = %s """
        cursor.execute(query, (id_sugerencia,))
        sugerencia = cursor.fetchone()
        cursor.close()
        connection.close()
        return sugerencia


    def crear_sugerencia(tipo, titulo, descripcion):
        connection = Database.get_connection()
        if not connection:
            return False, "Error de conexión"
        try:
            cursor = connection.cursor()
            query = """ INSERT INTO sugerencias (tipo, titulo, descripcion) VALUES (%s, %s, %s) """
            values = (tipo, titulo, descripcion)
            cursor.execute(query, values)
            connection.commit()
            cursor.close()
            connection.close()
            return True, "Publicación enviada correctamente"
        except Exception as err:
            return False, f"Error: {err}"


    def editar_sugerencia(id_sugerencia, tipo, titulo, descripcion):
        connection = Database.get_connection()
        if not connection:
            return False, "Error de conexión"
        try:
            cursor = connection.cursor()
            query = """ UPDATE sugerencias SET tipo = %s,titulo = %s, descripcion = %s WHERE id_sugerencia = %s """
            values = (tipo,titulo,descripcion,id_sugerencia)
            cursor.execute(query, values)
            connection.commit()
            cursor.close()
            connection.close()
            return True, "Publicación actualizada correctamente"
        except Exception as err:
            return False, f"Error: {err}"


    def eliminar_sugerencia(id_sugerencia):
        connection = Database.get_connection()
        if not connection:
            return False, "Error de conexión"
        try:
            cursor = connection.cursor()
            query = """ DELETE FROM sugerencias WHERE id_sugerencia = %s """
            cursor.execute(query, (id_sugerencia,))
            connection.commit()
            cursor.close()
            connection.close()
            return True, "Publicación eliminada correctamente"
        except Exception as err:
            return False, f"Error: {err}"

    def buscar_sugerencias(titulo):
        connection = Database.get_connection()
        if not connection:
            return []
        cursor = connection.cursor(dictionary=True)
        query = """ SELECT * FROM sugerencias WHERE titulo LIKE %s """
        cursor.execute(query, (f"%{titulo}%",))
        sugerencias = cursor.fetchall()
        cursor.close()
        connection.close()
        return sugerencias