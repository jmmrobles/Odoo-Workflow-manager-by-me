"""Pruebas básicas del servicio Excel (ampliar con fixtures reales)."""

import pytest

from app.services.excel_service import read_excel_file


def test_read_excel_missing_file(tmp_path):
    missing = tmp_path / "no_existe.xlsx"
    with pytest.raises(FileNotFoundError):
        read_excel_file(missing)
