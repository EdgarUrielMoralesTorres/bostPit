import flet as ft

from views.inicioView import inicioView
from views.tiendaView import PedidosView
from views.objetosView import ObjetosView
from views.sugerenciasView import SugerenciasView
from views.incidenciasView import IncidenciasView


def start(page: ft.Page):

    page.title = "Organizador Escolar"

    def route_change(route):

        page.views.clear()

        if page.route == "/":
            page.views.append(inicioView(page))

        elif page.route == "/pedidos":
            page.views.append(PedidosView(page))

        elif page.route == "/objetos":
            page.views.append(ObjetosView(page))

        elif page.route == "/sugerencias":
            page.views.append(SugerenciasView(page))

        elif page.route == "/incidencias":
            page.views.append(IncidenciasView(page))

        page.update()



    page.on_route_change = route_change

    page.go("/")
    route_change(page.route)

def main():
    ft.app(target=start)


if __name__ == "__main__":
    main()