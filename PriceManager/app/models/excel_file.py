"""Metadatos sobre un archivo Excel cargado."""

from dataclasses import dataclass
from pathlib import Path


@dataclass
class ExcelFileInfo:
    path: Path
    sheet_names: tuple[str, ...] = ()
