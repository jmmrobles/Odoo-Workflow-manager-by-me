"""Vista para seleccionar y leer un archivo Excel."""

from collections.abc import Callable
from pathlib import Path

import customtkinter as ctk

from app.controllers.excel_controller import ExcelController
from app.ui.views.home_view import BaseView
from app.ui.widgets.file_picker import FilePickerRow


class ExcelView(BaseView):
    def __init__(
        self,
        master: ctk.CTkFrame,
        controller: ExcelController | None = None,
        on_status: Callable[[str], None] | None = None,
        **kwargs: object,
    ) -> None:
        super().__init__(master, **kwargs)
        self._controller = controller or ExcelController()
        self._on_status = on_status

        ctk.CTkLabel(
            self,
            text="Archivo Excel",
            font=ctk.CTkFont(size=20, weight="bold"),
        ).pack(pady=(24, 12), anchor="w", padx=24)

        self._info = ctk.CTkLabel(
            self,
            text="Selecciona un archivo .xlsx para cargar la primera hoja.",
            text_color=("gray30", "gray70"),
            anchor="w",
            justify="left",
        )
        self._info.pack(anchor="w", padx=24, pady=(0, 12))

        FilePickerRow(
            self,
            button_text="Seleccionar Excel…",
            on_path_selected=self._on_file_chosen,
        ).pack(fill="x", padx=24, pady=8)

    def _emit_status(self, message: str) -> None:
        if self._on_status:
            self._on_status(message)

    def _on_file_chosen(self, path: Path) -> None:
        self._emit_status(f"Leyendo: {path.name}…")
        df, info, err = self._controller.load_sheet_safe(path)
        if err:
            self._info.configure(text=f"Error: {err}")
            self._emit_status("Error al leer el archivo")
            return
        assert df is not None and info is not None
        rows, cols = df.shape
        sheets = ", ".join(info.sheet_names[:5])
        if len(info.sheet_names) > 5:
            sheets += "…"
        self._info.configure(
            text=f"Hojas: {sheets}\nFilas: {rows} · Columnas: {cols}",
        )
        self._emit_status(f"Excel cargado: {path.name} ({rows}×{cols})")
