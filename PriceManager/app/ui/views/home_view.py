"""Vista de inicio y clase base para el área de contenido."""

import customtkinter as ctk


class BaseView(ctk.CTkFrame):
    """Contenedor común para todas las pantallas principales."""

    def __init__(self, master: ctk.CTkFrame, **kwargs: object) -> None:
        super().__init__(master, fg_color="transparent", **kwargs)


class HomeView(BaseView):
    def __init__(self, master: ctk.CTkFrame, **kwargs: object) -> None:
        super().__init__(master, **kwargs)
        ctk.CTkLabel(
            self,
            text="Bienvenido",
            font=ctk.CTkFont(size=22, weight="bold"),
        ).pack(pady=(32, 8), anchor="w", padx=24)
        ctk.CTkLabel(
            self,
            text="Usa el menú lateral para ir a Excel, informes o ajustes.",
            text_color=("gray30", "gray70"),
            anchor="w",
        ).pack(anchor="w", padx=24)
