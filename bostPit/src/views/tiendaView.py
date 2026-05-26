import flet as ft

def PedidosView(page):
    def tarjeta_producto(nombre, icono, precio):
        return ft.Container(width=170,height=240,bgcolor=ft.Colors.WHITE,border_radius=20,padding=15,
            content=ft.Column(spacing=10,horizontal_alignment=ft.CrossAxisAlignment.START,
                controls=[
                    ft.Container(width=140,height=100,bgcolor="#F3F4F6",border_radius=15,alignment=ft.Alignment(0, 0),
                        content=ft.Icon(icono,size=55,color="#FF4D67")
                    ),

                    ft.Text(nombre,size=18,weight=ft.FontWeight.BOLD,color="#1F2937"),


                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text(precio,size=16,weight=ft.FontWeight.BOLD,color="#FF4D67"
                            ),])]))


    header = ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        scroll=ft.ScrollMode.AUTO,
        controls=[
            ft.Column(
                spacing=2,
                controls=[
                    ft.Text(
                        "Tiendita",
                        size=32,
                        weight=ft.FontWeight.BOLD,
                        color="#1F2937",
                        font_family="Georgia"
                    ),]),

            ft.Container(width=50,height=50,bgcolor="#F3F4F6",border_radius=15,alignment=ft.Alignment(0, 0),
                content=ft.Icon(ft.Icons.PERSON,color="#1F2937"))])


    
    buscador = ft.TextField(
    hint_text="Buscar comida...",
    prefix_icon=ft.Icons.SEARCH,
    border_radius=18,
    filled=True,
    bgcolor=ft.Colors.WHITE,
    height=55,
    text_style=ft.TextStyle(size=15))
    
    productos = ft.Column(
    spacing=15,
    controls=[
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=15,
            controls=[
                tarjeta_producto("Hamburguesa", ft.Icons.LUNCH_DINING, "$50"),
                tarjeta_producto("Pizza", ft.Icons.LOCAL_PIZZA, "$40"),
            ]
        ),
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=15,
            controls=[
                tarjeta_producto("Refresco", ft.Icons.LOCAL_DRINK, "$20"),
                tarjeta_producto("Café", ft.Icons.LOCAL_CAFE, "$35"),
            ]
        ),
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=15,
            controls=[
                tarjeta_producto("Papas", ft.Icons.FASTFOOD, "$30"),
                tarjeta_producto("Galletas", ft.Icons.COOKIE, "$25"),
            ]
        ),
    ]
)
    return ft.View(
        route="/pedidos",
        bgcolor="#F8F8F8",
        controls=[
            ft.SafeArea(
                content=ft.Container(
                    expand=True,
                    padding=20,
                    
                    content=ft.Column(
                        scroll=ft.ScrollMode.AUTO,
                        expand=True,
                        controls=[
                            ft.IconButton(icon=ft.Icons.ARROW_BACK,icon_size=28,on_click=lambda e: page.go("/")),
                            header,
                            ft.Container(height=20),
                            buscador,
                            ft.Container(height=20),
                            ft.Container(height=20),
                            productos,
                        ]
                    )
                )
            )
        ]
    )