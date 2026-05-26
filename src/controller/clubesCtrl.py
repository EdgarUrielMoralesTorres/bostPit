from models.database import Database
from models.clubesModel import clubesModel

class ClubesCtrl:
    def __init__(self):
        self.model = clubesModel(Database())

    def obtener_clubes():
        connection = Database.get_connection()
        if not connection:
            return []
        cursor = connection.cursor(dictionary=True)
        query = """ SELECT * FROM club """
        cursor.execute(query)
        clubes = cursor.fetchall()
        cursor.close()
        connection.close()
        return clubes


    def obtener_club(id_club):
        connection = Database.get_connection()
        if not connection:
            return None
        cursor = connection.cursor(dictionary=True)
        query = """ SELECT * FROM club WHERE id_club = %s """
        cursor.execute(query, (id_club,))
        club = cursor.fetchone()
        cursor.close()
        connection.close()
        return club


    def crear_club(nombre, descripcion, telefono):
        connection = Database.get_connection()
        if not connection:
            return False, "Error de conexión"
        try:
            cursor = connection.cursor()
            query = """ INSERT INTO club (nombre_club, descripcion, telefono) VALUES (%s, %s, %s) """
            values = (nombre, descripcion, telefono)
            cursor.execute(query, values)
            connection.commit()
            cursor.close()
            connection.close()
            return True, "Club agregado correctamente"
        except Exception as err:
            return False, f"Error: {err}"


    def editar_club(id_club, nombre, descripcion, telefono):
        connection = Database.get_connection()
        if not connection:
            return False, "Error de conexión"
        try:
            cursor = connection.cursor()
            query = """ UPDATE club SET nombre_club = %s, descripcion = %s, telefono = %s WHERE id_club = %s """
            values = (nombre,descripcion,telefono,id_club)
            cursor.execute(query, values)
            connection.commit()
            cursor.close()
            connection.close()
            return True, "Club actualizado correctamente"
        except Exception as err:
            return False, f"Error: {err}"


    def eliminar_club(id_club):
        connection = Database.get_connection()
        if not connection:
            return False, "Error de conexión"
        try:
            cursor = connection.cursor()
            query = """ DELETE FROM club WHERE id_club = %s """
            cursor.execute(query, (id_club,))
            connection.commit()
            cursor.close()
            connection.close()
            return True, "Club eliminado correctamente"
        except Exception as err:
            return False, f"Error: {err}"
