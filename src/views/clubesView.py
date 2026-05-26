import flet as ft


def ClubesView(page):


    def tarjeta_club(nombre, descripcion, icono):

        return ft.Container(
            bgcolor=ft.Colors.WHITE,
            border_radius=20,
            padding=20,

            content=ft.Row(
                spacing=15,

                controls=[

                    ft.Container(
                        width=70,
                        height=70,
                        bgcolor="#F3F4F6",
                        border_radius=15,
                        alignment=ft.Alignment(0, 0),

                        content=ft.Icon(
                            icono,
                            size=35,
                            color="#FF4D67"
                        )
                    ),

                    # INFORMACION
                    ft.Column(
                        spacing=5,
                        expand=True,

                        controls=[

                            ft.Text(
                                nombre,
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                color="#1F2937"
                            ),

                            ft.Text(
                                descripcion,
                                size=14,
                                color="#6B7280"
                            )
                        ]
                    )
                ]
            )
        )

    # ---------- LISTA CLUBES ----------

    clubes = ft.Column(
        spacing=15,

        controls=[

            tarjeta_club(
                "Club de Programación",
                "Aprende programación y desarrolla proyectos.",
                ft.Icons.COMPUTER
            ),

            tarjeta_club(
                "Club de Música",
                "Participa en actividades musicales y eventos.",
                ft.Icons.MUSIC_NOTE
            ),

            tarjeta_club(
                "Club de Deportes",
                "Entrenamientos y torneos deportivos.",
                ft.Icons.SPORTS_SOCCER
            ),

            tarjeta_club(
                "Club de Arte",
                "Dibujo, pintura y creatividad artística.",
                ft.Icons.PALETTE
            ),

            tarjeta_club(
                "Club de Robótica",
                "Construcción y programación de robots.",
                ft.Icons.PRECISION_MANUFACTURING
            ),
        ]
    )

    # ---------- VISTA ----------

    return ft.View(
        route="/clubes",
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

                            # BOTON VOLVER
                            ft.IconButton(
                                icon=ft.Icons.ARROW_BACK,
                                icon_color="#1F2937",
                                icon_size=28,
                                on_click=lambda e: page.go("/")
                            ),

                            # TITULO
                            ft.Text(
                                "Clubes Escolares",
                                size=30,
                                weight=ft.FontWeight.BOLD,
                                color="#1F2937"
                            ),

                            # DESCRIPCION
                            ft.Text(
                                "Explora los clubes disponibles en la escuela.",
                                size=15,
                                color="#6B7280"
                            ),

                            # CLUBES
                            clubes
                        ]
                    )
                )
            )
        ]
    )