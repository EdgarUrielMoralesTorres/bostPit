from models.database import Database
from models.tiendaModel import tiendaModel

class ObjetosCtrl:
    def __init__(self):
        self.model = tiendaModel(Database())

    def obtener_objetos():
        connection = Database.get_connection()
        if not connection:
            return []
        cursor = connection.cursor(dictionary=True)
        query = """ SELECT * FROM objetos """
        cursor.execute(query)
        objetos = cursor.fetchall()
        cursor.close()
        connection.close()
        return objetos


    def obtener_objeto(id_objeto):
        connection = Database.get_connection()
        if not connection:
            return None
        cursor = connection.cursor(dictionary=True)
        query = """ SELECT * FROM objetos WHERE id_objetos = %s """
        cursor.execute(query, (id_objeto,))
        objeto = cursor.fetchone()
        cursor.close()
        connection.close()
        return objeto


    def crear_objeto(nombre, categoria, lugar, descripcion):
        connection = Database.get_connection()
        if not connection:
            return False, "Error de conexión"
        try:
            cursor = connection.cursor()
            query = """ INSERT INTO objetos (nombre_objeto, categoria, lugar, descripcion) VALUES (%s, %s, %s, %s) """
            values = (nombre, categoria, lugar, descripcion)
            cursor.execute(query, values)
            connection.commit()
            cursor.close()
            connection.close()
            return True, "Objeto publicado correctamente"
        except Exception as err:
            return False, f"Error: {err}"


    def editar_objeto(id_objeto, nombre, categoria, lugar, descripcion):
        connection = Database.get_connection()
        if not connection:
            return False, "Error de conexión"
        try:
            cursor = connection.cursor()
            query = """ UPDATE objetos SET nombre_objeto = %s, categoria = %s, lugar = %s, descripcion = %s WHERE id_objetos = %s """
            values = (nombre,categoria,lugar,descripcion,id_objeto)
            cursor.execute(query, values)
            connection.commit()
            cursor.close()
            connection.close()
            return True, "Objeto actualizado correctamente"
        except Exception as err:
            return False, f"Error: {err}"


    def eliminar_objeto(id_objeto):
        connection = Database.get_connection()
        if not connection:
            return False, "Error de conexión"
        try:
            cursor = connection.cursor()
            query = """ DELETE FROM objetos WHERE id_objetos = %s """
            cursor.execute(query, (id_objeto,))
            connection.commit()
            cursor.close()
            connection.close()
            return True, "Objeto eliminado correctamente"
        except Exception as err:
            return False, f"Error: {err}"

    def buscar_objetos(nombre):
        connection = Database.get_connection()
        if not connection:
            return []
        cursor = connection.cursor(dictionary=True)
        query = """ SELECT * FROM objetos WHERE nombre_objeto LIKE %s """
        cursor.execute(query, (f"%{nombre}%",))
        objetos = cursor.fetchall()
        cursor.close()
        connection.close()

        return objetos