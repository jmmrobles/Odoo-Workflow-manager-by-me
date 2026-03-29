"""Operaciones de archivos genéricas (placeholder)."""

from pathlib import Path


def path_exists(path: Path | str) -> bool:
    return Path(path).is_file()
