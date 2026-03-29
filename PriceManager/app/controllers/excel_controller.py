"""Casos de uso relacionados con Excel."""

from pathlib import Path

import pandas as pd

from app.models.excel_file import ExcelFileInfo
from app.services.excel_service import read_excel_file
from app.utils.logger import get_logger

_logger = get_logger(__name__)


class ExcelController:
    """Orquesta la lectura de Excel para la capa de presentación."""

    def load_sheet(
        self,
        path: Path | str,
        sheet_name: str | int | None = 0,
    ) -> tuple[pd.DataFrame, ExcelFileInfo]:
        return read_excel_file(path, sheet_name=sheet_name)

    def load_sheet_safe(
        self,
        path: Path | str,
        sheet_name: str | int | None = 0,
    ) -> tuple[pd.DataFrame | None, ExcelFileInfo | None, str | None]:
        """
        Igual que load_sheet pero sin lanzar excepciones hacia la UI.
        Devuelve (dataframe, info, mensaje_error).
        """
        try:
            df, info = self.load_sheet(path, sheet_name=sheet_name)
            return df, info, None
        except Exception as exc:  # noqa: BLE001 — capa fina para UI
            _logger.exception("Error al leer Excel")
            return None, None, str(exc)
