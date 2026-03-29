"""Ventana principal: layout, navegación y área de vistas."""

import customtkinter as ctk

from app.config.constants import APP_TITLE, WINDOW_MIN_SIZE
from app.ui.navigation.sidebar import Sidebar
from app.ui.navigation.topbar import TopBar
from app.ui.views.excel_view import ExcelView
from app.ui.views.home_view import HomeView
from app.ui.views.report_view import ReportView
from app.ui.views.settings_view import SettingsView
from app.ui.widgets.status_bar import StatusBar
from app.utils.paths import ensure_data_dirs


class AppWindow(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        ensure_data_dirs()
        self.title(APP_TITLE)
        self.minsize(*WINDOW_MIN_SIZE)
        self.geometry("1000x640")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self._top = TopBar(self, title=APP_TITLE)
        self._top.grid(row=0, column=0, columnspan=2, sticky="ew")

        self._sidebar = Sidebar(self, on_navigate=self._show_view)
        self._sidebar.grid(row=1, column=0, sticky="nsew")

        self._content = ctk.CTkFrame(self, fg_color="transparent")
        self._content.grid(row=1, column=1, sticky="nsew", padx=0, pady=0)
        self._content.grid_columnconfigure(0, weight=1)
        self._content.grid_rowconfigure(0, weight=1)

        self._status = StatusBar(self)
        self._status.grid(row=2, column=0, columnspan=2, sticky="ew")

        self._current_view: ctk.CTkFrame | None = None
        self._show_view("home")

    def _clear_content(self) -> None:
        if self._current_view is not None:
            self._current_view.destroy()
            self._current_view = None

    def _show_view(self, name: str) -> None:
        self._clear_content()
        titles = {
            "home": "Inicio",
            "excel": "Excel",
            "report": "Informes",
            "settings": "Ajustes",
        }
        self._top.set_title(f"{APP_TITLE} — {titles.get(name, name)}")

        if name == "home":
            self._current_view = HomeView(self._content)
        elif name == "excel":
            self._current_view = ExcelView(
                self._content,
                on_status=self._status.set_message,
            )
        elif name == "report":
            self._current_view = ReportView(self._content)
        elif name == "settings":
            self._current_view = SettingsView(self._content)
        else:
            self._current_view = HomeView(self._content)

        self._current_view.grid(row=0, column=0, sticky="nsew")
        self._status.set_message("Listo")
