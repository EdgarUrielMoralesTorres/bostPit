from models.database import Database
from models.tiendaModel import tiendaModel

class TiendaCtrl:
    def __init__(self):
        self.model = tiendaModel(Database())
            
    def obtener_comidas():
        connection = Database.get_connection()
        if not connection:
            return []
        cursor = connection.cursor(dictionary=True)
        query = """ SELECT * FROM tienda """
        cursor.execute(query)
        comidas = cursor.fetchall()
        cursor.close()
        connection.close()
        return comidas

    def obtener_comida(id_comida):
        connection = Database.get_connection()
        if not connection:
            return None
        cursor = connection.cursor(dictionary=True)
        query = """ SELECT * FROM tienda WHERE id_tienda = %s """
        cursor.execute(query, (id_comida,))
        comida = cursor.fetchone()
        cursor.close()
        connection.close()
        return comida

    def agregar_comida(nombre, descripcion, foto, precio):
        connection = Database.get_connection()
        if not connection:
            return False, "Error de conexión"

        try:
            cursor = connection.cursor()
            query = """ INSERT INTO tienda (nombre_comida, descripcion, foto_comida, precio) VALUES (%s, %s, %s, %s) """
            values = (nombre,descripcion,foto,precio)
            cursor.execute(query, values)
            connection.commit()
            cursor.close()
            connection.close()
            return True, "Comida agregada correctamente"

        except Exception as err:
            return False, f"Error: {err}"


    def editar_comida(id_comida, nombre, descripcion, foto, precio):
        connection = Database.get_connection()
        if not connection:
            return False, "Error de conexión"
        try:
            cursor = connection.cursor()

            query = """ UPDATE tienda SET nombre_comida = %s, descripcion = %s, foto_comida = %s, precio = %s WHERE id_tienda = %s """
            values = (nombre, descripcion,foto,precio,id_comida)
            cursor.execute(query, values)
            connection.commit()
            cursor.close()
            connection.close()
            return True, "Comida actualizada correctamente"

        except Exception as err:
            return False, f"Error: {err}"


    def eliminar_comida(id_comida):
        connection = Database.get_connection()
        if not connection:
            return False, "Error de conexión"
        try:
            cursor = connection.cursor()
            query = """ DELETE FROM tienda WHERE id_tienda = %s """
            cursor.execute(query, (id_comida,))
            connection.commit()
            cursor.close()
            connection.close()
            return True, "Comida eliminada correctamente"

        except Exception as err:
            return False, f"Error: {err}"


    def buscar_comida(nombre):
        connection = Database.get_connection()
        if not connection:
            return []
        cursor = connection.cursor(dictionary=True)
        query = """ SELECT * FROM tienda WHERE nombre_comida LIKE %s """
        cursor.execute(query, (f"%{nombre}%",))
        comidas = cursor.fetchall()
        cursor.close()
        connection.close()

        return comidas