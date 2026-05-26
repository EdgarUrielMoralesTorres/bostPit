from models.sugerenciasModel import SugerenciasModel
from models.database import Database


class SugerenciasCtrl:
    def __init__(self):
        self.model = SugerenciasModel(Database())


    def obtener_sugerencias(self):
        return self.model.obtener()


    def obtener_sugerencia(self, id_sugerencia):
        return self.model.obtener_por_id(id_sugerencia)


    def crear_sugerencia(self,tipo,titulo,descripcion):

        if str(tipo).strip() == "":
            return False, "Seleccione un tipo"
        if titulo.strip() == "":
            return False, "El título no puede estar vacío"
        if descripcion.strip() == "":
            return False, "La descripción no puede estar vacía"

        return self.model.crear(tipo,titulo,descripcion)


    def editar_sugerencia(self,id_sugerencia,tipo,titulo,descripcion):


        if titulo.strip() == "":
            return False, "El título no puede estar vacío"
        if descripcion.strip() == "":
            return False, "La descripción no puede estar vacía"
        return self.model.editar(id_sugerencia, tipo,titulo,descripcion)


    def eliminar_sugerencia(self, id_sugerencia):
        return self.model.eliminar(id_sugerencia)


    def buscar_sugerencias(self, titulo):
        if titulo.strip() == "":
            return []
        return self.model.buscar(titulo)