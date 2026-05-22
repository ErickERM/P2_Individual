import flet as ft


class DiabetesView:

    def __init__(self, page: ft.Page):

        self.page = page

        # CONFIGURACIÓN
        self.page.title = (
            "Análisis Dataset Diabetes"
        )

        self.page.window_width = 800
        self.page.window_height = 700
        self.page.padding = 30

        self.page.scroll = ft.ScrollMode.AUTO

        # BOTONES
        self.btn_estadisticas = (
            ft.ElevatedButton(
                "Mostrar estadísticas",
                color="white",
                bgcolor="blue"
            )
        )

        self.btn_riesgo = (
            ft.ElevatedButton(
                "Pacientes de riesgo",
                color="white",
                bgcolor="red"
            )
        )


        # RESULTADOS
        self.resultado = ft.Text(
            size=16,
            theme_style=ft.TextThemeStyle.BODY_LARGE,
            selectable=True
        )

        self.tabla = ft.ListView(
            expand=True,
            spacing=15,
            padding=10
        )

    # CONSTRUIR INTERFAZ
    def construir(self):

        return ft.Column(

            controls=[

                ft.Text(
                    "Sistema de Análisis Diabetes",
                    size=30,
                    weight="bold"
                ),

                ft.Divider(),

                ft.Row(

                    controls=[
                        self.btn_estadisticas,
                        self.btn_riesgo
                    ]

                ),

                ft.Divider(),

                self.resultado,

                self.tabla

            ],

            spacing=20

        )

    # LIMPIAR TABLA
    def limpiar_tabla(self):

        self.tabla.controls.clear()
