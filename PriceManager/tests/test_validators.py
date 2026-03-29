"""Pruebas de validadores."""

from pathlib import Path

from app.utils.validators import is_excel_path


def test_is_excel_path():
    assert is_excel_path(Path("libro.xlsx")) is True
    assert is_excel_path(Path("libro.XLSX")) is True
    assert is_excel_path(Path("notas.txt")) is False
