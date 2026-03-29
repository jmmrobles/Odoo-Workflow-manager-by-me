"""Barra de estado inferior."""

import customtkinter as ctk


class StatusBar(ctk.CTkFrame):
    def __init__(self, master: ctk.CTkFrame, **kwargs: object) -> None:
        super().__init__(master, height=28, corner_radius=0, **kwargs)
        self._label = ctk.CTkLabel(self, text="Listo", anchor="w", font=ctk.CTkFont(size=12))
        self._label.pack(fill="x", padx=12, pady=4)

    def set_message(self, message: str) -> None:
        self._label.configure(text=message)
