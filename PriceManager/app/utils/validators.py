"""Validaciones reutilizables."""

from pathlib import Path

from app.config.constants import DEFAULT_EXCEL_EXTENSIONS


def is_excel_path(path: Path) -> bool:
    return path.suffix.lower() in DEFAULT_EXCEL_EXTENSIONS
