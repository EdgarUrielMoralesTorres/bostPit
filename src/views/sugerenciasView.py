import flet as ft


def SugerenciasView(page):
    contenido = ft.Column(spacing=15)


    def tarjeta_publicacion(tipo, titulo, descripcion, color, icono):
        return ft.Container(bgcolor=ft.Colors.WHITE,border_radius=20,padding=15,
            content=ft.Column(spacing=10,
                controls=[
                    ft.Row(
                        controls=[
                            ft.Container(padding=10,bgcolor=color,border_radius=12,
                                content=ft.Row(spacing=5,
                                    controls=[
                                        ft.Icon(icono,color=ft.Colors.WHITE,size=18
                                        ),
                                        ft.Text(tipo,color=ft.Colors.WHITE,weight=ft.FontWeight.BOLD
                                        )]))]),
                    ft.Text(titulo,size=20,weight=ft.FontWeight.BOLD,color="#1F2937"),
                    ft.Text(descripcion,size=14,color="#6B7280")]))


    def mostrar_publicaciones(e=None):
        contenido.controls = [
            tarjeta_publicacion("Sugerencia","Más enchufes en biblioteca","Sería útil agregar más conexiones para laptops.","#22C55E",ft.Icons.LIGHTBULB),
            tarjeta_publicacion("Queja","Baños sucios","Los baños del edificio B necesitan limpieza constante.","#EF4444",ft.Icons.WARNING),
            tarjeta_publicacion("Felicitación","Buen evento deportivo","El torneo estuvo muy bien organizado.","#3B82F6",ft.Icons.STAR),]
        page.update()


    def mostrar_formulario(e=None):
        contenido.controls = [
            ft.Dropdown(label="Tipo",border_radius=15,filled=True,bgcolor=ft.Colors.WHITE,
                options=[
                    ft.dropdown.Option("Sugerencia"),
                    ft.dropdown.Option("Queja"),
                    ft.dropdown.Option("Felicitación"),
                ]),
            
            ft.TextField(label="Título",border_radius=15,filled=True,bgcolor=ft.Colors.WHITE),
            ft.TextField(label="Descripción",multiline=True,min_lines=5,max_lines=7,border_radius=15,filled=True,bgcolor=ft.Colors.WHITE),
            ft.Container(height=55,bgcolor="#FF4D67",border_radius=15,alignment=ft.Alignment(0, 0),ink=True,
                content=ft.Text(
                    "Enviar",
                    color=ft.Colors.WHITE,
                    size=16,
                    weight=ft.FontWeight.BOLD
                ))]
        page.update()

    mostrar_publicaciones()
    botones = ft.Row(
        spacing=10,
        controls=[
            ft.ElevatedButton("Ver Publicaciones",bgcolor="#FF4D67",color=ft.Colors.WHITE,on_click=mostrar_publicaciones),
            ft.ElevatedButton("Enviar",bgcolor="#1F2937",color=ft.Colors.WHITE,on_click=mostrar_formulario),])

    return ft.View(route="/sugerencias",bgcolor="#F8F8F8",
        controls=[
            ft.SafeArea(
                content=ft.Container(expand=True,padding=20,
                    content=ft.Column(scroll=ft.ScrollMode.AUTO,expand=True,spacing=20,
                        controls=[
                            ft.IconButton(icon=ft.Icons.ARROW_BACK,icon_color="#1F2937",icon_size=28,on_click=lambda e: page.go("/")),
                            ft.Text("Sugerencias y Quejas",size=30,weight=ft.FontWeight.BOLD,color="#1F2937"),
                            ft.Text("Comparte tus ideas, opiniones o reportes.",size=15,color="#6B7280"
                            ),
                            botones,
                            contenido
                        ])))])