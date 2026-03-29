"""Vista de informes (placeholder)."""

import customtkinter as ctk

from app.ui.views.home_view import BaseView


class ReportView(BaseView):
    def __init__(self, master: ctk.CTkFrame, **kwargs: object) -> None:
        super().__init__(master, **kwargs)
        ctk.CTkLabel(self, text="Informes", font=ctk.CTkFont(size=20, weight="bold")).pack(
            pady=24, anchor="w", padx=24
        )
        ctk.CTkLabel(
            self,
            text="Aquí irá la generación y vista previa de informes.",
            text_color=("gray30", "gray70"),
            anchor="w",
        ).pack(anchor="w", padx=24)
