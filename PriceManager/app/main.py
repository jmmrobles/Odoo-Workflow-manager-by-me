"""Arranque de la aplicación y configuración global de CustomTkinter."""

import customtkinter as ctk

from app.config import settings
from app.ui.app_window import AppWindow


def run_app() -> None:
    ctk.set_appearance_mode(settings.APPEARANCE_MODE)
    ctk.set_default_color_theme(settings.COLOR_THEME)
    app = AppWindow()
    app.mainloop()
