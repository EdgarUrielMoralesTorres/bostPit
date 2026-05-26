from models.objetosModel import ObjetosModel
from models.database import Database


class ObjetosCtrl:
    def __init__(self):
        self.model = ObjetosModel(Database())


    def obtener_objetos(self):
        return self.model.obtener()
    
    def obtener_objeto(self, id_objeto):
        return self.model.obtener_por_id(id_objeto)
    
    def crear_objeto(self,nombre,categoria,lugar,descripcion):
        if nombre.strip() == "":
            return False, "El nombre no puede estar vacío"
        if str(categoria).strip() == "":
            return False, "Seleccione una categoría"
        if lugar.strip() == "":
            return False, "El lugar no puede estar vacío"
        if descripcion.strip() == "":
            return False, "La descripción no puede estar vacía"

        return self.model.crear(nombre,categoria,lugar,descripcion)


    def editar_objeto(self,id_objeto,nombre,categoria,lugar,descripcion):
        if nombre.strip() == "":
            return False, "El nombre no puede estar vacío"
        if lugar.strip() == "":
            return False, "El lugar no puede estar vacío"
        if descripcion.strip() == "":
            return False, "La descripción no puede estar vacía"

        return self.model.editar(id_objeto,nombre,categoria,lugar,descripcion
)

    def eliminar_objeto(self, id_objeto):
        return self.model.eliminar(id_objeto)


    def buscar_objetos(self, nombre):
        if nombre.strip() == "":
            return []
        return self.model.buscar(nombre)