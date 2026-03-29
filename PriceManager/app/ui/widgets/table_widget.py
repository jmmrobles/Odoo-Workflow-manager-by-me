"""Tabla de datos (placeholder; se puede sustituir por CTkScrollableFrame + grid)."""

import customtkinter as ctk


class TableWidget(ctk.CTkFrame):
    """Contenedor reservado para mostrar filas/columnas de un DataFrame."""

    def __init__(self, master: ctk.CTkFrame, **kwargs: object) -> None:
        super().__init__(master, **kwargs)
        self._placeholder = ctk.CTkLabel(self, text="(Tabla — pendiente de implementar)")
        self._placeholder.pack(pady=24)
