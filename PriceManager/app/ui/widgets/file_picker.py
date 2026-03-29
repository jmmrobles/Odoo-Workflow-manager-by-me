"""Fila con botón para elegir archivo (reutilizable)."""

from collections.abc import Callable
from pathlib import Path
import tkinter.filedialog as filedialog

import customtkinter as ctk

from app.config.constants import DEFAULT_EXCEL_EXTENSIONS


class FilePickerRow(ctk.CTkFrame):
    def __init__(
        self,
        master: ctk.CTkFrame,
        button_text: str = "Explorar…",
        filetypes: list[tuple[str, str]] | None = None,
        on_path_selected: Callable[[Path], None] | None = None,
        **kwargs: object,
    ) -> None:
        super().__init__(master, fg_color="transparent", **kwargs)
        self._on_path_selected = on_path_selected
        self._filetypes = filetypes or [
            ("Excel", " ".join(f"*{e}" for e in DEFAULT_EXCEL_EXTENSIONS)),
            ("Todos", "*.*"),
        ]
        self._path_label = ctk.CTkLabel(self, text="Ningún archivo seleccionado", anchor="w")
        self._path_label.pack(side="left", fill="x", expand=True, padx=(0, 8))
        ctk.CTkButton(self, text=button_text, width=120, command=self._browse).pack(side="right")

    def _browse(self) -> None:
        path = filedialog.askopenfilename(filetypes=self._filetypes)
        if not path:
            return
        p = Path(path)
        self._path_label.configure(text=str(p))
        if self._on_path_selected:
            self._on_path_selected(p)

    def set_path_text(self, text: str) -> None:
        self._path_label.configure(text=text)
