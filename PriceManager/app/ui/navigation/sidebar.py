"""Barra lateral de navegación entre vistas."""

from collections.abc import Callable

import customtkinter as ctk


class Sidebar(ctk.CTkFrame):
    def __init__(
        self,
        master: ctk.CTk | ctk.CTkFrame,
        on_navigate: Callable[[str], None],
        **kwargs: object,
    ) -> None:
        super().__init__(master, width=200, corner_radius=0, **kwargs)
        self._on_navigate = on_navigate

        ctk.CTkLabel(self, text="Secciones", font=ctk.CTkFont(size=14, weight="bold")).pack(
            pady=(16, 8), padx=16, anchor="w"
        )
        for key, label in (
            ("home", "Inicio"),
            ("excel", "Excel"),
            ("report", "Informes"),
            ("settings", "Ajustes"),
        ):
            ctk.CTkButton(
                self,
                text=label,
                anchor="w",
                fg_color="transparent",
                text_color=("gray10", "gray90"),
                hover_color=("gray70", "gray30"),
                command=lambda k=key: self._on_navigate(k),
            ).pack(fill="x", padx=8, pady=4)
