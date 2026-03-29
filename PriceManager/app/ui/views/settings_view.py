"""Vista de ajustes (placeholder)."""

import customtkinter as ctk

from app.ui.views.home_view import BaseView


class SettingsView(BaseView):
    def __init__(self, master: ctk.CTkFrame, **kwargs: object) -> None:
        super().__init__(master, **kwargs)
        ctk.CTkLabel(self, text="Ajustes", font=ctk.CTkFont(size=20, weight="bold")).pack(
            pady=24, anchor="w", padx=24
        )
        ctk.CTkLabel(
            self,
            text="Preferencias de la aplicación (pendiente).",
            text_color=("gray30", "gray70"),
            anchor="w",
        ).pack(anchor="w", padx=24)
