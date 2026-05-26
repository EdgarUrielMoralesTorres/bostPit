import flet as ft

def IncidenciasView(page):
    contenido = ft.Column(spacing=15)

    def tarjeta_incidencia(titulo, lugar, icono):
        return ft.Container(bgcolor=ft.Colors.WHITE,border_radius=20,padding=15,
            content=ft.Row(
                spacing=15,
                controls=[
                    ft.Container(width=70,height=70,bgcolor="#F3F4F6",border_radius=15,alignment=ft.Alignment(0, 0),
                        content=ft.Icon(icono,size=35,color="#FF4D67")),
                    ft.Column(spacing=5,expand=True,

                        controls=[
                            ft.Text(titulo,size=18,weight=ft.FontWeight.BOLD,color="#1F2937"),
                            ft.Text(f"Lugar: {lugar}",size=14,color="#6B7280"
                            )])]))


    def mostrar_reportes(e=None):
        contenido.controls = [
            tarjeta_incidencia("Computadora dañada","Laboratorio 2",ft.Icons.COMPUTER),
            tarjeta_incidencia("Luz fundida","Salón A1",ft.Icons.LIGHTBULB),
            tarjeta_incidencia("Fuga de agua","Baños",ft.Icons.WATER_DROP),
            tarjeta_incidencia("Proyector sin funcionar","Salón C3",ft.Icons.VIDEOCAM),]
        page.update()


    def mostrar_reportar(e=None):
        contenido.controls = [
            ft.TextField(label="Tipo de incidencia",border_radius=15,filled=True,bgcolor=ft.Colors.WHITE),
            ft.Dropdown(label="Categoría",border_radius=15,filled=True,bgcolor=ft.Colors.WHITE,
                options=[
                    ft.dropdown.Option("Tecnología"),
                    ft.dropdown.Option("Electricidad"),
                    ft.dropdown.Option("Agua"),
                    ft.dropdown.Option("Mobiliario"),
                    ft.dropdown.Option("Limpieza"),
                ]),

            ft.TextField(label="Lugar",border_radius=15,filled=True,bgcolor=ft.Colors.WHITE),
            ft.Dropdown(label="Prioridad",border_radius=15,filled=True,bgcolor=ft.Colors.WHITE,
                options=[
                    ft.dropdown.Option("Baja"),
                    ft.dropdown.Option("Media"),
                    ft.dropdown.Option("Alta"),
                ]),

            ft.TextField(label="Descripción",multiline=True,min_lines=4,max_lines=6,border_radius=15,filled=True,bgcolor=ft.Colors.WHITE),
            ft.Container(height=55,bgcolor="#FF4D67",border_radius=15,alignment=ft.Alignment(0, 0),
                content=ft.Text("Enviar Reporte",color=ft.Colors.WHITE,size=16,weight=ft.FontWeight.BOLD
                ))]
        page.update()


    mostrar_reportes()
    botones = ft.Row(
        spacing=10,
        controls=[

            ft.ElevatedButton("Ver Reportes",bgcolor="#FF4D67",color=ft.Colors.WHITE,on_click=mostrar_reportes),
            ft.ElevatedButton("Reportar",bgcolor="#1F2937",color=ft.Colors.WHITE,on_click=mostrar_reportar),
        ])


    return ft.View(
        route="/incidencias",
        bgcolor="#F8F8F8",
        controls=[
            ft.SafeArea(

                content=ft.Container(expand=True,padding=20,
                    content=ft.Column(scroll=ft.ScrollMode.AUTO,expand=True,spacing=20,
                        controls=[

                            ft.IconButton(
                                icon=ft.Icons.ARROW_BACK,
                                icon_color="#1F2937",
                                icon_size=28,
                                on_click=lambda e: page.go("/")
                            ),

                            ft.Text(
                                "Reporte de Incidencias",
                                size=30,
                                weight=ft.FontWeight.BOLD,
                                color="#1F2937"
                            ),
                            botones,
                            contenido
                        ])))])