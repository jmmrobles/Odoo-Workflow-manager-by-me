"""Barra superior con título."""

import customtkinter as ctk


class TopBar(ctk.CTkFrame):
    def __init__(self, master: ctk.CTk | ctk.CTkFrame, title: str, **kwargs: object) -> None:
        super().__init__(master, height=48, corner_radius=0, **kwargs)
        self._title = ctk.CTkLabel(self, text=title, font=ctk.CTkFont(size=18, weight="bold"))
        self._title.pack(side="left", padx=16, pady=12)

    def set_title(self, title: str) -> None:
        self._title.configure(text=title)
