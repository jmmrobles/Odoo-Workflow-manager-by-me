"""Lectura y procesamiento de archivos Excel con pandas."""

from pathlib import Path

import pandas as pd

from app.models.excel_file import ExcelFileInfo
from app.utils.validators import is_excel_path


def read_excel_file(
    path: Path | str,
    sheet_name: str | int | None = 0,
    **kwargs: object,
) -> tuple[pd.DataFrame, ExcelFileInfo]:
    """
    Lee un Excel y devuelve el DataFrame de la hoja indicada y metadatos básicos.

    kwargs se reenvían a pandas.read_excel cuando aplica.
    """
    p = Path(path)
    if not p.is_file():
        raise FileNotFoundError(p)
    if not is_excel_path(p):
        raise ValueError(f"No es un archivo Excel soportado: {p.suffix}")

    xl = pd.ExcelFile(p, engine="openpyxl")
    info = ExcelFileInfo(path=p.resolve(), sheet_names=tuple(xl.sheet_names))
    df = pd.read_excel(xl, sheet_name=sheet_name, **kwargs)
    return df, info
