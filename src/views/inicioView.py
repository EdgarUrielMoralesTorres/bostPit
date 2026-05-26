import flet as ft


def inicioView(page):
    titulo = ft.Text("titulo",size=45,weight=ft.FontWeight.BOLD,color="#192538",)
    bienvenida = ft.Text("Bienvenido de nuevo",size=20,color="#344358",)
    perfil = ft.Container(width=140,height=140,bgcolor=ft.Colors.GREY_200,border_radius=100,alignment=ft.Alignment(0, 0),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Icon(ft.Icons.PERSON,size=45,color="#000000"),
                ft.Text("Perfil",size=15,weight=ft.FontWeight.W_600,color="#334155",
                )]))
    pedidos = ft.Container(width=190,height=190,bgcolor="#60A5FA",border_radius=20,padding=20,ink=True,on_click=lambda e: page.go("/pedidos"),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Icon(ft.Icons.SHOPPING_CART,size=50,color=ft.Colors.WHITE),
                ft.Text("Pedidos",size=20,weight=ft.FontWeight.BOLD,color=ft.Colors.WHITE
                )]))
    objetos = ft.Container(width=190,height=190,bgcolor="#A78BFA",border_radius=20,padding=20,ink=True,on_click=lambda e: page.go("/objetos"),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Icon(ft.Icons.SEARCH,size=50,color=ft.Colors.WHITE),
                ft.Text("Objetos",size=20,weight=ft.FontWeight.BOLD,color=ft.Colors.WHITE
                )]))
    sugerencias = ft.Container(width=190,height=190,bgcolor="#34D399",border_radius=20,padding=20,ink=True,on_click=lambda e: page.go("/sugerencias"),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Icon(ft.Icons.GROUP,size=50,color=ft.Colors.WHITE),
                ft.Text("Sugerencias",size=20,weight=ft.FontWeight.BOLD,color=ft.Colors.WHITE)]))
    incidencias = ft.Container(width=190,height=190,bgcolor="#FBBF24",border_radius=20,padding=20,ink=True,on_click=lambda e: page.go("/incidencias"),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Icon(ft.Icons.WARNING_AMBER,size=50,color=ft.Colors.WHITE),
                ft.Text("Incidencias",size=20,weight=ft.FontWeight.BOLD,color=ft.Colors.WHITE)]))

    return ft.View(
        route="/",
        bgcolor="#E5E7EB",
        controls=[
            ft.Container(expand=True,padding=20,
                content=ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=20,
                    controls=[
                        ft.Container(height=20),
                        titulo,
                        bienvenida,
                        ft.Container(height=20),

                        ft.Stack(
                            alignment=ft.Alignment(0, 0),
                            controls=[
                                ft.Column(spacing=15,
                                    controls=[
                                        ft.Row(alignment=ft.MainAxisAlignment.CENTER,spacing=15,
                                            controls=[
                                                pedidos,
                                                objetos,
                                            ]),
                                        ft.Row(alignment=ft.MainAxisAlignment.CENTER,spacing=15,
                                            controls=[
                                                sugerencias,
                                                incidencias,
                                            ]),
                                        ]),
                                ft.Container(alignment=ft.Alignment(0, 0),
                                    content=perfil
                                )])]))])