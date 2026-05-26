from models.incidenciasModel import IncidenciasModel
from models.database import Database


class IncidenciasCtrl:
    def __init__(self):
        self.model = IncidenciasModel(Database())


    def obtener_reportes(self):
        return self.model.obtener()


    def obtener_reporte(self, id_reporte):
        return self.model.obtener_por_id(id_reporte)


    def crear_reporte(self,tipo,lugar,prioridad,descripcion):
        if str(tipo).strip() == "":
            return False, "Seleccione un tipo"

        if lugar.strip() == "":
            return False, "El lugar no puede estar vacío"

        if str(prioridad).strip() == "":
            return False, "Seleccione una prioridad"

        if descripcion.strip() == "":
            return False, "La descripción no puede estar vacía"


        return self.model.crear(tipo,lugar,prioridad,descripcion)


    def editar_reporte(self,id_reporte,tipo,lugar,prioridad,descripcion):
        if lugar.strip() == "":
            return False, "El lugar no puede estar vacío"
        if descripcion.strip() == "":
            return False, "La descripción no puede estar vacía"
        return self.model.editar(id_reporte,tipo,lugar,prioridad,descripcion)


    def eliminar_reporte(self, id_reporte):
        return self.model.eliminar(id_reporte)