import flet as ft

def ObjetosView(page):
    contenido = ft.Column(spacing=15)
    
    def tarjeta_objeto(nombre, lugar, icono):
        return ft.Container(
            bgcolor=ft.Colors.WHITE,
            border_radius=20,
            padding=15,

            content=ft.Row(
                spacing=15,
                controls=[
                    ft.Container(width=70,height=70,bgcolor="#F3F4F6",border_radius=15,alignment=ft.Alignment(0, 0),
                        content=ft.Icon(icono,size=35,color="#FF4D67")),

                    ft.Column(spacing=5,expand=True,
                        controls=[

                            ft.Text(nombre,size=18,weight=ft.FontWeight.BOLD,color="#1F2937"),
                            ft.Text(f"Encontrado en: {lugar}",size=14,color="#6B7280"
                            )])]))


    def mostrar_objetos(e=None):
        contenido.controls = [
            tarjeta_objeto("iPhone 13","Cafetería",ft.Icons.PHONE_IPHONE),
            tarjeta_objeto("Mochila Negra","Salón B2",ft.Icons.BACKPACK),
            tarjeta_objeto("Cartera","Patio principal",ft.Icons.ACCOUNT_BALANCE_WALLET),
            tarjeta_objeto("Audífonos","Biblioteca",ft.Icons.HEADPHONES),]
        page.update()


    def mostrar_reportar(e=None):
        contenido.controls = [
            ft.TextField(label="Nombre del objeto",border_radius=15,filled=True,bgcolor=ft.Colors.WHITE),
            ft.Dropdown(label="Categoría",border_radius=15,filled=True,bgcolor=ft.Colors.WHITE,
                options=[
                    ft.dropdown.Option("Tecnología"),
                    ft.dropdown.Option("Útiles"),
                    ft.dropdown.Option("Dinero"),
                    ft.dropdown.Option("Ropa"),
                    ft.dropdown.Option("Otros"),
                ]),

            ft.TextField(label="Lugar encontrado",border_radius=15,filled=True,bgcolor=ft.Colors.WHITE),
            ft.TextField(label="Descripción",multiline=True,min_lines=4,max_lines=6,border_radius=15,filled=True,bgcolor=ft.Colors.WHITE),
            ft.Container(height=55,bgcolor="#FF4D67",border_radius=15,alignment=ft.Alignment(0, 0),
                content=ft.Text("Publicar Objeto",color=ft.Colors.WHITE,size=16,weight=ft.FontWeight.BOLD))]
        page.update()


    mostrar_objetos()
    botones = ft.Row(spacing=10,
        controls=[
            ft.ElevatedButton("Ver Objetos",bgcolor="#FF4D67",color=ft.Colors.WHITE,on_click=mostrar_objetos),
            ft.ElevatedButton("Reportar",bgcolor="#1F2937",color=ft.Colors.WHITE,on_click=mostrar_reportar
            ),])


    return ft.View(
        route="/objetos",
        bgcolor="#F8F8F8",
        controls=[
            ft.SafeArea(

                content=ft.Container(
                    expand=True,
                    padding=20,

                    content=ft.Column(
                        scroll=ft.ScrollMode.AUTO,
                        expand=True,
                        spacing=20,

                        controls=[

                            ft.IconButton(
                                icon=ft.Icons.ARROW_BACK,
                                icon_color="#1F2937",
                                icon_size=28,
                                on_click=lambda e: page.go("/")
                            ),
                            ft.Text(
                                "Objetos Perdidos",
                                size=30,
                                weight=ft.FontWeight.BOLD,
                                color="#1F2937"
                            ),
                            botones,
                            contenido
                        ]
                    )
                )
            )
        ]
    )