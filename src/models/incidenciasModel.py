from models.database import Database


class IncidenciasCtrl:

    def obtener_reportes():
        connection = Database.get_connection()
        if not connection:
            return []
        cursor = connection.cursor(dictionary=True)
        query = """ SELECT * FROM reportes """
        cursor.execute(query)
        reportes = cursor.fetchall()
        cursor.close()
        connection.close()
        return reportes


    def obtener_reporte(id_reporte):
        connection = Database.get_connection()
        if not connection:
            return None
        cursor = connection.cursor(dictionary=True)
        query = """ SELECT * FROM reportes WHERE id_reporte = %s """
        cursor.execute(query, (id_reporte,))
        reporte = cursor.fetchone()
        cursor.close()
        connection.close()
        return reporte

    def crear_reporte(tipo, lugar, prioridad, descripcion):
        connection = Database.get_connection()
        if not connection:
            return False, "Error de conexión"
        try:

            cursor = connection.cursor()
            query = """ INSERT INTO reportes (tipo_incidente, lugar, prioridad, descripcion) VALUES (%s, %s, %s, %s) """
            values = (tipo, lugar, prioridad, descripcion)
            cursor.execute(query, values)
            connection.commit()
            cursor.close()
            connection.close()
            return True, "Reporte enviado correctamente"
        except Exception as err:
            return False, f"Error: {err}"


    def editar_reporte(id_reporte, tipo, lugar, prioridad, descripcion):
        connection = Database.get_connection()
        if not connection:
            return False, "Error de conexión"
        try:
            cursor = connection.cursor()
            query = """ UPDATE reportes SET tipo_incidente = %s, lugar = %s, prioridad = %s, descripcion = %s WHERE id_reporte = %s """
            values = (tipo, lugar, prioridad, descripcion,id_reporte)
            cursor.execute(query, values)
            connection.commit()
            cursor.close()
            connection.close()
            return True, "Reporte actualizado correctamente"
        except Exception as err:
            return False, f"Error: {err}"


    def eliminar_reporte(id_reporte):
        connection = Database.get_connection()
        if not connection:
            return False, "Error de conexión"
        try:
            cursor = connection.cursor()
            query = """ DELETE FROM reportes WHERE id_reporte = %s """
            cursor.execute(query, (id_reporte,))
            connection.commit()
            cursor.close()
            connection.close()
            return True, "Reporte eliminado correctamente"
        except Exception as err:
            return False, f"Error: {err}"