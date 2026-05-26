from models.tiendaModel import TiendaModel
from models.database import Database


class TiendaCtrl:
    def __init__(self):
        self.model = TiendaModel(Database())


    def obtener_productos(self):
        return self.model.obtener()


    def obtener_producto(self, id_producto):
        return self.model.obtener_por_id(id_producto)


    def crear_producto(self,nombre,descripcion,foto,precio):
        if nombre.strip() == "":
            return False, "El nombre no puede estar vacío"
        if descripcion.strip() == "":
            return False, "La descripción no puede estar vacía"
        if str(precio).strip() == "":
            return False, "El precio no puede estar vacío"
        try:
            precio = float(precio)
            if precio <= 0:
                return False, "El precio debe ser mayor a 0"
        except:
            return False, "Precio inválido"


        return self.model.crear(nombre,descripcion,foto,precio)


    def editar_producto(self,id_producto,nombre,descripcion,foto,precio):
        if nombre.strip() == "":
            return False, "El nombre no puede estar vacío"
        if descripcion.strip() == "":
            return False, "La descripción no puede estar vacía"
        try:
            precio = float(precio)
            if precio <= 0:
                return False, "El precio debe ser mayor a 0"
        except:
            return False, "Precio inválido"
        return self.model.editar(id_producto,nombre,descripcion,foto,precio)


    def eliminar_producto(self, id_producto):
        return self.model.eliminar(id_producto)


    def buscar_productos(self, nombre):
        if nombre.strip() == "":
            return []
        return self.model.buscar(nombre)


    def calcular_total(self, carrito):
        """
        carrito:
        [
            {"precio": 50, "cantidad": 2},
            {"precio": 20, "cantidad": 1}
        ]
        """
        total = 0
        for producto in carrito:
            total += producto["precio"] * producto["cantidad"]
        return total